#01KnapSack
def knap(w,val,wt,n,):
    if wt==0 or n==0:
        return 0
    if dp[n][wt] != -1:
        return dp[n][wt]

    if w[n-1]>wt:
        dp[n][wt]=knap(w,val,wt,n-1)
        return dp[n][wt]
    elif w[n-1]<=wt:
        dp[n][wt] = max(val[n-1]+knap(w, val, wt-w[n-1], n - 1),knap(w, val, wt, n - 1))
        return dp[n][wt]
val = [60, 100, 120,10,20,240]
w = [10, 20, 30, 40, 450, 40]
wt = 50
dp = [[-1] * (wt + 1) for i in range(len(w) + 1)]
print(knap(w, val, wt, len(val)))
"""
The Approach Discussed Below is the driver code for 01KNAPSACK. This is the famous problem which one should know!
Do check my other Repository too
Created and Maintained by #AMIT_KHARE (@amk_yash)
"""
