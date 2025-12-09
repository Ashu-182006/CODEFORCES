#include<stdio.h>
#include<iostream>
#include<stdlib.h>
#define null 0
struct lstack{
    int data;
    lstack *next;
};
lstack *top,*temp;
void init(){
    top=temp=null;

}
void push(){
    int x;
    printf("enter a no.");
    scanf("%d",&x);
    temp=new lstack;
    if(temp==null)
       return;
    temp->data=x;
    temp->next=top;
    top=temp;
}
void pop(){
    int x;
    if(top==null)
     return;
    temp =top;
    top=top->next;
    x=temp->data;
    temp->next=null;
    delete temp;
    printf("%d\n",x);
}
void empty(){
    while(top!=null)
    {
        pop();
    }
}
void print(){
    if(top==null)
        return;
    temp=top;
    printf("they are elements from bottom to top\n");
    while(temp!=null){
        printf("%d\n",temp->data);
        temp=temp->next;
    }
    
}
int main(){
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
}