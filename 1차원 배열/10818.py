import sys

sys.stdin = open("../input.txt", "r")

n = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().split()))

print(min(l), max(l))