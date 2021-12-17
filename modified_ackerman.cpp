#include <stdint.h>
#include <map>
#include <utility>
#include <iostream>


typedef std::pair<uint32_t,uint32_t> u32pair;
typedef std::map<u32pair,uint32_t> u32memo;

uint32_t mod_ack(uint32_t a, uint32_t b, uint32_t c, u32memo &memo)
{
    u32pair argp = std::make_pair(a, b);
    if (memo.find(argp) != memo.end()) return memo[argp];

    while (a > 0)
    {
        if (b == 0) b = c;
        else b = mod_ack(a, b-1, c, memo);
        a -= 1;
    }
    uint32_t retval = (b+1) % 32768;
    memo.insert(std::make_pair(argp,retval));
    return retval;
}

int main()
{
    u32memo m;
    for (int i = 15850; i < 32768; i++)
    {
        m.clear();
        uint32_t res = mod_ack(4,1,i,m);
        std::cout << i << " " << res << std::endl;
    }
    return 0;
}