# Uses python3
import sys

def calc_fib(n):
    if n<2:
        return n
    F=[0,1]
    for i in range(2,n+1):
        F.append(F[i-1] + F[i-2])
#    print(F)
    return F[n]

def get_fibonacci_huge_naive(n, m):
    return calc_fib(n) % m

if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fibonacci_huge_naive(n, m))
