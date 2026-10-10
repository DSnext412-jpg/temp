#include<stdio.h>
#include<unistd.h>
#include<sys/wait.h>
#include<stdlib.h>
void main(){
    int a[20],n,i,j,temp,key;
    int pid;

    printf("Enter number of integers: ");
    scanf("%d", &n);

    printf("Enter integers:\n");
    for(i=0;i<n;i++)
        scanf("%d", &a[i]);

    pid=fork();
    if(pid==0){
        for (i=1;i<n;i++){
            key=a[i];
            j=i-1;
            while(j>=0 && a[j]>key){
                a[j+1]=a[j];
                j--;
            }
            a[j+1]=key;
        }

        printf("\nChild: Insertion Sort\n");
        for(i=0;i<n;i++)
            printf("%d ", a[i]);

        printf("\n");
        exit(0);
    }
    else if(pid>0){
        for(i=0;i<n-1;i++){
            for(j=0;j<n-i-1;j++){
                if (a[j]>a[j+1]){
                    temp=a[j];
                    a[j]=a[j+1];
                    a[j+1]=temp;
                }
            }
        }

        printf("\nParent: Bubble Sort\n");
        for (i=0;i<n;i++)
            printf("%d ",a[i]);
        printf("\n");
        wait(NULL);
    }
}