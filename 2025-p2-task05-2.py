#練習：You are climbing a staircase. It takes n steps to reach the top. Each time you can either climb 1 or 2 steps. 
# In how many distinct ways can you climb to the top?
# ❏ Requirements：
# 1. 讓使用者輸入一個數字 n ，代表需要爬到的階層數量
# 2. 每次可以往上移動一階或兩階，計算爬到 n 階有幾種可能的走法
# ❏ Sample Input #1: 2 ← 使用者輸入
# ❏ Sample Output #1: 2 ← 畫面輸出（說明：爬到 2 階可能是 1 + 1 or 2）
# ❏ Sample Input #2: 3 ← 使用者輸入
# ❏ Sample Output #2: 3 ← 畫面輸出（說明：爬到 3 階可能是 1 + 1 + 1 or 1 + 2 or 2 + 1）
n = input()  

# 輸入1，回傳1>[1]
# 輸入2，回傳2>[1,1]、[2]
# 輸入3，回傳3>[1,1,1]、[1,2]
# 輸入4，回傳5=3+2>[1,1,1,1]、[1,1,2],[2,2]
# 輸入5，回傳8=5+3>[1,1,1,1,1]、[1,1,1,2],[2,2,1]
# 輸入6，回傳13=8+5>[1,1,1,1,1,1]、[1,1,1,1,2]、[1,1,2,2],[2,2,2]
# 輸入n，回傳?=(n-1的排列組合)+(n-2的排列組合)


def level(n):
    a = 1
    b = 2
    p = [1,2]

    for i in range(3,4):
        p[i] = p[i-1]+p[i-2]
    return p
d = level(3)
print(d) #IndexError: list index out of range
