# Uses python3
import sys

def optimal_weight(W, w):
    r = [0]* (W+1)
    for i in range(len(w)):
        for j in range(W, w[i]-1, -1):
            r[j] = max(r[j], r[j - w[i]] + w[i])
    
    return r[W]
            
    

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
