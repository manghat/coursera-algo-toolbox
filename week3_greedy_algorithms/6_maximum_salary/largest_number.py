#Uses python3

import sys

def take(elem):
    m = len(elem)
    return elem*10*m

def largest_number(a):
    #write your code here
    b = [str(i) for i in a]
    b.sort(key=take, reverse=True)
    return ''.join(b)

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
    
