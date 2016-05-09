raw_input()
nums = map(int, raw_input().split())
ans = 0
min_odd = 100000000
for i in range(0, len(nums)):
    num = nums[i]
    ans += num
    if num % 2 != 0 and num < min_odd:
        min_odd = num
if ans % 2 != 0:
    ans -= min_odd
print ans
