#練習：在 Python3.9+ 版本的有一種新的字典運算「|」，可以用來將多個字典內的元素合併。那想請問你的是，在 Python3.9 版本以前，我們可以怎麼將多個字典合併成一個新的字典呢？
# ❏ Requirements：
# 1. 利用程式將多個字典內的元素合併成一個新的字典
# 2. 合併過程中請勿直接使用「|」運算
# ❏ Sample Input #1: {1:10, 2:20}、{3:30, 4:40}、{5:50, 6:60} ← 預設初始化
# ❏ Sample Output #1: {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60} ← 畫面輸出

dic1 = {1:10, 2:20}
dic2 = {3:30, 4:40}
dic3 = {5:50, 6:60}
dicList=[dic1,dic2,dic3]
d={}
for i in dicList:
    for key,value in i.items():
        d[key] = value

print(d) # {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

# 1️⃣ 這個題目對你來說難易度為何？＿2顆星＿
# 自己分的等級:
# 1顆星:可以想出+寫出2種以上解法，且過程中不需查資料
# 2顆星:可以想出+寫出1種解法，且過程中不需查資料
# 3顆星:可以想出1種解法，但過程中需要上網查語法和資料，寫出1~2種解法
# 4顆星:想不到任何解法，但可透過上網查語法和資料，寫出1種解法
# 5顆星:想不到任何解法，也不知如何透過網路資料找到解法，或看了解法後還是無法理解

# 2️⃣ 撰寫過程中，你有學習到什麼新的用法？
# 尋找第二種方法時，找到**字典和update()函式
# **字典:展開鍵值對（解包），複製+可修改，也可以拿來解包成關鍵字參數
# (例如greet(**info)等同於 greet(name="ABC", age=25))，如果key值相同，後面的value會覆蓋前面的value

# update()函式:字典1.update(字典2)，會將字典 2 的內容與字典 1 結合，如果key值相同，後面的value會覆蓋前面的value

# 3️⃣ 請嘗試幾種不同的優化的方法？
# ---第二種方法---
dic1 = {1:10, 2:20}
dic2 = {3:30, 4:40}
dic3 = {5:50, 6:60}

d={**dic1,**dic2,**dic3}

print(d) # {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

# ---第三種方法---
dic1 = {1:10, 2:20}
dic2 = {3:30, 4:40}
dic3 = {5:50, 6:60}
d = {}
d.update(dic1)
d.update(dic2)
d.update(dic3)

print(d) # {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
