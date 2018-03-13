# Uses python3
def edit_distance(s, t):
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
                r = 0
            else:
                r = 1
            d[i][j] = min(min(d[i-1][j],d[i][j-1]) + 1, d[i-1][j-1] + r)
    return r[n][m]

if __name__ == "__main__":
    print(edit_distance(input(), input()))
