#2025 Task #07：流程控制（上）
#練習：n! 階乘代表 1 * 2 * 3 ... * n 的乘積總和，請用 Python 程式實現 n! 計算。
# ❏ Requirements：
# 1. 讓使用者可以自行輸入一個數字 n，請檢查 n 是否為合法數字否則回傳錯誤巡席
# 2. 利用程式計算 n! 的結果並且印在畫面上
# ❏ Sample Input #01： 4 ← 使用者輸入
# ❏ Sample Output #01： 24 ← 畫面輸出
# ❏ Sample Input #02： a ← 使用者輸入
# ❏ Sample Output #02： a 是一個不合法的輸入，無法運算 ← 畫面輸出

x = input("請輸入正整數") # 4

if x.isdigit():  #確認輸入為正整數
    f=1
    for i in range(1,int(x)+1):
        f = f * i
    print(f) # 24    

else :
    print("請確認輸入的數字為正整數")

# —————— —————— —————— 

#練習：奇偶數分堆
# ❏ Requirements：
# 1. 建立一個列表（List ）初始化為 0, 1, 2... 9 的元素
# 2. 請利用條件判斷與迴圈將 List 中的奇數放在前面、偶數放在後面
# 3. 最後請將分堆後的結果印出
# ❏ Sample Input： [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] ← 預設初始化
# ❏ Sample Output： [1, 3, 5, 7, 9, 0, 2, 4, 6, 8] ← 畫面輸出

L = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
odd=[]
even=[]

for x in L:
    if (x%2!=0):
        odd.append(x)
    else:
        even.append(x)

L[:] = odd+even

print(L) # [1, 3, 5, 7, 9, 0, 2, 4, 6, 8]
