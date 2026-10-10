#include<stdio.h>
#include<unistd.h>
#include<stdlib.h>
void main()
{
    int pid=fork();
    if(pid==0)
    {
        sleep(3);
        printf("Child Process\n");
        printf("Child PID =%d\n",getpid());
        printf("Parent PID =%d\n",getppid());
    }
    else if(pid>0)
    {
        printf("Parent Process\n");
        printf("Parent PID = %d\n",getpid());
        printf("Child PID = %d\n",pid);
        exit(0);
    }
}