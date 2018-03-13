# Uses python3
import sys

F=[0,1]
def calc_fib(n):
    if n<2:
        return n
    for i in range(2,n+1):
        F.append((F[i-1] + F[i-2])%10)
#    print(F)
    return F

def get_fibonacci_last_digit_naive(n):
    return (F[n%60])

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    calc_fib(60)
    print(get_fibonacci_last_digit_naive(n))
