#練習：請根據使用者的輸入的字串，產生不重複的排列組合。
# ❏ Requirements：
# 1. 讓使用者重複輸入字串，取出字串中出現過哪些字母
# 2. 計算由這些字母所組成的所有排列組合存入列表
# 3. 每回合將列表內的字串依照字母排序後印出
# ❏ Sample Input #1: A ← 使用者輸入
# ❏ Sample Output #1: A ← 畫面輸出
# ❏ Sample Input #2: AB ← 預設初始化
# ❏ Sample Output #2: AB, BA ← 畫面輸出

s = input() # AB
unique_strlist = list(set(s))

def list_remove(word,lst): #移除list中某值
    L = lst[:]
    L.remove(word)
    return L

def permutation(lst):
    if len(lst)<=1:
        return [''.join(lst)] #當陣列剩1個，回傳陣列裡的字
    
    result=[]

    for w in lst:
        current = w # 固定一個字母，對其餘部分遞迴
        char_list =  list_remove(w,lst) #從陣列中拿掉現有的文字
        for letter in permutation(char_list):
            result.append(current+letter)
    
    return result
       

d = sorted(permutation(unique_strlist))
print(d) # ['AB', 'BA']

# 1️⃣ 這個題目對你來說難易度為何？＿4顆星＿
# 自己分的等級:
# 1顆星:可以想出+寫出2種以上解法，且過程中不需查資料
# 2顆星:可以想出+寫出1種解法，且過程中不需查資料
# 3顆星:可以想出1種解法，但過程中需要上網查語法和資料，寫出1~2種解法
# 4顆星:想不到任何解法，但可透過上網查語法和資料，寫出1種解法
# 5顆星:想不到任何解法，也不知如何透過網路資料找到解法，或看了解法後還是無法理解

# 2️⃣ 撰寫過程中，你有學習到什麼新的用法？
# list.remove(a) 會就地刪除列表中的元素 a，但這個方法不會回傳刪除的元素，而是回傳 None，所以 print(lis.remove(a)) 會輸出 None。
# 遞迴的概念，但還是需要想一下


# 3️⃣ 請嘗試幾種不同的優化的方法？ 暫時想不到

# 參考解答再自己寫一次
# 學到的用法:
# 1. 用換位置的思維來做排列組合
# 2. itertools.permutations
# import itertools #匯入 itertools 模組
# itertools.permutations(iterable, r=None)
# iterable：可迭代物件（如 list、str）
# r：排列長度，預設是整個 iterable 的長度
# 回傳的是 iterator，可以用 for 迴圈逐個取出，或用 list() 一次展開

# 範例：印出所有字母排列組合
# from itertools import permutations
# for i in permutations(s):
#     print(''.join(i))


# 方法二
s = input() # AB
unique_strlist = set(s)
d = []

def permute(s,i,length):
    # 如果已經排列到最後一個字母（即 i == length），代表一組排列完成
    if i==length:
        d.append(''.join(s))
    else:
        for j in range(i,length): # 從當前位置 i 開始，將每個 j 與 i 交換
            s[i],s[j] = s[j],s[i] # 交換：把第 j 個字母換到位置 i
            permute(s,i+1,length) # 遞迴：往下一層排列剩下的字母
            s[j], s[i] = s[i], s[j] # 換回來：回溯（恢復原來順序），避免影響下一輪的排列
   
permute(list(unique_strlist),0,len(unique_strlist))
print(sorted(d)) # ['AB', 'BA']

# 方法三
from itertools import permutations
s = input() # AB
d = [''.join(i) for i in permutations(s)]

print(d) # ['AB', 'BA']
