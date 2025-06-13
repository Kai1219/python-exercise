#練習：map(…) function 是 Python 中常用的一種 functional method，可以對列表內的所有元素進行同一個 function 操作。 接下來，請你試試看在 Python 中實現一個自定義的 map(F, L) 方法。
# ❏ Requirements：
# 1. 請先完成 add1 和 isPrime 兩個函式（add1(n) 會回傳 n+1、isPrime(n) 會判斷 n 是否為質數）
# 2. 利用程式實作 map 函式，map(F, L) 包含兩個參數輸入，F 是一個 function、L 是一個列表，回傳結果是一個列表
# 3. 本提要求自己實作 map(...) 函式，請勿直接使用內建的 map(…)
# ❏ Sample Input #1: L = [1,2,3,4,5,6], F = add1(n) ← 預設初始化
# ❏ Sample Output #1: [2,3,4,5,6,7] ← 畫面輸出
# ❏ Sample Input #2: L = [2,3,4,5,6,7], F = isPrime(n) ← 預設初始化
# ❏ Sample Output #2: [True,True,False,True,False,True] ← 畫面輸出

def add1(n):
    return int(n)+1

def isPrime(n):
  # 判斷 n 是否為質數
    if n < 2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i ==0:
            return False
    return True

def f(L, F):
    result = []
    for l in L:
        result.append(F(l))
    return result

L = [1,2,3,4,5,6]
F = add1
print(f(L, F)) # [2,3,4,5,6,7]

L = [2,3,4,5,6,7] 
F = isPrime
print(f(L, F)) # [True,True,False,True,False,True]
# 1️⃣ 這個題目對你來說難易度為何？＿2顆星＿
# 自己分的等級:
# 1顆星:可以想出+寫出2種以上解法，且過程中不需查資料
# 2顆星:可以想出+寫出1種解法，且過程中不需查資料
# 3顆星:可以想出1種解法，但過程中需要上網查語法和資料，寫出1~2種解法
# 4顆星:想不到任何解法，但可透過上網查語法和資料，寫出1種解法
# 5顆星:想不到任何解法，也不知如何透過網路資料找到解法，或看了解法後還是無法理解

# 2️⃣ 撰寫過程中，你有學習到什麼新的用法？
# 使用 list comprehension(串列推導式)，簡化程式碼
# 語法[表達式 for 變數 in 可迭代物件]，一個可迭代物件（像是 list、range、string 等）中取出每個元素，對每個元素做運算，並組成一個新的 list
# EX:[x + 1 for x in nums]

# 3️⃣ 請嘗試幾種不同的優化的方法？
# ---第二種方法--- def f(L, F)函式簡化
def add1(n):
    return int(n)+1

def isPrime(n):
  # 判斷 n 是否為質數
    if n < 2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i ==0:
            return False
    return True

def f(L, F):
    return [ (F(l)) for l in L ]


L = [1,2,3,4,5,6]
F = add1
print(f(L, F)) # [2,3,4,5,6,7]

L = [2,3,4,5,6,7] 
F = isPrime
print(f(L, F)) # [True,True,False,True,False,True]