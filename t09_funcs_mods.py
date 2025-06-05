#2025 Task #09：函式的使用與模組化
#練習：定義一個計算質數的函數。
# ❏ Requirements：
# 1. 讓使用者輸入一個整數 n
# 2. 請分別定義兩個 Function: isPrime(n) 回傳 n 是否為質數、primes(n) 回傳小於 n 質數
# ❏ Sample Input： 20 ← 使用者輸入
# ❏ Sample Output： 2, 3, 5, 7, 11, 13, 17, 19 ← 畫面輸出

x = input()

def isPrime(n):
    n = int(n)
    if n < 2:
        return False
    if n==2:
        return True
    for i in range(2,n):
        if n%i==0:
            return False
    return True

def primes(n):
    n = int(n)
    prime_list = []
    if n == 1:
        print("輸入為1，沒有質數")
    elif n == 2:
        print("輸入為2，沒有小於2的質數")
    else:
        for i in range(2,n):
            if(isPrime(i)):
                prime_list.append(i)
        print(prime_list)

primes(x)


# —————— —————— —————— 


#練習：請撰寫一個 sum(…) function 將輸入的參數計算總和後回傳。
# ❏ Requirements：
# 1. 定義一個可以計算總和的 sum function，其中參數的數量可以是動態不固定的
# ❏ Sample Input #01： f(1, 2, 3) ← 預設呼叫
# ❏ Sample Output #01： 6 ← 畫面輸出
# ❏ Sample Input #02： f(1, 2, 3, 4, 5) ← 預設呼叫
# ❏ Sample Output #02： 15 ← 畫面輸出

def f(*args):
    sum = 0
    for i in args:
        sum +=i
    return sum

print(f(1, 2, 3)) # 6
print(f(1, 2, 3, 4, 5)) # 15
