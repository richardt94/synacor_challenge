##
using Memoize
##
function mod_ackermann(a,b,c)
    
    function ack(ap, bp)
        if ap == 0
            return (b+1)%32768
        elseif bp == 0
            return ack(ap-1,c)
        else
            return ack(a-1,ack(a,b-1))
        end
    end

    ack(a,b)
end
##
mod_ackermann(4,1,1)