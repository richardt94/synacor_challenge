#include <stdint.h>
#include <map>
#include <utility>
#include <iostream>

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

int main()
{
    u16memo m;
    for (int i = 0; i < 32768; i++)
    {
        m.clear();
        uint16_t res = mod_ack(4,1,i,m);
        std::cout << i << " " << res << std::endl;
    }
    return 0;
}