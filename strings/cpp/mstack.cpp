#include<stdio.h>
#include<iostream>
#include<stdlib.h>
#define null 0
#define max 100
struct mstack{
    int data[max];
    mstack *next;
    int top;
};
mstack *p,s;
void init(){
    p=&s;
    p->top=-1;

}
void push(){
    int x;
    printf("enter a no.");
    scanf("%d",&x);
    if(p->top==-1)
       return;
    p->top++;
    p->data[p->top]=x;
}
void pop(){
    int x;
    if(empty()==1)
     return;
    x=p->data[p->top];
    top--;
    }
void empty(){
    if(p->top!=-1)
     return (1);
    else
    return (0);
}
'''void print(){
    if(top==null)
        return;
    temp=top;
    printf("they are elements from bottom to top\n");
    while(temp!=null){
        printf("%d\n",temp->data);
        temp=temp->next;
    }'''
    
}
'''int main(){
    int i=0;
    init();
    while(i!=-1)
    {
     printf("what do you want\n");
     printf("1 : push \n 2: pop\n 3: empty \n 4: print the stack\n-1:exit\n");
     scanf("%d",&i);
     switch(i)
     {
       case 1 : push();
                break;
       case 2: pop();
               break;
       case 3 : empty();
                break;
       case 4 : print();
                break;
       case-1: break;

     }
    }
}'''