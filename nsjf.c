#include<stdio.h>

void main(){
    int n, i, time = 0, count = 0, p;
    int at[20],bt[20],ct[20],tat[20], wt[20];
    int done[20] = {0};
    int totalWT=0,totalTAT=0,gantt_p[20], gantt_time[21],g_count=0;

    printf("enter no. of Processes: ");
    scanf("%d",&n);

    printf("\nPID\tATime\tBTime\n");
    for(i=0;i<n;i++){
        printf("%d\t",i+1);
        scanf("%d%d",&at[i],&bt[i]);
    }
    printf("\ngantt chart:\n");
    gantt_time[0]=time;

    while(count<n){
        p=-1;
        for(i=0;i<n;i++) {
            if (!done[i] && at[i] <= time) {
                if (p==-1||bt[i]<bt[p])
                    p=i;
            }
        }
        
        if(p==-1){
            time++;
            gantt_time[g_count+1]=time;
            continue;
        }

        gantt_p[g_count]=p+1;
        
        time+=bt[p];
        gantt_time[g_count+1]=time;
        g_count++;

        ct[p]=time;
        tat[p]=ct[p]-at[p];
        wt[p]=tat[p]-bt[p];

        done[p] = 1;
        count++;
    }

    for(i=0; i<g_count;i++) {
        printf("| P%d ",gantt_p[i]);
    }
    printf("|\n");
    for(i=0;i<=g_count;i++) {
        printf("%d    ",gantt_time[i]);
    }
    
    printf("\n\nPID\tATime\tBTime\tCTime\tTAT\tWT\n");
    for(i = 0; i < n; i++){
        printf("%d\t%d\t%d\t%d\t%d\t%d\n", i + 1, at[i], bt[i], ct[i], tat[i], wt[i]);
        totalWT += wt[i];
        totalTAT += tat[i];
    }

    printf("\naverage waiting time = %.2f", (float)totalWT / n);
    printf("\naverage turnaround time = %.2f\n", (float)totalTAT / n);
}
