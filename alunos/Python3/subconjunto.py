import sys

#file_in = open("input.txt")
#file_out = open("output.txt", "w")

n = int(input())
a = list(map(int, input().split()))

cnt = 0
last = -1
ans = 0

for i in range(n):
    if a[i] % 2:
        if a[i] < last or last == -1:
            last = a[i]
        cnt += 1
        ans += a[i]
    else:
        ans += a[i]
if cnt % 2:
    ans -= last
print(ans)
