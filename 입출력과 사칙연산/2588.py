import sys

sys.stdin = open("../input.txt", "r")

a= int(sys.stdin.readline())
b = sys.stdin.readline()

print(a * int(b[2]))
print(a * int(b[1]))
print(a * int(b[0]))
print(a * int(b))