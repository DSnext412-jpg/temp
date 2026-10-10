#include<stdio.h>
void main(){
    int pages[50],frames[10],freq[10];
    int n,f,i,j,k,found,faults=0;
    int min,pos;

    printf("Enter number of pages: ");
    scanf("%d",&n);

    printf("Enter reference string:\n");
    for (i=0;i<n;i++)
        scanf("%d",&pages[i]);

    printf("Enter number of frames: ");
    scanf("%d",&f);

    for(i=0;i<f;i++){
        frames[i]=-1;
        freq[i]=0;
    }

    printf("\nPage\tFrames\t\tpage fault\n");
    for(i=0;i<n;i++){
        found=0;
        for(j=0;j<f;j++){
            if (frames[j]==pages[i]){
                found=1;
                freq[j]++;
                break;
            }
        }

        if(found==0){
            faults++;
            pos=-1;
            min=-1;

            for(j=0;j<f;j++){
                if (frames[j]==-1){
                    pos=j;
                    break;
                }
                if (freq[j]>min){
                    min=freq[j];
                    pos=j;
                }
            }

            frames[pos]=pages[i];
            freq[pos]=1;
        }
        printf("%d\t", pages[i]);
        for(k=0;k<f;k++){
            if (frames[k]==-1)
                printf("  ");
            else
                printf("%d|",frames[k]);
        }

        if(found==1)
            printf("\tN\n");
        else
            printf("\tY\n");
    }
    printf("\ntotal page faults=%d\n",faults);
}
