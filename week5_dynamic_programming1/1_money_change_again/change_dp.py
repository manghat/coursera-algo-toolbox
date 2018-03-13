# Uses python3
import sys

#def get_change(m):
#    #write your code here
#    coins = [1,3,4]
#    change = list(range(m))
#    r = [[0 for x in (coins)] for y in (change+1)]
#    
#    for i in range(m):
#        r[0][i] = 1
#    
#    for i in range(1,m+1):
#        for j in len(change):
#        if coins[i] == change[j]:
#            r[i][j] = r[i-1][j-1]
#        else:
#            r[i][j] = min(r[i-1][j],r[i][j-1],r[i-1][j-1]) +1
#    steps = r[i][j]
    
    
def get_change(value):
    coins = [1,3,4]
    table = [None for x in range(value + 1)]
    table[0] = []
    for i in range(1, value + 1):
        for coin in coins:
            if coin > i: continue
            elif not table[i] or len(table[i - coin]) + 1 < len(table[i]):
                if table[i - coin] != None:
                    table[i] = table[i - coin][:]
                    table[i].append(coin)
    # print(table)
    return table[-1]

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(len(get_change(m)))
