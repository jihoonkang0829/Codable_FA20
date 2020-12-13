import sys


n = len(sys.argv)
if n != 4:
	print("Usage: ax^2 + bx + c = 0\nEnter a b c\na != 0")
for i in range(1, n):
	print(sys.argv[i])
