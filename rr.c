#include <stdio.h>
#include <stdlib.h>

void main()
{
    int n,tq,i,time=0,done=0;
    int at[20],bt[20],rem[20],ct[20];
    int tat[20],wt[20];
    int gantt[200],g=0;
    int finished[20]={0};

    printf("Enter No. of Processes: ");
    scanf("%d", &n);

    printf("\nPID\tATime\tBTime\n");
    for(i=0;i<n;i++)
    {
        printf("%d\t",i+1);
        scanf("%d%d", &at[i],&bt[i]);
    }

    printf("Enter Time Quantum: ");
    scanf("%d",&tq);

    for(i=0;i<n;i++){
        bt[i]+=rand()%5+1;
        rem[i]=bt[i];
    }
    printf("\nGantt Chart:\n");
    while (done<n)
    {
        int found=0;
        for(i=0;i<n;i++){
            if(rem[i]>0 && at[i]<=time)
            {
                found=1;
                gantt[g++]=i+1;

                if (rem[i]>tq){
                    time+=tq;
                    rem[i]-=tq;
                }
                else{
                    time+=rem[i];
                    rem[i]=0;
                    ct[i]=time;
                    done++;
                }
            }
        }

        if (found==0)
            time++;
    }

    for(i=0;i<g;i++)
        printf("| P%d ", gantt[i]);
    printf("|\n");

    printf("\nPID\tATime\tBTime\tCTime\tTAT\tWT\n");

    for(i=0;i<n;i++){
        tat[i]=ct[i]-at[i];
        wt[i]=tat[i]-bt[i];
        printf("%d\t%d\t%d\t%d\t%d\t%d\n",i+1,at[i],bt[i],ct[i],tat[i],wt[i]);
    }

        int sumWT=0,sumTAT=0;
        for(i=0;i<n;i++){
            sumWT+=wt[i];
            sumTAT+=tat[i];
        }

        printf("\nAverage Waiting Time=%.2f",
               (float)sumWT/n);
        printf("\nAverage Turnaround Time=%.2f\n",
               (float)sumTAT/n);
}