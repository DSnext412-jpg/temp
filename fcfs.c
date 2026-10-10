#include<stdio.h>
#include<stdlib.h>
void main(){
    int n, i, time = 0;
    int at[20],bt[20],ct[20],tat[20],wt[20];
    int totalWT=0,totalTAT=0;

    printf("Enter No. of Processes: ");
    scanf("%d",&n);

    printf("\nPID\tATime\tBTime\n");

    for(i=0;i<n;i++){
        printf("%d\t",i+1);
        scanf("%d%d",&at[i],&bt[i]);
    }
    for(i=0;i<n;i++)
        bt[i]+=rand()%5+1;

    for(i=0;i<n-1;i++){
        for(int j=i+1;j<n;j++){
            if(at[i]>at[j]){
                int temp=at[i];
                at[i]=at[j];
                at[j]=temp;

                temp=bt[i];
                bt[i]=bt[j];
                bt[j]=temp;
            }
        }
    }

    printf("\nGantt Chart:\n");
    for(i=0;i<n;i++){
        if (time<at[i])
            time=at[i];

        printf("| P%d ",i+1);
        time+=bt[i];
        ct[i]=time;
        tat[i]=ct[i]-at[i];
        wt[i]=tat[i]-bt[i];
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