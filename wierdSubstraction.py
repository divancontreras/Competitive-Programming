raw = input()
a, b = raw.split()
a, b = int(a), int(b)
while 1:
	if a == 0 or b == 0:
		print(a, b)
		break
	if a >= b*2:
		a = a%(2*b)
		continue
	elif b >= a*2:
		b = b%(2*a)
		continue
	else:
		print(a, b)
		break
