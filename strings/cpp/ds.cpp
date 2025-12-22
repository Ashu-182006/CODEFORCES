#include<stdio.h>
#include<conio.h>
#include<graphics.h>
#include<dos.h>
#include<stdlib.h>

struct bst
{
  int data;
  bst *left,*right;
};
bst *root ,*temp,*ttemp,*p,*q;
void createroot()
{
  int x;
  root =new bst;
  printf("enter no.");
  scanf("%d",&x);
  root ->data=x;
  root->left=root->right=NULL;
}
void addroot()
{
  int x;
  printf("enter a no");
  scanf("%d",&x);
  temp=root;
  while(temp!=NULL)
  {
    ttemp=temp;
    if(temp->data>x)
    {
      temp=temp->left ;
    }
    else
    temp=temp->right;
  }
  p=new bst ;
  p->data=x;
  p->left=p->right=NULL;
  if(ttemp->data>x)
  ttemp->left=p;
  else
  ttemp->right=p;
}
bst* lr(bst* p)
{
   bst* q=p->right;
   bst* temp=q->left;
   q->left=p;
   p->right=temp;
   return q;
}
bst* rr(bst* p)
{
   bst* q=p->left;
   bst* temp=q->right;
   q->right=p;
   p->left=temp;
   return q;
}


bst* defoliation(bst *p)

{
  if(p!=NULL)
  {
   if(p->left==NULL&&p->right==NULL)
   {
      delete p;
      return NULL;
   }
   else
   {
   p->left= defoliation(p->left);
   p->right= defoliation(p->right);
    return p;
   }}
   return NULL;


}
void in(bst *p)
{
  if(p!=NULL)
  {
    in(p->left)  ;
    delay(100);
    printf("%d   ",p->data);
    in(p->right);
  }
}
void post(bst *p)
{
  if(p!=NULL)
  {
    post(p->left);
    post(p->right);
     delay(110) ;
    printf("%d   ",p->data);
  }

}
void pre(bst *p)
{
    if(p!=NULL)
  { delay(100);
    printf("%d   ",p->data);
    pre(p->left)          ;
    pre(p->right)       ;

  }

}
void tree(bst* node,int x,int y,int o)
{
 if( node==NULL)
 return ;
 delay(100);
  circle(x,y,20);
  char s[10];
  delay(200);
  sprintf(s,"%d",node->data);
  outtextxy(x-10,y-5,s);
  if(node->left)
  { delay(100);
    line(x,y+20,x-o,y+50);
    tree(node->left,x-o,y+70,o/2);
  }
  if(node->right)
  {  delay(100);
     line(x,y+20,x+o,y+50);
    tree(node->right,x+o,y+70,o/2);
  }
}
bst* search(bst* root,int k)
{
  if(root==NULL|| root->data==k)
  {
    return root;
  }
  if(k<root->data)
     return search(root->left,k);
  return search(root->right,k);
}
bst* nnode(bst* root,bst* c)
{
  if(root==NULL||root==c)
  return NULL;
  if(root->left==c||root->right==c)
  return root;
  if(c->data<root->data)
  return nnode(root->left,c)  ;
  else
  return nnode(root->right,c);
}


int main()
{
/*int gdriver = DETECT,gmode;
int x,y,i;
	initgraph(&gdriver,&gmode,"C:\\Turboc3\\BGI");
	x=getmaxx()/2;
	y=getmaxy()/2;
	for(i=30;i<200;i++)
	{
		delay(50);
		setcolor(i/10);
		arc(x,y,0,180,i-10);*/
int i;
clrscr();
while(i!=0)
{ delay(100);
  printf("\nchoose what to do\n");
  delay(120);
  printf("\n-1:draw the tree\n 1:create a root\n2: add aroot\n3:print pre order\n4:print in order\n5:print post order\n6:defoliation\n7:left rotation\n8:right rotation\n0:exit");
  scanf("%d",&i);
  switch (i)
  {
   case 1: createroot();
	  break;
   case 2:addroot();
	  break;
   case 3:pre(root);
	  break;
   case 4:in(root);
	  break;
   case 5:post(root);
	  break;
   case 6:defoliation(root);
	  break;
   case 7:{
	  int k;
	  printf("enter in tree");
	  scanf("%d",&k);
	  bst* p=search(root,k);
	  if(p!=NULL&&p->right!=NULL)
	  {
	    bst* newr=lr(p);
	    bst* node=nnode(root,p);
	    if(node==NULL)
	      root=newr;
	    else
	    {
	      if(node->left==p)
		node->left=newr;
	      else
	       node->right=newr;
	    }
	  }     else
	    printf("not posssiblr");

	  break;
	  }
    case 8:
	  {
	  int k;
	  printf("enter in tree");
	  scanf("%d",&k);
	  bst* p=search(root,k);
	  if(p!=NULL&&p->right!=NULL)
	  {
	    bst* newr=rr(p);
	    bst* node=nnode(root,p);
	    if(node==NULL)
	      root=newr;
	    else
	    {
	      if(node->left==p)
		node->left=newr;
	      else
	       node->right=newr;
	    }

	  }    else
	    printf("not posssiblr");

	  break;
	  }
   case -1:int gdriver = DETECT,gmode;
	   initgraph(&gdriver,&gmode,"C:\\Turboc3\\BGI");
	   cleardevice();
	   tree(root,320,50,120);
	   getch();
	   closegraph();
	   break;
  }

}

return 0;
}