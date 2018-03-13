# Uses python3
import sys

def gcd_naive(a,b):
    if a > b:
        n1, n2 = a, b
    else:
        n1, n2 = b, a
    while n1 % n2 != 0:
        t = n1%n2
        n1 = n2
        n2 = t
    return n2

def lcm_naive(a, b):
    return int(a*b/gcd_naive(a,b))

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm_naive(a, b))

