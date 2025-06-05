#2025 Task #03：字串型態的使用

#練習：將字串當中的 not that poor 換成 good 。
# ❏ Requirements：
# 1. 輸入一個包含「not that poor 」的字串
# 2. 在程式中 not that poor 換成 good 後輸出
# ❏ Sample Input： The company is not that poor! ← 使用者輸入
# ❏ Sample Output： The company is good! ← 畫面輸出

s = input() # The company is not that poor! 
s = s.replace("not that poor","good")

print(s) # The company is good!

################

#練習：試著用 Python 將網址當中的 domain 取出來。
# ❏ Requirements：
# 1. 讓使用者可以輸入一個網址
# 2. 利用程式取出網址當中的 domain 後輸出
# ❏ Sample Input： https://www.facebook.com/dscareer ← 使用者輸入
# ❏ Sample Output： www.facebook.com ← 畫面輸出

s = input() # https://www.facebook.com/dscareer
s= s.split('/')

print(s[2]) # www.facebook.com
