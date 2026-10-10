#include<stdio.h>
void main(){
    int pages[50],frames[10],counter[10];
    int n,f,i,j,found,pos,faults=0,time=0;

    printf("Enter number of pages: ");
    scanf("%d", &n);

    printf("Enter reference string:\n");
    for(i=0;i<n;i++)
        scanf("%d",&pages[i]);

    printf("Enter number of frames: ");
    scanf("%d",&f);

    for(i=0;i<f;i++){
        frames[i]=-1;
        counter[i]=0;
    }

    printf("\nPage\tFrames\t\tpage fault\n");

    for(i=0;i<n;i++){
        time++;
        found=0;

        for(j=0;j<f;j++){
            if (frames[j]==pages[i]){
                counter[j]=time;
                found=1;
                break;
            }
        }

        if(found==0){
            faults++;
            pos=-1;

            for(j=0;j<f;j++){
                if(frames[j]==-1){
                    pos=j;
                    break;
                }
            }

            if(pos==-1){
                pos=0;
                for(j=1;j<f;j++){
                    if (counter[j]<counter[pos])
                        pos=j;
                }
            }

            frames[pos]=pages[i];
            counter[pos]=time;
        }

        printf("%d\t", pages[i]);

        for(j=0;j<f;j++){
            if (frames[j]==-1)
                printf("  ");
            else
                printf("%d|",frames[j]);
        }
        printf("\t");

        if (found==1)
            printf("\tN\n");
        else
            printf("\tY\n");
    }

    printf("\nTotal Number of Page Faults =%d\n",faults);
}