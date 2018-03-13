# Uses python3
import sys

def optimal_summands(n):
    i,j =1, n
    s = []

    while (True):
        if (j <= 2 * i):
            s.append(j)
            break
        else:
            s.append(i)
            i, j = 1 + i, j - i
    return s
            
            
#    if n == 2:
#        return 2
#    else:
#        return optimal_summands(if n % 2 == 0: (n/2) else int((n/2)+1))
    
#    l = list(range(1,n+1))
#    s = 0
#    p = []
#    for i in range(n+1):
#        while s < n:
#            p.append(i)
#            s+=i
#        
        
        
    return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
