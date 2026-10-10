#include<stdio.h>
#include<stdlib.h>
void main(){
    int n,i,choice,size,block;
    int bit[100], next[100];
    char name[20][20];
    int start[20],end[20],files=0;

    printf("Enter number of disk blocks: ");
    scanf("%d",&n);

    for(i=0;i<n;i++){
        bit[i]=rand()%2;
        next[i]=-1;
    }

    do{
        printf("1.Show Bit Vector\n");
        printf("2.Create New File\n");
        printf("3.Show Directory\n");
        printf("4.Exit\n");
        printf("Enter choice: ");
        scanf("%d", &choice);
        switch(choice){
            case 1:
                printf("\nBit Vector:\n");
                for(i=0;i<n;i++)
                    printf("%d ", bit[i]);
                printf("\n");
                break;

            case 2:
                if(files==20){
                    printf("Directory is full!\n");
                    break;
                }

                printf("Enter file name: ");
                scanf("%19s",name[files]);

                printf("Enter number of blocks required: ");
                scanf("%d", &size);

                if(size<=0||size>n){
                    printf("Invalid file size!\n");
                    break;
                }
                int freeCount = 0;
                for (i = 0; i < n; i++)
                    if (bit[i] == 0)
                        freeCount++;

                if (freeCount < size){
                    printf("Not enough free blocks!\n");
                    break;
                }

                start[files]=-1;
                end[files]=-1;

                for(i=0;i<size;i++){
                    do{
                        block=rand()%n;
                    }
                    while (bit[block]==1);
                    bit[block]=1;
                    if (start[files]==-1)
                        start[files]=block;
                    else
                        next[end[files]]=block;
                    end[files]=block;
                }

                files++;
                printf("File created successfully!\n");
                break;

            case 3:
                printf("\nFile Name\tStart\tBlock Chain\n");
                for(i=0;i<files;i++){
                    int current = start[i];
                    printf("%s\t\t%d\t", name[i],current);
                    while(current!=-1){
                        printf("%d",current);
                        if (current==end[i])
                            break;
                        printf(" -> ");
                        current=next[current];
                    }
                    printf(" -> NULL\n");
                }
                break;
            case 4:
                printf("Exiting program...\n");
                break;
            default:
                printf("Invalid choice!\n");
        }
    } while(choice!=4);
}