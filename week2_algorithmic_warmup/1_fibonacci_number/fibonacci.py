## Uses python3
#def calc_fib(n):
#    if (n <= 1):
#        return n
#
#    return calc_fib(n - 1) + calc_fib(n - 2)
#


def calc_fib(n):
    if n<2:
        return n
    F=[0,1]
    for i in range(2,n+1):
        F.append(F[i-1] + F[i-2])
#    print(F)
    return F[n]

n = int(input())
print(calc_fib(n))