import sys

sys.stdin = open("../input.txt", "r")

n = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().split()))
v = int(sys.stdin.readline())

print(l.count(v))