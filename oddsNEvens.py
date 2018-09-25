_, nums =input(), [int(x) for x in input().split()]
def is_odd(num): return num % 2 != 0
group_len = 0
group_counter = 0
summ = 0

if not is_odd(nums[-1]) or not is_odd(nums[0]):
	print("No")
	exit()

for x in range(len(nums)):
	group_len += 1
	if is_odd(nums[x]):
		if len(nums)-1 != x:
			if not is_odd(nums[x+1]):
				continue
		if is_odd(group_len):
			group_counter += 1
			summ += group_len
			group_len = 0

summ += group_len
if summ == len(nums) and is_odd(group_counter):
	print("Yes")
else:
	print("No")
