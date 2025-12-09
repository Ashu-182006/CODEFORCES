#include<stdio.h>
int main()
{ printf("Frequency of elements in an array:\n");
    int a[11]={0,1,2,3,4,4,4,5,6,3,4};
    int j=0;
    while (j<7)
    {
        int k=0;
        for(int i=0;i<10;i++)
        {
             if(a[i]==j)
             {
                 k++;
             }
             if(i==10)
                {
                    printf("The frequency of %d is %d\n",j,k);
                    j=j+1;
                }
        }
    }
    
}