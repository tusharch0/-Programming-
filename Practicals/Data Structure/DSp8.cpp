#include<iostream> 
using namespace std;
struct node 
{ 
int data; 
struct node *rlink; 
struct node *llink; 
}*tmp=NULL; 

typedef struct node NODE; 
NODE *create(); 
void preorder(NODE *); 
void inorder(NODE *); 
void postorder(NODE *); 
void insert(NODE *); 

int main() 
{ 
int n,i,ch; 
cout<<"1.Create\n2.Insert\n3.Preorder\n4.Postorder\n5.Inorder\n6.Exit\n\n";
do 
{ 
cout<<"Enter Your Choice : ";
cin>>ch; 
switch(ch) 
{ 
case 1: 
tmp=create(); 
break; 
case 2: 
insert(tmp); 
break; 
case 3: 
cout<<"\nDisplay Tree in Preorder Traversal : "; 
preorder(tmp); 
break; 
case 4: 
cout<<"\nDisplay Tree in Postorder Traversal : "; 
postorder(tmp); 
break; 
case 5: 
cout<<"\nDisplay Tree in Inorder Traversal : "; 
inorder(tmp); 
break; 
case 6: 
exit(0); 
default: 
cout<<"\n Inavild Choice.."; 
} 
} 
while(n!=5); 
}
void insert(NODE *root) 
{ 
NODE *newnode; 
if(root==NULL) 
{ 
newnode=create(); 
root=newnode; 
} 
else 
{ 
newnode=create(); 
while(1) 
{ 
if(newnode->data<root->data) 
{ 
if(root->llink==NULL) 
{ 
root->llink=newnode; 
break; 
} 
root=root->llink; 
} 
if(newnode->data>root->data) 
{ 
if(root->rlink==NULL) 
{ 
root->rlink=newnode; 
break; 
} 
root=root->rlink; 
} 
} 
} 
} 
NODE *create() 
{ 
NODE *newnode; 
int n; 
newnode=(NODE *)malloc(sizeof(NODE)); 
cout<<"Enter the Data: "; 
cin>>n; 
newnode->data=n; 
newnode->llink=NULL; 
newnode->rlink=NULL; 
return(newnode); 
} 
void postorder(NODE *tmp) 
{ 
if(tmp!=NULL) 
{ 
postorder(tmp->llink); 
postorder(tmp->rlink); 
cout<<"->"<<tmp->data; 
} 
} 
void inorder(NODE *tmp) 
{  
if(tmp!=NULL) 
{ 
inorder(tmp->llink); 
cout<<"->"<<tmp->data; 
inorder(tmp->rlink); 
} 
} 
void preorder(NODE *tmp) 
{ 
if(tmp!=NULL) 
{ 
cout<<"->"<<tmp->data; 
preorder(tmp->llink); 
preorder(tmp->rlink); 
} 
}
