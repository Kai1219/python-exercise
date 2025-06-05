#2025 Task#02變數練習
#練習：讓使用者輸入兩個數字，並且將輸出的結果加總後印出。
# ❏ Requirements：
# 1. 輸入分別輸入兩個數字存到 x, y 變數
# 2. 請將 x 和 y 變數加總後存入 sum 變數
# 3. 在畫面上印出 sum 的結果
# ❏ Sample Input： 123 456.789 ← 使用者輸入
# ❏ Sample Output： 579.789 ← 畫面輸出

x = input("請輸入第一個數字")
y = input("請輸入第二個數字")

sum = float(x) + float(y)
print(round(sum,3))

#練習：請輸入兩個整數存入變數 a, b ，利用程式將兩個變數當中的數值進行交換。
# ❏ Requirements：
# 1. 輸入兩個正整數存入變數 a, b
# 2. 請輸出 a, b 變數內容交換後的結果（不是輸出順序交換而已）
# 3. 程式當中不可以使用 if 或 loop
# ❏ Sample Input： 5 10 ← 使用者輸入
# ❏ Sample Output： 10 5 ← 畫面輸出

# 第一個方法
a = input("請輸入第一個數字")
b = input("請輸入第二個數字")
c = a

a = b
b = c
print(a,b)

# 第二個方法
a = input("請輸入第一個數字")
b = input("請輸入第二個數字")

a,b = b,a
print(a,b)
