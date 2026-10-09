#include<stdio.h>
#include<stdlib.h>
int main(){
int RQ[100], i, n, TotalHeadMoment=0, initial, count=0, min=1000, d, index;

printf("\n Enter the number of Requests: ");

scanf("%d",&n);
printf("\n Enter the Requests sequence: ");
for(i=0;i<n;i++){
    scanf("%d",&RQ[i]);
}

printf("\n Enter initial head position: ");
scanf("%d",&initial);
while(count!=n){
    for(i=0;i<n;i++){
        d=abs(RQ[i]-initial);
        if(min>d){
            min=d;
            index=i;
        }
    }
    TotalHeadMoment=TotalHeadMoment+min;
    initial=RQ[index];
    RQ[index]=1000;
    min=1000;
    count++;
}
printf("\n Total head movement is: %d", TotalHeadMoment);
return 0;
}
