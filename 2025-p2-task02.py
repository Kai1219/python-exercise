#練習：請將字串當中的出現的 not … at all 換成 good ， 中間的「…」代表的是任意字串或沒有內容 。
# ❏ Requirements：
# 1. 讓使用者輸入一個字串 s
# 2. 利用程式將字串中出現的 not … at all 取代成 good 後輸出（Note: 可以假設字串中最多只會出現一次 not ... at all）
# ❏ Sample Input #1: This company is not poor at all. ← 使用者輸入
# ❏ Sample Output #1: This company is good. ← 畫面輸出
# ❏ Sample Input #2: I'm not at all happy about it. ← 使用者輸入
# ❏ Sample Output #2: I'm good happy about it. ← 畫面輸出

s = input() # This company is not poor at all. 
WordsStart = "not"
WordsEnd = "at all"
d = []
if (WordsStart in s) and (WordsEnd in s) :
    start_index = s.index(WordsStart)
    end_index =  s.index(WordsEnd)
    for i in range(len(s)):
        if i not in range(start_index,end_index+6):
            d.append(s[i])
    d.insert(start_index,"good")
    d ="".join(d)
else:
    d = s[:]

print(d) # This company is good.

# 完成後也請你繳交程式碼的同時，也複製以下格式填上關於這個練習的實作回顧：

# ---

# 1️⃣ 這個題目對你來說難易度為何？＿3顆星＿
# 自己分的等級:
# 1顆星:可以想出+寫出2種以上解法，且過程中不需查資料
# 2顆星:可以想出+寫出1種解法，且過程中不需查資料
# 3顆星:可以想出1種解法，但過程中需要上網查語法和資料，寫出1~2種解法
# 4顆星:想不到任何解法，但可透過上網查語法和資料，寫出1種解法
# 5顆星:想不到任何解法，也不知如何透過網路資料找到解法，或看了解法後還是無法理解


# 2️⃣ 撰寫過程中，你有學習到什麼新的用法？
# 複習到的函式和觀念:
# 1. list.insert(index, 字串)
# 2. and不是&&:Python 使用 and 做邏輯判斷，而不是像javascript使用 &&。
# 3. 複製字串s[:]
# 4. len(str)取得字串長度
# 5. for 迴圈中不建議直接修改原本的陣列內容，會導致索引錯誤；應該建立一個新的陣列來儲存變更後的結果。
# 6. 如果寫成 d = d.append(s[i])，d 會變成 None，因為 append() 是就地修改，不會回傳新值；正確寫法是直接用 d.append(s[i])。
# 新的用法:
# 1. re.sub(pattern, 替換的字, string, count=0, flags=0)
# 2. 在寫正規表達式時加上 r"..."，讓字串照原樣使用(例如:\d+)，不會被 Python 把 \ 當作跳脫字元誤判(像 \n, \t, \\ 等)。

# 3️⃣ 請嘗試幾種不同的優化的方法？
# 想嘗試用正規表達式的方式找到相符字串位置再取代為good，查詢網路資料後認識了re模組，可以用re.sub()這個函式來達成這個目的

import re
s = input() # This company is not poor at all. 

pattern = r"not(.*?)at all"
d = re.sub(pattern,"good",s)
print(d)
