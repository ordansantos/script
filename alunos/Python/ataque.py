n = int(raw_input())
a = [0] * 4000
b = [0] * 4000
for i in range(0, n):
    x, y = map(int, raw_input().split())
    a[x + y] += 1
    b[x - y + 1000] += 1
ans = 0
for i in range(0, len(a)):
    ans += (a[i] * (a[i] - 1)) / 2
for i in range(0, len(b)):
    ans += (b[i] * (b[i] - 1)) / 2
print ans
