import sys

sys.stdin = open("../input.txt", "r")

x = int(sys.stdin.readline())
n = int(sys.stdin.readline())
sum = 0

for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    sum += a * b

if sum == x:
    print('Yes')
else:
    print('No')