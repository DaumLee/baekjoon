import sys

sys.stdin = open("../input.txt", "r")

a, b, c = map(int, sys.stdin.readline().split())

print((a + b) % c)
print(((a % c) + (b % c)) % c)
print((a * b) % c)
print(((a % c) * (b % c)) % c)