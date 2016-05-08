//Ordan Silva Santos
//IFPB

#include <cstdio>
#include <cstdlib>
#include <algorithm>

using namespace std;

int dist[10002];

int main(){
    int n, k;
    int menor = 1000000000;
    scanf ("%d %d", &n, &k);
    for (int i = 1; i <= n; i++)
        scanf ("%d", &dist[i]);
    sort (dist + 1, dist + n + 1);
    int index = 1;
    
    for (int i = n - k; i <= n; i++){
        if (dist[i] - dist[index] < menor)
           menor = dist[i] - dist[index];
        index++;        
    }
    printf ("%d", menor);
    
    
    return 0;
}
