#include<stdio.h>

#include<string.h>
int main()
{
    int i,n;
    char s[100],s2[100],s3[100];
    printf("Enter a string: ");
    gets(s);
    printf("Enter a string: ");
    gets(s);
    if(strlen(s)==strlen(s2))
    {
        for(i=0;i<strlen(s);i++)
    
    {
        s3[i]=s[i];
    }
    for(i=0;i<strlen(s2);i++)
    
    {
        s3[i+strlen(s)]=s2[i];
    }
    if(strstr(s3,s2)!=NULL)
     printf("Rotation");
     else
     printf("no");
      return(0);
    }
}   

