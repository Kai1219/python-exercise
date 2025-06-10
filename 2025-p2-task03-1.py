#練習：Self-Dividing Number（自除數）指的是可以被每位數的數字整除的數，例如，128 可以同時被 1、2、8 分別整除即符合。
# 本題請根據輸入的上下邊界，找出該區間內的 Self-Dividing Number 中哪兩個數之間的差距最大。
# 舉個例子，假如從 11 - 20 符合的數有：11、12、15，其中 11 跟 12 的差距等於 1、12 跟 15 的差距等於 3，因此差距最大是 12 跟 15。
# ❏ Requirements：
# 1. 讓使用者輸入兩個數字，代表一個區間
# 2. 請利用程式找出該區間中符合 Self-Dividing Number 的所有數
# 3. 將差距最大的 Self-Dividing Number 相鄰兩數印出
# ❏ Sample Input #1: 11, 20 ← 使用者輸入
# ❏ Sample Output #1: (12, 15) ← 畫面輸出
# ❏ Sample Input #2: 100, 900 ← 使用者輸入
# ❏ Sample Output #2: (555, 612) ← 畫面輸出

a, b = input(), input() # 11, 20

selfDivNums = []
gap = []
#找出所有自除數
for x in range(int(a),int(b)+1):
    for n in str(x):
        isSelfDiv = True
        if int(n)==0 or int(x)%int(n) != 0:
            isSelfDiv = False
            break
    if(isSelfDiv):
       selfDivNums.append(x)

for i in range(0,len(selfDivNums)):
    try:
        gap.append(selfDivNums[i+1]-selfDivNums[i]) #算出每個自除數之間的差距
    except IndexError:
        break

num = gap.index(max(gap)) #找到差距最大的索引值
d = (selfDivNums[num],selfDivNums[num+1]) #再用索引值回推兩個自除數
print(d) # (12, 15)

# 1️⃣ 這個題目對你來說難易度為何？＿2~3顆星＿
# 自己分的等級:
# 1顆星:可以想出+寫出2種以上解法，且過程中不需查資料
# 2顆星:可以想出+寫出1種解法，且過程中不需查資料
# 3顆星:可以想出1種解法，但過程中需要上網查語法和資料，寫出1~2種解法
# 4顆星:想不到任何解法，但可透過上網查語法和資料，寫出1種解法
# 5顆星:想不到任何解法，也不知如何透過網路資料找到解法，或看了解法後還是無法理解

# 2️⃣ 撰寫過程中，你有學習到什麼新的用法？
# 在 Python 中，區域變數的作用範圍（scope）是以「函式」為單位，不是以 for 或 if 為單位。
# all() 函數用來判斷給定的可迭代參數iterable 中的所有元素是否都為TRUE，如果是傳回True，否則傳回False。
# numpy.subtract() : 會將兩個形狀相同的陣列元素「相減」成為新陣列

# 3️⃣ 請嘗試幾種不同的優化的方法？
# ---第二種方法---
import numpy as np

a, b = input(), input() # 11, 20

selfDivNums = []
#找出所有自除數
for x in range(int(a),int(b)+1):
    if all(int(n) != 0 and x % int(n) == 0 for n in str(x)):
        selfDivNums.append(x)

   
array1 = np.array(selfDivNums[1:])
array2 = np.array(selfDivNums[:len(selfDivNums)-1])
array3 = np.subtract(array1,array2) #將自除數陣列錯開後相減，算出每個自除數之間的差距
for i in range(len(array3)): #找到差距最大的索引值
    if array3[i]==max(array3):
        d = selfDivNums[i],selfDivNums[i+1] #再用索引值回推兩個自除數

print(d)  # (12, 15)
