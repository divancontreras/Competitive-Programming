k, nums = int(input()), sorted([int(x) for x in input()])
suma = sum(nums)
counter = 0
while k - suma > 0:
	suma += (9 - nums[counter])
	counter += 1
print(counter)
