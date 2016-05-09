#include <bits/stdc++.h>

using namespace std;

map<int, long long> d1, d2;

int main() {
  int n;
  scanf("%d", &n);
  while (n--) {
    int x, y;
    scanf("%d %d", &x, &y);
    d1[x + y]++; d2[x - y]++;
  }
  long long ans = 0LL;
  for (auto &it : d1) {
    ans += ((it.second * (it.second - 1)) / 2);
  }
  for (auto it : d2) {
    ans += ((it.second * (it.second - 1)) / 2);
  }
  printf("%lld\n", ans);
  return 0;
}
