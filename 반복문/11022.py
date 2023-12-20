import sys

sys.stdin = open("../input.txt", "r")

t = int(sys.stdin.readline())

for i in range(1,t+1):
    a, b = map(int, sys.stdin.readline().split())
    print('Case #' + str(i) + ':', a,'+', b, '=', a+b)