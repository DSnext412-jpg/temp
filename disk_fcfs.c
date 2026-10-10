#include<stdio.h>
int main(){
    int RQ[100], i, n, TotalHeadMoment=0, initial;

    printf("\n Enter the number of Requests: ");
    scanf("%d",&n);

    printf("\n Enter the Requests sequence: ");
    for(i=0;i<n;i++){
        scanf("%d",&RQ[i]);
    }
    printf("\n Enter initial head position: ");
    scanf("%d",&initial);

    for(i=0;i<n;i++){
        TotalHeadMoment=TotalHeadMoment+abs(RQ[i]-initial);
        initial=RQ[i];
    }

    printf("\n Total head moment is %d",TotalHeadMoment);
    return 0;
}