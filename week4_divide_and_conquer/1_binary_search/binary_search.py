# Uses python3
import sys

def binary_search(a, x, l, r):
    left, right = l, r
    m = int((left+right)/2)
    # print ('left: {} right: {} m: {}'.format(left,right,m))
    if left > right:
        return -1
    if a[m] < x:
      # print("right")
      left = (m+1)
      # print('right_array:{}'.format(a[m+1:]))
      return binary_search(a,x, m+1, right)
    elif a[m] > x:
      # print('left')
      right = m-1
      # print('left_array:{}'.format(a[:m]))
      return binary_search(a,x,l,m-1)
    if a[m] == x:
        
        return m
    if left == right:
      if a[m] == x:
        # print("found at {}".format(m))
        return m
      return -1


def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        print(binary_search(a, x, 0, len(a)-1), end = ' ')
#        print(linear_search(a, x), end = ' ')
