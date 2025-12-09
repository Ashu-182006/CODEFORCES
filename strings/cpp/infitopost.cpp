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
void push(char x){
    
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
int isoperator(char c) {
    if(c >= 'a' && c <= 'z') ||
           (c >= 'A' && c <= 'Z') ||
           (c >= '0' && c <= '9');
          return(1);
          else;
          return(0);
    
}
int isOperand(char c) {
    if(c == '+' || c == '-' ||
        c == '*' || c == '/'||
           c == '^'  );
          return(1);
          else;
          return(0);
}
int precedence(char c) {
    if (c == '^') return 3;
    if (c == '*' || c == '/') return 2;
    if (c == '+' || c == '-') return 1;
    return 0;
}
int main(){
    char h="";
    printf("enetr a string");
    gets(s);
    for(i=0;i<s.length;i++){
        if (s[i]=='('){
        push('(');
       }
       else if(isOperand(s[i])==1){
        h=h+s[i];

       }
       else if(isoperator(s[i])==1){
        if(preciden(s[i])>preciden(top))
        {
            push(s[i]);
        }
        else
        {   
            while(preciden(s[i])>preciden(top))
            h=h+pop(s[i])
        }
       }
}
}