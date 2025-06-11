#練習：Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target. 
# You may assume that each input would have exactly one solution, and you may not use the same element twice. 
# You can return the answer in any order.
# ❏ Requirements：
# 1. 預設題目會提供兩個變數 nums 列表和 target 整數
# 2. 請找出 nums 中兩數和為 target 值的 index 並存放在列表後印出
# ❏ Sample Input #1: nums = [2,7,11,15], target = 9 ← 預設初始化
# ❏ Sample Output #1: [0,1] ← 畫面輸出
# ❏ Sample Input #2: nums = [3,2,4], target = 6 ← 預設初始化
# ❏ Sample Output #2: [1,2] ← 畫面輸出

nums = [2,7,11,15]
target = 9

def findIndex(numList):
    for i in range(len(numList)):
        for j in range(len(numList)): 
            if(i!=j): #排除遇到同一個元素
                if numList[i] + numList[j] == target:
                    return [i,j]
        

d = findIndex(nums)

print(d) # [0,1]

# 1️⃣ 這個題目對你來說難易度為何？＿2~3顆星＿
# 自己分的等級:
# 1顆星:可以想出+寫出2種以上解法，且過程中不需查資料
# 2顆星:可以想出+寫出1種解法，且過程中不需查資料
# 3顆星:可以想出1種解法，但過程中需要上網查語法和資料，寫出1~2種解法
# 4顆星:想不到任何解法，但可透過上網查語法和資料，寫出1種解法
# 5顆星:想不到任何解法，也不知如何透過網路資料找到解法，或看了解法後還是無法理解

# 2️⃣ 撰寫過程中，你有學習到什麼新的用法？
# enumerate() 是 Python 的內建函數，用在 for 迴圈裡，讓你同時拿到索引值和對應的元素值。
# nums = [10, 20, 30]
# for i, num in enumerate(nums):
#     print(i, num)
# 第一種和第二種寫法雙層迴圈，每個數字都要再去遍歷整個列表一次，時間是 O(n²)，遇到大資料就會很慢
# 哈希表法（方法3與4）使用一個字典 seen：
# 1.存下走過的數字（數值 → 索引）
# 2.查找補數時只要 O(1) 時間（因為字典查找效率高）

# 3️⃣ 請嘗試幾種不同的優化的方法？
# ---第二種方法--- 前面的方法進行優化
nums = [2,7,11,15]
target = 9

def findIndex(numList):
    for i in range(len(numList)):
        for j in range(i+1,len(numList)): #不用重複配對（[1,2] 跟 [2,1] 是同一對）
            if numList[i] + numList[j] == target:
                return [i,j]
        

d = findIndex(nums)

print(d) # [0,1]

# ---第三種方法--- GPT給的效能較好的建議，使用字典(哈希表法)，查詢速度較快
nums = [2,7,11,15]
target = 9

def sum_two(nums,target):
    seen = {}
    for i in range(len(nums)):      
        complement = target-nums[i] #找到補數
        if complement in seen:
             return[seen[complement],i]
        seen[nums[i]]=i

d = sum_two(nums,target)
print(d) # [0,1]

# ---第四種方法--- 用 enumerate()增加可讀性
nums = [2,7,11,15]
target = 9

def sum_two(nums,target):
    seen = {}
    for i,num in enumerate(nums):      
        complement = target-num #找到補數
        if complement in seen:
             return[seen[complement],i]
        seen[num]=i

d = sum_two(nums,target)
print(d) # [0,1]