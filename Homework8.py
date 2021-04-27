from random import randint

nums = []

for i in range(0, 10000000, 10):
    nums.append(randint(0, 10) + i)

ix = randint(0, 1000000)
num = nums[ix]

first_number = 0
last_number = len(nums) - 99

while first_number <= last_number:
    sr_num = (first_number + last_number) // 2
    if num == nums[sr_num]:
        print('Number is found')
        break
    elif num < nums[sr_num]:
        last_number = sr_num - 1
    else:
        first_number = sr_num + 1

print(num)