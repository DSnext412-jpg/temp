#include<stdio.h>
#include<unistd.h>
#include<sys/wait.h>
#include<sys/resource.h>

void main(){
    int pid=fork();
    if (pid==0){
        nice(-5);
        printf("Child Process\n");
        printf("Child PID=%d\n",getpid());
        printf("Nice value=%d\n",getpriority(PRIO_PROCESS,0));
    }
    else{
        wait(NULL);
        printf("Parent Process\n");
        printf("Parent PID=%d\n",getpid());
    }
}