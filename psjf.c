#include<stdio.h>
#include<stdlib.h>
void main(){
    int n, i, time = 0, count = 0, p, completed = 0;
    int at[20], bt[20], rem[20],ct[20], tat[20], wt[20];
    int gantt[200], start[200],end[200];
    int totalWT = 0, totalTAT=0;

    printf("Enter No. of Processes: ");
    scanf("%d", &n);

    printf("\nPID\tATime\tBTime\n");

    for (i = 0; i < n; i++)
    {
        printf("%d\t", i + 1);
        scanf("%d%d", &at[i], &bt[i]);
    }

    for (i = 0; i < n; i++)
    {
        bt[i] += rand() % 5 + 1;
        rem[i] = bt[i];
    }

    printf("\nGantt Chart:\n");

    while(completed<n)
    {
        p = -1;

        for (i = 0; i < n; i++)
        {
            if (at[i] <= time && rem[i] > 0)
            {
                if (p == -1 || rem[i] < rem[p])
                    p = i;
            }
        }

        if (p == -1)
        {
            time++;
            continue;
        }

        if (count == 0 || gantt[count - 1] != p)
        {
            gantt[count] = p;
            start[count] = time;
            count++;
        }

        rem[p]--;
        time++;
        end[count - 1] = time;

        if (rem[p] == 0){
            ct[p]=time;
            completed++;
        }
    }

    for (i = 0; i < count; i++)
        printf("| P%d ", gantt[i] + 1);
    printf("|\n");

    printf("%d", start[0]);
    for (i = 0; i < count; i++)
        printf("\t%d", end[i]);

    printf("\n\nPID\tATime\tBTime\tCTime\tTAT\tWT\n");

    for (i = 0; i < n; i++)
    {
        tat[i] = ct[i] - at[i];
        wt[i] = tat[i] - bt[i];

        printf("%d\t%d\t%d\t%d\t%d\t%d\n",
               i + 1, at[i], bt[i], ct[i], tat[i], wt[i]);

        totalWT += wt[i];
        totalTAT += tat[i];
    }

    printf("\nAverage Waiting Time = %.2f",
           (float)totalWT / n);

    printf("\nAverage Turnaround Time = %.2f\n",
           (float)totalTAT/n);
}