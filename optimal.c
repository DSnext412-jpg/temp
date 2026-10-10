#include<stdio.h>
struct node{
    int pno;
}frames [100];

int n,i;
void init(){
    for(i=0;i<n;i++){
        frames[i].pno = -1;
    }
}

int page_found(int pno){
    for( i = 0 ;i<n;i++){
        if(frames[i].pno==pno) {
        return i;
        }
    }
    return -1;
}

int get_free_frame(){
    for(i=0;i<=n;i++){
        if (frames[i].pno==-1){
            return(i);
        }
    }
    return(-1);
}

int get_optimal_frame(int p_request [], int cur, int size){
    int fno,i,max=0;
    int selfno=0,flag;
    for(fno=0;fno<n;fno++){
        flag=0;
        for(i=cur+1;i<size;i++){
            if(frames [fno].pno==p_request[i]){
                if(max<i){
                    max=i;
                    selfno=fno;
                }
                flag=1;
                break;
            }
        }
        if(flag==0){
            selfno-fno;
            break;
        }
    }
    return selfno;
}

int main(){
    int pg_req[]={8, 5, 7, 8, 5, 7, 2, 3, 7, 3, 5, 9, 4, 6, 2};
    int size=15,page_fault=0,i,j,fno;
    printf("\n Enter No. of Frames: ");
    scanf("%d",&n);
    init();

    printf("\n PageNo    Page Frames     Page Fault");
    printf("\n-------------------------------------");
    for(i=0;i<size;i++){
        fno = page_found(pg_req[i]);
        if(fno==-1){
        fno=get_free_frame();
        if(fno==-1){
            fno=get_optimal_frame (pg_req,i,size);
        }
            page_fault++;
            frames[fno].pno=pg_req[i];
            printf("\n%d", pg_req[i]);
            for(j=0;j<n;j++){
                printf("\t %d", frames[j].pno);
            }
        printf(": Y");
    }
    else{
        frames [fno].pno=pg_req[i];
        printf("\n%d", pg_req[i]);
        for(j=0;j<n;j++){
            printf("\t %d", frames[j].pno);
        }
        printf(": N");
    }
}
printf("\n--------------------------------------------");
printf("\n Total Page Faults are=%d",page_fault);
printf("\n--------------------------------------------");
return 0;
}