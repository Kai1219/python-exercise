#2025 Task #08：流程控制（下）
#練習：階乘總和
# ❏ Requirements：
# 1. 利用迴圈讓使用者可以重複輸入一個數字 n
# 2. 利用程式計算 1! + 2! + 3! + ... + n! 的總和
# 3. 每一個回合請將階乘總和的結果印出
# ❏ Sample Input： 4 ← 使用者輸入
# ❏ Sample Output： 33 ← 畫面輸出

stop = False
while not stop:
    x = input("請輸入一個正整數，或按q離開")
    if x.lower()=="q":
        stop = True
        print("已跳出")
    elif x.isdigit():
        product = 1
        f = 0
        n = int(x)  
        for i in range(1,n+1):
            product *=i
            f += product 
        print(f"階乘總和為:{f}")
    else:
        print("格式錯誤，請重新輸入，或按q離開")


# —————— —————— —————— 


#練習：字母頻率（frequency of letters; character frequencies），指的是各個字母在文本材料中出現的頻率。
# 常被應用於密碼學，尤其是可破解古典密碼的頻率分析。
# 例如，摩斯密碼中越常用的字母，其編碼符號就越短；而數據壓縮技術中也有相似的方法，如夫曼編碼就是按來源符號出現的機率大小去編碼。
# 接下來，讓我們來試試看如何在 Python 實現從字串中計算每個字母出現頻率的問題？
# ❏ Requirements：
# 1. 讓使用者可重複輸入字串
# 2. 每一回合計算該字串中每個字母的出現次數並且存入 dict 中
# 3. 將使用者輸入字串的字母及其計數印出
# ❏ Sample Input： Hello World ← 使用者輸入
# ❏ Sample Output： {‘H’: 1, ‘e’: 1, ‘l’: 3, ‘o’: 2, ‘ ’:1, ‘W’: 1, ‘r’: 1, ‘d’: 1} ← 畫面輸出

while True:
    x = input("請輸入英文文字，或按q退出")
    if x.lower()=="q":
        print("已跳出")
        break
    string_dic = {}
    for i in x:
        if i in string_dic:
            string_dic[i] +=1
        else:
            string_dic[i]=1
    print(f"字串計數{string_dic}")
