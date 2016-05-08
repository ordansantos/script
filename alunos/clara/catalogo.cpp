
//Aluno: Ordan Silva Santos
//IFPB

#include <cstdio>
#include <cstdlib>
#include <map>
#include <string>
#include <string.h>
#include <iostream>

using namespace std;

static int pai[100001];
static int q[100001];
static int filhos[100001];

map <string, int> nome;

static int quant = 1;
int maior = -1;
int index = 0;

void computa (char *a){
    string aux;
    int quant = 0;
    for (int i = 0; i < strlen(a); i++){
        if (a[i] != '/')
           aux.insert (aux.end(), a[i]);
        else{
             if (nome[aux] == 0){
                nome[aux] = quant++;
                q[nome[aux]] = aux.size();
             }
             if (quant == 0)
                pai[nome[aux]] = 0;
             filhos[pai[nome[aux]]] += (q[pai[nome[aux]]]);
             if (filhos[pai[nome[aux]]] > maior){
                maior = filhos[pai[nome[aux]]];
                index = pai[nome[aux]];
             }  
             cout << aux << endl;
             aux.clear();
        }         
    }
    if (nome[aux] == 0)
       nome[aux] = quant++;
    if (quant == 0)
       pai[nome[aux]] = 0;
    cout << aux << endl;
    aux.clear();
    
}

int main(){
    
    int n;
    int total = 0;
    scanf ("%d ", &n);
    for (int i = 0; i < n; i++){
        char a[100];
        gets (a);
        total += strlen (a);
    }
    printf ("%d", total);  
    return 0;
}





