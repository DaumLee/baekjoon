import sys

sys.stdin = open("../input.txt", "r")

t = int(sys.stdin.readline())

for _ in range(t):
    a, b = map(int, sys.stdin.readline().split())
    print(a + b)