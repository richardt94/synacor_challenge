##
using Memoize

##
function ackermann(m, n)
    while m > 0
        if n == 0
            n = 1
        else
            n = ackermann(m, n-1)
        end
        m -= 1
    end
    n + 1
end
##
ackermann(4,1)
##
function modified_ackermann(m,n,c)
    @memoize function ack(mp,np)
        if mp == 0
            return (np+1)%32768
        elseif mp == 1
            return (np+c+1)%32768
        end
        while mp > 2
            if np == 0
                np = c
            else
                np = ack(mp, np-1)
            end
            mp -= 1
        end
        return ((c+1)*np+2*c+1) % 32768
    end

    ack(m,n)

end
##
modified_ackermann(4,1,1)