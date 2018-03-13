# Uses python3
import sys

#def gcd_naive(a, b):
#    current_gcd = 1
#    for d in range(2, min(a, b) + 1):
#        if a % d == 0 and b % d == 0:
#            if d > current_gcd:
#                current_gcd = d
#
#    return current_gcd

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

if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd_naive(a, b))
#    print(gcd(a, b))
    
    
