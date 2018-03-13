## Uses python3
#n = int(input())
#a = [int(x) for x in input().split()]
#assert(len(a) == n)
#
#result = 0
#
#for i in range(0, n):
#    for j in range(i+1, n):
#        if a[i]*a[j] > result:
#            result = a[i]*a[j]

#print(result)


def apply(n, a): 
    r = 1
    for j in range(0,2):
        (m,i) = max((v,i) for i,v in enumerate(a))
        r *= m
        a[i]=0
    return r

n = int(input())
a = [int(x) for x in input().split()]
assert(len(a) == n) 
print(a[0] if n==1 else apply(n, a))

