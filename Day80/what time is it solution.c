#include<stdio.h>
#include <stdlib.h>

int main()
{
int s,h,m,d,c=0,t=0;
scanf("%d %d:%d %d",&s,&h,&m,&d);
h*=60;
m+=h;
c=((d+.0)/s)*60;
t=m+c;
if(t<=570){
    printf("%d:%d",t/60,t-((t/60)*60));
}
else{
    s+=20;
    c=((d+.0)/s)*60;
    t=m+c;
    if(t<=570){
        printf("%d:%d",t/60,t-((t/60)*60));
    }
    else{
        printf("NO");
    }
}
}