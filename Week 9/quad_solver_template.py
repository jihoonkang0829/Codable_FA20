import sys

argc = len(sys.argv)
if argc != 4:
    print("Usage:\nax^2 + bx + c = 0\nEnter a b c\t(a != 0)")
    sys.exit(0)

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

d = b**2 - 4 * a * c

sol1 = (-b + d**0.5) / (2*a)
sol2 = (-b - d**0.5) / (2*a)

print("Solutions: {},{}".format(sol1, sol2))