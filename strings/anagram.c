#include<stdio.h>

#include<string.h>
int main()
{
    int i,n;
    char s[100],s2[100];
    printf("Enter a string: ");
    gets(s);
    printf("Enter a string: ");
    gets(s);
    if(strlen(s)==strlen(s2))
    {
       for(i=0;i<strlen(s);i++)
       {
         if(n==0)
         {
           for(int j=0;j<strlen(s2);j++,n++)
           {
               if(s[i]==s2[j])
               {
                   break;
                   n=0;
               }
           }
              if(n!=0)
              {
                printf("Not anagram");
                break;
              }  
        }  
    } 
}    if(n==0)
    {
        printf("Anagram");
    }      
    else
    {
        printf("Not anagram");
    }
    return(0);
}   

