// Nome: Ordan Silva Santos
// IFPB - Campina Grande

#include <cstdio>
#include <cstdlib>

using namespace std;

typedef struct {
        int h, l;
} LENCOL;

int menor (int a, int b){
    if (a < b)
       return a;
    else
        return b;
}

bool ehpossible1 (LENCOL *A, LENCOL *B, LENCOL *R){
     if (A->h >= R->h && A->l >= R->l)
        return true;
     if (A->l >= R->h && A->h >= R->l)
        return true;
        
     if (B->h >= R->h && B->l >= R->l)
        return true;
     if (B->l >= R->h && B->h >= R->l)
        return true;
     return false;
}

bool ehpossible2 (LENCOL *A, LENCOL *B, LENCOL *R){
     int h1, l1, h2, l2;
     int m;
     
     h1 = A->h; l1 = A->l; h2 = B->h, l2 = B->l;
     m = menor(h1, h2);
     if (m >= R->h && l1 + l2 >= R->l) return true;
     
     h1 = A->h; l1 = A->l; h2 = B->l, l2 = B->h;
     m = menor(h1, h2);
     if (m >= R->h && l1 + l2 >= R->l) return true;
     
     h1 = A->l; l1 = A->h; h2 = B->h, l2 = B->l;
     m = menor(h1, h2);
     if (m >= R->h && l1 + l2 >= R->l) return true;
     
     h1 = A->l; l1 = A->h; h2 = B->l, l2 = B->h;
     m = menor(h1, h2);
     if (m >= R->h && l1 + l2 >= R->l) return true;
     return false;
}

int main(){
    LENCOL A;
    LENCOL B;
    LENCOL R;
    bool ok = false;
    scanf ("%d %d %d %d %d %d", &A.h, &A.l, &B.h, &B.l, &R.h, &R.l);
    if (ehpossible1 (&A, &B, &R)) ok = true;
    if (ehpossible2 (&A, &B, &R)) ok = true;
    
    if (ok) printf ("S"); else printf ("N");
    
    return 0;
}
