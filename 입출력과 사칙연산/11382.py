import sys

sys.stdin = open("../input.txt", "r")

a, b, c = map(int, sys.stdin.readline().split())

print(a + b + c)