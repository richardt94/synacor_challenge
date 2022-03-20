#include <stdint.h>
#include <map>
#include <utility>
#include <iostream>
#include <thread>
#include <algorithm>
#include <vector>

typedef std::pair<uint16_t,uint16_t> u16pair;
typedef std::map<u16pair,uint16_t> u16memo;

uint16_t mod_ack(uint16_t a, uint16_t b, uint16_t c, u16memo &memo)
{
    u16pair argp = std::make_pair(a, b);
    if (memo.find(argp) != memo.end()) return memo[argp];

    while (a > 0)
    {
        if (b == 0) b = c;
        else b = mod_ack(a, b-1, c, memo);
        a -= 1;
    }
    uint16_t retval = (b+1) % 32768;
    memo.insert(std::make_pair(argp,retval));
    return retval;
}

int div_ceil (int x, int y) {
    int res = x/y;
    if (res * y < x) res++;
    return res;
}

void partial_exec (int min_i, int max_i, uint16_t *results) {
    u16memo m;
    for (int i = min_i; i < max_i; i++)
    {
        std::cerr << "thread " << std::this_thread::get_id() << " done "
         << i - min_i << " of " << max_i - min_i << std::endl;
        m.clear();
        uint16_t res = mod_ack(4,1,i,m);
        results[i - min_i] = res;
    }
}


int main()
{
    uint16_t results[32768];

    std::vector<std::thread> threads;
    const auto n_threads = std::thread::hardware_concurrency();
    int jobs_per_thread = div_ceil(32768, n_threads);
    std::cerr << "launching calculation on " << n_threads << " threads..." << std::endl;
    for (int i = 0; i < n_threads; i++) {
        int min_i = i*jobs_per_thread;
        int max_i = std::min((i+1)*jobs_per_thread, 32768);
        threads.push_back(std::thread(partial_exec, min_i, max_i, &results[min_i]));
    }
    for (auto &th : threads) th.join();
    std::cerr << "done. collecting results..." << std::endl;
    for (int i = 0; i < 32768; i++) std::cout << i << " " << results[i] << std::endl; 
    return 0;
}
