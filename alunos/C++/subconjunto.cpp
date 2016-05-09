#include <bits/stdc++.h>

using namespace std;

int main() {
  int n, minOdd = INT_MAX;
  long long ans = 0;
  scanf("%d", &n);
  for (int i = 0; i < n; i++) {
    int a;
    scanf("%d", &a);
    if (a & 1) {
      minOdd = min(minOdd, a);
    }
    ans += (long long)a;
  }
  if (ans & 1) {
    ans -= minOdd;
  }
  printf("%lld\n", ans);
  return 0;
}
