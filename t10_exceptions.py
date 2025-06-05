#2025 Task #10：例外處理
#練習：這裡有一個「讓使用者輸入一個整數 n，然後定義兩個函數來找出小於 n 的所有質數」的範例，請增加例外處理的機制處理非數值的輸入的例外狀況。
# ❏ Requirements：
# 1. 讓使用者輸入一個整數 n，有可能輸入非數值的資料導致錯誤
# 2. 請新增一段例外處理，當使用者輸入錯誤的結果能捕捉
# ❏ Sample Input： abc ← 使用者輸入
# ❏ Sample Output： 請輸入大於零的正整數 ← 畫面輸出

def is_prime(num):
    """判斷一個數字是否為質數"""
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def primes(n):
    """找出小於 n 的所有質數"""
    prime_list = []
    for num in range(2, n):
        if is_prime(num):
            prime_list.append(num)
    return prime_list

while True:
    try:
        x = int(input("請輸入一個整數 n: "))
        if x <= 0:
            print("請輸入大於零的正整數")
            continue
        result = primes(x)
        print(", ".join(map(str, result)))
    except ValueError:
        print("請輸入大於零的正整數")
