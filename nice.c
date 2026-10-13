#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>

void main()
{
    pid_t pid;
    pid = fork();
    if (pid == 0)
    {
        nice(5);

        printf("Child Process\n");
        printf("Child PID = %d\n", getpid());
        printf("Child priority changed using nice()\n");
    }
    else if (pid > 0)
    {
        wait(NULL);

        printf("Parent Process\n");
        printf("Parent PID = %d\n", getpid());
    }
    else
    {
        printf("Fork failed\n");
    }
}
