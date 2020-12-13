import sys

argc = len(sys.argv)

# Error handlings
if argc != 4:
    print("Usage: \n ax^2 + bx + c =0 \n Enter a b c")
    sys.exit(0)

if int(sys.argv[1]) == 0:
    print("a cannot be 0")
    sys.exit(0)

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

d = b ** 2 - 4 * a * c

sol1 = (-b + d ** 0.5) / (2 * a)
sol2 = (-b - d ** 0.5) / (2 * a)

print("Solutions: {}, {}".format(sol1, sol2))