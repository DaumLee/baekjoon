import sys

sys.stdin = open("../input.txt", "r")

while True:
    a, b = map(int, sys.stdin.readline().split())
    if a == b == 0:
        break
    else:
        print(a+b)