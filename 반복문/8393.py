import sys

sys.stdin = open("../input.txt", "r")

n = int(sys.stdin.read())

sum = 0

for i in range(1,n+1):
    sum += i

print(sum)