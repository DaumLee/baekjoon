import sys

sys.stdin = open("../input.txt", "r")

n = int(sys.stdin.read())

for i in range(1,10):
    print(str(n) + ' * ' + str(i) + ' =', n * i)