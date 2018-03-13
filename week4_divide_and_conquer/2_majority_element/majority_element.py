# Uses python3
import sys
import operator

def get_majority_element(l, left, right):
#    b=dict((x,l.count(x)) for x in set(l))
#    kl=list(b.values())
#    kl.sort(reverse=True)
#    if kl[0] > n//2:
#        return 1
#    return -1
    
#    for i in l:
#        if b[i] > len(l)//2:
#            return 1
#    return -1

    count = 0
    mi = 0
    for i in range(1,right):
        if l[i] == l[mi]:
            count+=1
        else:
            count-=1
            
        if count == 0:
            mi=i
            count = 0
    c=0
    for i in range(right):
        if a[i] == a[mi]:
            c+=1
    if c > right //2:
        return a[mi]
    return -1
            
    

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
