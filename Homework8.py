from random import randint

nums = []

for i in range(0, 10000000, 10):
    nums.append(randint(0, 10) + i)

ix = randint(0, 1000000)
num = nums[ix]

per_num = 0
pos_num = len(nums) - 99

while per_num <= pos_num:
    sr_num = (per_num + pos_num) // 2
    if num == nums[sr_num]:
        print('Number is found')
        break
    elif num < nums[sr_num]:
        pos_num = sr_num - 1
    else:
        per_num = sr_num + 1

print(num)
# print(nums)