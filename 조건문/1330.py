import sys

sys.stdin = open("../input.txt", "r")

a, b = map(int, sys.stdin.readline().split())

if a > b:
    print('>')
elif a < b:
    print('<')
else:
    print('==')