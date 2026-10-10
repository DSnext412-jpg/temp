#include<stdio.h> 
#include<string.h> 
#include<stdlib.h>

char comm[80],*args[5]; 
void get_comm() { 
    int len; 
    fgets(comm,80,stdin); 
    len=strlen(comm); 
    comm[len-1]='\0'; 
} 
void sep_args() { 
    int i=0; 
    char *p; p = strtok(comm," "); 
    while(p!=NULL) { 
        args[i]=p; i++; 
        p=strtok(NULL," "); 
    } 
    args[i]=NULL; 
} 
void count(char op,char fname[]) { 
    int tot_chars=0,words=0,lines=0; 
    char ch; FILE *fp;  
    fp = fopen(fname,"r"); 
    if(fp==NULL) { 
        printf("\n File not found"); 
    } else {
        while(ch!=EOF) { 
            ch = fgetc(fp); 
            tot_chars++; 
            if(ch==' ' || ch=='\t') { 
                words++; 
            }    
            else if(ch=='\n'){     
                lines++;     
                words++;    
            }   
        }        
        fclose(fp);      
        if(op=='l'){    
            printf("\n Total Lines are : %d",lines);   
        }   
        else if(op=='w'){    
            printf("\n Total words are : %d",words);   
        }   
        else if(op=='c'){    
            printf("\n Total Characters are : %d",tot_chars);   
        }   
        else{    
            printf("\n Invalid Option");   
        }  
    } 
}  
void take_action(){  
    if(strcmp(args[0],"count")==0){   
        count(args[1][0],args[2]);  
    }  
    else if(strcmp(args[0],"quit")==0){   
        exit(0);  
    }  
    else{   
        printf("\n %s: Command not found",args[0]);  
    } 
}  

void main() 
{  
    while(1){   
        printf("\n myshell$ ");
        get_comm();   
        sep_args();   
        take_action();  
    }   
} 