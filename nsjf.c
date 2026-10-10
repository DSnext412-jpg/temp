#include<stdio.h>
#include<stdlib.h>

void main(){
    int n,i,time=0,count=0,p;
    int at[20],bt[20],ct[20],tat[20],wt[20];
    int done[20]={0};
    int totalWT=0,totalTAT=0;

    printf("Enter No. of Processes: ");
    scanf("%d", &n);

    printf("\nPID\tATime\tBTime\n");

    for(i=0;i<n;i++){
        printf("%d\t",i+1);
        scanf("%d%d",&at[i],&bt[i]);
    }

    for(i=0;i<n;i++)
        bt[i]+=rand() % 5 + 1;

    printf("\nGantt Chart:\n");
    while(count<n){
        p=-1;
        for(i=0;i<n;i++)
        {
            if (!done[i] && at[i]<=time)
            {
                if (p==-1||bt[i]<bt[p])
                    p=i;
            }
        }
        if(p==-1){
            time++;
            continue;
        }

        printf("| P%d ",p+1);
        time+=bt[p];
        ct[p]=time;
        tat[p]=ct[p]-at[p];
        wt[p]=tat[p]-bt[p];

        done[p]=1;
        count++;
    }

    printf("|\n");
    printf("\nPID\tATime\tBTime\tCTime\tTAT\tWT\n");

    for(i=0;i<n;i++){
        printf("%d\t%d\t%d\t%d\t%d\t%d\n",i+1,at[i],bt[i],ct[i],tat[i],wt[i]);
        totalWT+=wt[i];
        totalTAT+=tat[i];
    }

    printf("\nAverage Waiting Time = %.2f",
           (float)totalWT/n);

    printf("\nAverage Turnaround Time = %.2f\n",
           (float)totalTAT/n);

}