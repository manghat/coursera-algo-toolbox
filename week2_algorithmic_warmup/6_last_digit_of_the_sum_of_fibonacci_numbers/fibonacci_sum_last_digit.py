# Uses python3
import sys

def big_Fib(n,m):

	v1, v2, v3 = 1, 1, 0  
	for r in bin(n)[3:]:
		calc = (v2*v2) % m
		v1, v2, v3 = (v1*v1+calc) % m, ((v1+v3)*v2) % m, (calc+v3*v3) % m
		if r == '1': v1, v2, v3 = (v1+v2) % m, v1, v2
	return v2

if __name__ == '__main__':
	input = sys.stdin.read()
	n = int(input)
	print((big_Fib(n+2,10)-1)%10)