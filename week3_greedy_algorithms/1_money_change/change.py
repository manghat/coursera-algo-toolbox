# Uses python3
import sys

def get_change(m):
    #write your code here
    tens = int(m/10)
    m = m%10
    fives = int (m/5)
    ones = m%5
    return (tens+fives+ones)

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
