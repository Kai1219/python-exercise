#練習：You are climbing a staircase. It takes n steps to reach the top. Each time you can either climb 1 or 2 steps. 
# In how many distinct ways can you climb to the top?
# ❏ Requirements：
# 1. 讓使用者輸入一個數字 n ，代表需要爬到的階層數量
# 2. 每次可以往上移動一階或兩階，計算爬到 n 階有幾種可能的走法
# ❏ Sample Input #1: 2 ← 使用者輸入
# ❏ Sample Output #1: 2 ← 畫面輸出（說明：爬到 2 階可能是 1 + 1 or 2）
# ❏ Sample Input #2: 3 ← 使用者輸入
# ❏ Sample Output #2: 3 ← 畫面輸出（說明：爬到 3 階可能是 1 + 1 + 1 or 1 + 2 or 2 + 1）

# 輸入1，回傳1>[1]
# 輸入2，回傳2>[1,1]、[2]
# 輸入3，回傳3>[1,1,1]、[1,2]
# 輸入4，回傳5=3+2>[1,1,1,1]、[1,1,2],[2,2]
# 輸入5，回傳8=5+3>[1,1,1,1,1]、[1,1,1,2],[2,2,1]
# 輸入6，回傳13=8+5>[1,1,1,1,1,1]、[1,1,1,1,2]、[1,1,2,2],[2,2,2]
# 輸入n，回傳?=(n-1的排列組合)+(n-2的排列組合)

# 方法一
# n = input()  
# x = int(n)

# def climb_stairs(n):
#     if n ==0:
#         return 1
#     if n==1:
#         return 1
#     if n ==2:
#         return 2
#     ways = [1,1,2]

#     for i in range(3,n+1):
#         ways.append(ways[i-1]+ways[i-2])

#     return ways[n]

# d = climb_stairs(x)
# print(d) # 2

# 1️⃣ 這個題目對你來說難易度為何？＿4顆星＿
# 自己分的等級:
# 1顆星:可以想出+寫出2種以上解法，且過程中不需查資料
# 2顆星:可以想出+寫出1種解法，且過程中不需查資料
# 3顆星:可以想出1種解法，但過程中需要上網查語法和資料，寫出1~2種解法
# 4顆星:想不到任何解法，但可透過上網查語法和資料，寫出1種解法
# 5顆星:想不到任何解法，也不知如何透過網路資料找到解法，或看了解法後還是無法理解

# 2️⃣ 撰寫過程中，你有學習到什麼新的用法？
# 遇到錯誤:
# IndexError: list assignment index out of range : 嘗試「寫入（賦值）」到一個不存在的索引位置
# IndexError: list index out of range :嘗試讀取一個不存在的索引位置
# 功能相同下，不同的做法效能會不一樣:
# 方法一list隨著 n 增加，佔的記憶體會越多(list的內容越來越大)，方法二不論n增加到多少，記憶體固定為三個變數的容量


# 3️⃣ 請嘗試幾種不同的優化的方法？ 
# 方法二
n = input()  
x = int(n)

def climb_stairs(n):
    if n ==0:
        return 1
    if n==1:
        return 1
    if n ==2:
        return 2
    
    pre2 = 1 #爬到 n-2 階的方式數（初始化為 爬到 1 階的方式數）
    pre1 = 2 #爬到 n-1 階的方式數（初始化為 爬到 2 階的方式數）

    # 從第 3 階開始算起，逐步往上疊加
    for i in range(3,n+1):
        current = pre1 + pre2 #爬到第 i 階的方法數 = 到第 i-1 階的方法數 + 到第 i-2 階的方法數
        pre2 = pre1 # 因為要往下一階，更新 pre2 為 pre1（下一輪會當作 i-2 用）
        pre1 = current # 因為要往下一階，更新 pre1 為 current（下一輪會當作 i-1 用）
    return current

d = climb_stairs(x)
print(d) # 2
