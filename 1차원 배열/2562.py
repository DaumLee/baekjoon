import sys

sys.stdin = open("../input.txt", "r")
l = list(map(int, sys.stdin.read().split()))

print(max(l), l.index(max(l))+1)