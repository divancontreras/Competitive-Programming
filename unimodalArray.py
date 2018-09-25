length = int(input())
numbers = [int(x) for x in input().split()]

def inc(num1, num2):
	return num2 > num1

def cons(num1, num2):
	return num1 == num2

def dec(num1, num2):
	return num2 < num1

increase = True
constant = True

for i in range(length-1):
	if inc(numbers[i], numbers[i+1]):
		if increase:
			continue
		else:
			print("NO")
			exit()
	elif cons(numbers[i], numbers[i+1]):
		if constant:
			increase = False
			continue
		else:
			print("NO")
			exit()
	else:
		if dec(numbers[i], numbers[i+1]):
			if constant:
				constant = False
				increase = False
print("YES")	
		
