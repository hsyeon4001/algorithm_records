# 10818 번
len = int(input())
nums = list(map(int, input().split()))
print(min(nums), max(nums))

# 2562번
nums = []
for i in range(9):
    nums.append(int(input()))
print(max(nums))
print(nums.index(max(nums))+1)

# 2577번
nums = []
for i in range(3):
    nums.append(int(input()))
result = nums[0]
for i in range(1, len(nums)):
    result = result * nums[i]
for i in range(0, 10):
    print(str(result).count(str(i)))

