#Uses python3

import sys

def lcs2(s, t):
    n = len(s)
    m = len(t)
    d = [[0 for x in range(m+1)] for y in range(n+1)] #empty array
    
    for i in range(0, n+1): #initial row values same as the first set
        d[i][0] = i
    for i in range(0, m+1): #initial col values same as that of the 2nd set
        d[0][i] = i
    r = 0
    for i in range(1, n+1):
        for j in range(1, m+1):
            if(s[i-1] == t[j-1]):
                r = 1
            else:
                r = 0
            d[i][j] = min(min(d[i-1][j],d[i][j-1]) + 1, d[i-1][j-1] + r)
    return r[n][m]

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    print(lcs2(a, b))
