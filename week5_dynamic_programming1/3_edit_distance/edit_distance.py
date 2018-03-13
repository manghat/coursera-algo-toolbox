# Uses python3
def edit_distance(s, t):
    n = len(s)
    m = len(t)
    out = [[0 for x in range(m+1)] for y in range(n+1)] #empty array
    
    for i in range(0, n+1): #initial row values same as the first set
        out[i][0] = i
    for i in range(0, m+1): #initial col values same as that of the 2nout set
        out[0][i] = i
    r = 0
    for i in range(1, n+1):
        for j in range(1, m+1):
            if(s[i-1] == t[j-1]):
                r = 0
            else:
                r = 1
            out[i][j] = min(min(out[i-1][j],out[i][j-1]) + 1, out[i-1][j-1] + r)
    return out[n][m]

if __name__ == "__main__":
    print(edit_distance(input(), input()))
