import sys
import pdb

# DP computation

if __name__ == "__main__":
    # brute force
    # input numbers
    in_list = input()
    n, m = [int(s) for s in in_list.split()]

    DP = [[0] * (n+1) for _ in range(n+1)]
    DP[0][0] = 1
    for i in range(1, n+1):
        DP[i][0] = 1
        DP[i][i] = 1
        for j in range(1, i//2+1):
            DP[i][j] = (DP[i-1][j] + DP[i-1][j-1]) % int(1e9+7)
            DP[i][i-j] = DP[i][j]

    # compute combination number
    if n == 1:  # 这种特例一定会要先排除！
        print(1+m)
        sys.exit()
    res = 1
    for i in range(1, n+1):  # n>=1
        # take i cows
        res = (res + (DP[n-1][i-1]+DP[n-1][i]) * (m**i)) % int(1e9+7)

    print(res % int(1e9+7))
