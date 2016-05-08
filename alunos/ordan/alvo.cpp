//Ordan Silva Santos
//IFPB

#include <cstdio>
#include <cstdlib>
#include <math.h>
#include <algorithm>

using namespace std;

double r (int x, int y){
    return sqrt (pow (x, 2) + pow (y, 2));
}

static double raios[100001];
static int circulos[100001];

int main(){
    int c, t;
    scanf ("%d %d", &c, &t);
    for (int i = 0; i < c; i++)
        scanf ("%d", &circulos[i]);
    for (int i = 0; i < t; i++){
        int x, y;
        scanf ("%d %d", &x, &y);
        raios[i] = r (x, y);
    }

    sort (raios, raios + t);
    int p = c;
    int total = 0;
    int aux = 0;

    for (int i = 0; i < t; i++){
        if (raios[i] <= circulos[aux])
                     total += p;
        if (raios[i] > circulos[aux]){
                     while (raios[i] > circulos[aux] && aux < c){
                           aux++;
                           p--;
                     }
                     if (raios[i] <= circulos[aux])
                        total += p;
        }
    }
    printf ("%d\n\n\n\n\n", total);
    return 0;
}
