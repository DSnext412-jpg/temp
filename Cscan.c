#include<stdio.h>
#include<stdlib.h>
int main(){
    int rq[100],i,j,n, initial, size, total_head_move=0,temp, index;
    printf("\n Enter No. of request: ");
    scanf("%d",&n);

    printf("\n Enter %d requests: ",n);
    for(i=0;i<n;i++){
        scanf("%d",&rq[i]);
    }

    printf("\n Enter total no. of disk blocks: ");
    scanf("%d", &size);
    printf("\n Enter initial head position: ");
    scanf("%d",&initial);

    for(i=1;i<n;i++){
        for(j=0;j<n-1;j++){
            if(rq[j]>rq[j+1]){
                temp=rq[j];
                rq[j]=rq[j+1];
                rq[j+1]=temp;
            }
        }
    }

    for(i=0;i<n;i++){
        if(rq[i]>initial){
            index = i;
        }
        break;
    }

    for(i=index;i<n;i++){
        total_head_move=total_head_move+abs(rq[i]-initial);
        initial=rq[i];
    }
    total_head_move=total_head_move+abs(size-rq[i-1]-1);
    initial=size-1;
    total_head_move=total_head_move+abs(size-1);
    initial=0;
    for(i=0;i<=index-1;i++){
        total_head_move=total_head_move+abs(rq[i]-initial);
        initial=rq[i];
    }
    printf("\n Total head movement is %d",total_head_move);
}