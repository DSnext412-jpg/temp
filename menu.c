#include <stdio.h>
void main()
{
    int allocation[5][3]={{2,3,2},
                          {4,0,0},
                        {5,0,4},
                        {4,3,3},
                        {2,2,4}};

    int max[5][3]={
        {9,7,5},
        {5,2,2},
        {1,0,4},
        {4,4,4},
        {6,5,5}};

    int need[5][3],available[3],i,j,choice;

    do{
        printf("1.accept available\n");
        printf("2.display allocation and max\n");
        printf("3.display need matrix\n");
        printf("4.display available\n");
        printf("5.exit\n");
        printf("enter your choice: ");
        scanf("%d",&choice);
        switch (choice)
        {
            case 1:
                printf("enter available A B C: ");
                scanf("%d%d%d",&available[0],&available[1],&available[2]);
                break;

            case 2:
                printf("\nPID\tAllocation\tMax\n");
                for(i=0;i<5;i++)
                {
                    printf("P%d\t", i);
                    for(j=0;j<3;j++)
                        printf("%d ",allocation[i][j]);
                    printf("\t\t");
                    for(j=0;j<3;j++)
                        printf("%d ",max[i][j]);
                    printf("\n");
                }
                break;

            case 3:
                printf("\nneed matrix:\n");
                printf("PID\tA\tB\tC\n");
                for(i=0;i<5;i++)
                {
                    printf("P%d\t",i);
                    for(j=0;j<3;j++)
                    {
                        need[i][j]=max[i][j]-allocation[i][j];
                        printf("%d\t",need[i][j]);
                    }
                    printf("\n");
                }
                break;

            case 4:
                printf("\navailable: \n");
                for(j=0;j<3;j++)
                    printf("%d ",available[j]);
                printf("\n");
                break;

            case 5:
                printf("exit\n");
                break;

            default:
                printf("invalid choice\n");
        }
    } while(choice!=5);
}