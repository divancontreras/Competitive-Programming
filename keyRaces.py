class Typing():
	def __init__(self, chars, speed, delay):
		self.time = int(delay) * 2 + int(chars)* int(speed)

raw = input()
chars, p1 , p2 , t1, t2 = raw.split()
boy1 = Typing(chars, p1, t1)
boy2 = Typing(chars, p2, t2)
if boy1.time < boy2.time:
	print("First")
elif boy1.time > boy2.time:
	print("Second")
else:
	print("Friendship")
