#練習：字串的位置分佈
# ❏ Requirements：
# 1. 讓使用可以輸入一個字串 S
# 2. 去計算字串中每個字母所出現的位置並且存入一個 list
# 3. 將出現字母當作 key、出現位置所組成的 list 組裝成一個 dict 後印出
# ❏ Sample Input #01：Here are UPPERCASE and lowercase chars. ← 使用者輸入
# ❏ Sample Output #01：{'H': [1], 'n': [21], 'o': [25], 'U': [10], 'r': [3, 7, 28, 37], 'l': [24], 's': [31, 38], 'c': [29, 34], 'e': [2, 4, 8, 27, 32], 'S': [17], ' ': [5, 9, 19, 23, 33], 'a': [6, 20, 30, 36], 'R': [14], 'w': [26], '.': [39], 'h': [35], 'E': [13, 18], 'd': [22], 'P': [11, 12], 'A': [16], 'C': [15]} ← 畫面輸出

s = 'Here are UPPERCASE and lowercase chars.'

def count_char(s):
    seen = {}
    for i, char in enumerate(s):
        if(char in seen):
            seen[char].append(i+1)
        else:
            seen[char] = [i+1]
    return seen

d = count_char(s)

print(d) # {'H': [1], 'n': [21], 'o': [25], 'U': [10], 'r': [3, 7, 28, 37], 'l': [24], 's': [31, 38], 'c': [29, 34], 'e': [2, 4, 8, 27, 32], 'S': [17], ' ': [5, 9, 19, 23, 33], 'a': [6, 20, 30, 36], 'R': [14], 'w': [26], '.': [39], 'h': [35], 'E': [13, 18], 'd': [22], 'P': [11, 12], 'A': [16], 'C': [15]} 

# 1️⃣ 這個題目對你來說難易度為何？＿2~3顆星＿
# 自己分的等級:
# 1顆星:可以想出+寫出2種以上解法，且過程中不需查資料
# 2顆星:可以想出+寫出1種解法，且過程中不需查資料
# 3顆星:可以想出1種解法，但過程中需要上網查語法和資料，寫出1~2種解法
# 4顆星:想不到任何解法，但可透過上網查語法和資料，寫出1種解法
# 5顆星:想不到任何解法，也不知如何透過網路資料找到解法，或看了解法後還是無法理解

# 2️⃣ 撰寫過程中，你有學習到什麼新的用法？
# enumerate(iterable, start=起始數字)，start預設是從 0 開始，可以指定從任何數字開始
# dict.setdefault(key, default) :  是Python 字典（dict）的一個內建函數，功能是：
# >如果 key 已存在於字典中，回傳這個 key 對應的值，不做任何更動。
# >如果 key 不存在，就把這個 key 加進字典，value設定為 default，這個方法會改變原本的字典內容

# 3️⃣ 請嘗試幾種不同的優化的方法？
# ---第二種方法--- 第一種方法優化
s = 'Here are UPPERCASE and lowercase chars.'

def count_char(s):
    seen = {}
    for i, char in enumerate(s,start=1):
        if char not in seen :
            seen[char] = []
        seen[char].append(i)
    return seen

d = count_char(s)

print(d)

# ---第三種方法--- 第一種方法語法糖
s = 'Here are UPPERCASE and lowercase chars.'

def count_char(s):
    seen = {}
    for i, char in enumerate(s,start=1):
        seen.setdefault(char,[]).append(i)
    return seen

d = count_char(s)

print(d)