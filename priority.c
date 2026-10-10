#include<stdio.h>
#include<stdlib.h>
void main(){
    int n,i,time=0,done=0;
    int at[10],bt[10],rem[10],pr[10];
    int ct[10],tat[10],wt[10];
    int gantt[100],start[100],end[100];
    int count=0,p,high;
    float avgWT=0,avgTAT=0;

    printf("Enter No. of Processes: ");
    scanf("%d", &n);

    printf("\nPID\tATime\tBTime\tPriority\n");

    for(i=0;i<n;i++){
        printf("%d\t",i+1);
        scanf("%d%d%d",&at[i],&bt[i],&pr[i]);

        bt[i]+=rand()%5+1;
        rem[i]=bt[i];
    }

    while(done<n){
        p=-1;
        high=9999;
        for(i=0;i<n;i++){
            if (at[i] <= time && rem[i] > 0 && pr[i] < high)
            {
                high = pr[i];
                p = i;
            }
        }

        if(p ==-1){
            time++;
            continue;
        }

        if(count==0 || gantt[count - 1] != p){
            gantt[count] = p;
            start[count] = time;
            count++;
        }

        rem[p]--;
        time++;
        end[count - 1] = time;

        if (rem[p] ==0){
            ct[p] = time;
            done++;
        }
    }

    printf("\nGantt Chart:\n");
    for(i=0;i<count;i++)
        printf("| P%d ", gantt[i] + 1);
    printf("|\n");

    printf("%d", start[0]);
    for(i=0;i<count;i++)
        printf("\t%d", end[i]);

    printf("\n\nPID\tATime\tBTime\tPriority\tCTime\tTAT\tWT\n");

    for(i=0; i<n; i++){
        tat[i]=ct[i]-at[i];
        wt[i]=tat[i]-bt[i];
        avgWT+=wt[i];
        avgTAT+=tat[i];
        printf("%d\t%d\t%d\t%d\t\t%d\t%d\t%d\n",i+1,at[i], bt[i],pr[i],ct[i],tat[i], wt[i]);
    }
    printf("\nAverage Waiting Time =%.2f", avgWT/n);
    printf("\nAverage Turnaround Time =%.2f\n",avgTAT/n);
}