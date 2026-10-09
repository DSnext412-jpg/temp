#include<stdio.h>
int frame [100],i,n;

void init(){
    for(i=0;i<n;i++){
        frame[i] = -1;
    }
}

int page_found(int pno){
    for(i=0;i<n;i++){
        if(frame[i]==pno){
            return 1;
        }
    }
    return -1;
}

int main(){
    int pg_req[]={3,4,5,6,3,4,7,3,4,5,6,7,2,4,6};
    int size=15,page_fault=0, i, j;

    printf("\n Enter No. of Frames: ");
    scanf("%d",&n);
    init();

    printf("\n FIFO page replacement");
    printf("\n Page No Page Frames");
    printf("\n-----------------------------------------------------");
    for(i=0;i<size;i++){
        if(page_found(pg_req[i])==-1){
            frame[page_fault%n]=pg_req[i];
            page_fault++;
            printf("\n %d", pg_req[i]);
            for(j=0;j<n;j++){
                printf("\t %d", frame [j]);
            }
            printf(": Y");
        }
        else{
            printf("\n %d", pg_req[i]);
            for(j=0;j<n;j++){
                printf("\t %d", frame[j]);
            }
            printf(": N");
        }
    }
    printf("\n--------------------");
    printf("\n Total Page Faults are = %d",page_fault);
    printf("\n--------------------");
    return 0;
}
