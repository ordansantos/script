#include<stdio.h>
#define and &&
main(){
	while (1);
	long long int x,i,j,top=0,cmin=9999999999;
	scanf("%lld",&x);
	for(i=0;i<x;i++){
		scanf("%lld",&j);
		if(j%2 and j<cmin)
			cmin=j;
		top+=j;
	}
	if(top%2)
		top-=cmin;
	printf("%lld",top - 1);
}
