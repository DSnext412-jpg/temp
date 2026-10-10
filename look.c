#include<stdio.h>
#include<stdlib.h>
void main(){
    int req[20], n, blocks, head, i, j, temp;
    int total = 0, pos;

    printf("Enter total number of disk blocks: ");
    scanf("%d", &blocks);

    printf("Enter number of requests: ");
    scanf("%d", &n);

    printf("Enter disk request string:\n");
    for (i = 0; i < n; i++)
        scanf("%d", &req[i]);

    printf("Enter starting head position: ");
    scanf("%d", &head);

    char dir[10];
    printf("Enter direction (Left/Right): ");
    scanf("%s", dir);

    for(i=0;i<n-1;i++)
    {
        for (j = i + 1; j < n; j++)
        {
            if (req[i] > req[j])
            {
                temp = req[i];
                req[i] = req[j];
                req[j] = temp;
            }
        }
    }

    // Find first request greater than or equal to head
    for (i = 0; i < n; i++)
    {
        if (req[i] >= head)
            break;
    }
    pos = i;

    printf("\nRequest service order: %d", head);

    if (dir[0] == 'L' || dir[0] == 'l')
    {
        for (i = pos - 1; i >= 0; i--)
        {
            printf(" -> %d", req[i]);
            total += abs(head - req[i]);
            head = req[i];
        }

        for (i = pos; i < n; i++)
        {
            printf(" -> %d", req[i]);
            total += abs(head - req[i]);
            head = req[i];
        }
    }
    else
    {
        for (i = pos; i < n; i++)
        {
            printf(" -> %d", req[i]);
            total += abs(head - req[i]);
            head = req[i];
        }

        for (i = pos - 1; i >= 0; i--)
        {
            printf(" -> %d", req[i]);
            total += abs(head - req[i]);
            head = req[i];
        }
    }

    printf("\nTotal head movement = %d\n", total);
}