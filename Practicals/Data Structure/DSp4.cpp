#include <iostream>
using namespace std;
struct node {
    int item;
    node*link;
}*head;

void insertion(int a){
    int i;
if (head ==NULL)
{
   node *temp=new node() ;
   temp->item=a;
   temp->link=head;
   head= temp;
}
else {
        if(head->link==NULL)
            {
              node*temp =new node ;
              temp->item=a;
              temp->link=head->link;
              head->link=temp;
            }
    else
        {
        node *ptr=new node;
        ptr=head;
        for(i=0;ptr->link!=NULL;i++)
        {
            ptr=ptr->link;
        }
        node*temp=new node ;
        temp->item=a;
        temp->link=ptr->link;
        ptr->link=temp;
        }
      }
}

void display(){
    int i;
    node *ptr=new node ;
    ptr=head;
    for(i=0;ptr!=NULL;i++)
    {
        cout<<ptr->item<<" ";
        ptr=ptr->link;
    }
    if (head==NULL)
    {
        cout<<"\nLinked list is empty";
    }
}

void insertionbegin(){
    int a;
    cout<<"Enter the value you want to insert : ";
    cin>>a;
    node *temp=new node ;
    temp->item =a;
    temp->link =head ;
    head =temp;
}
void insertionend(){
     int a,i;
     node *ptr=new node ;
     node *temp=new node ;
     ptr=head;
     cout<<"Enter the value you want to insert : ";
     cin>>a;
     for(i=0;ptr->link!=NULL;i++)
        {
            ptr=ptr->link;
        }
        temp->item=a;
        temp->link=NULL;
        ptr->link=temp;
}
void insertionrandom(){
    int a,pos,i;
    cout<<"Enter the position in which you want to Insert Element : ";
    cin>>pos;
    if(pos==1){
        insertionbegin();
    }
    else{
    cout<<"Enter the Element you want to insert : ";
    cin>>a;
    pos=pos-1;
    node *ptr =new node;
    node *temp= new node;
    ptr =head ;
    for(i=0;i<pos-1;i++){
        ptr =ptr->link;
    }
    temp->item=a;
    temp->link=ptr->link;
    ptr->link=temp;
    }

}
void deletionbegin()
{
head = head->link;
}
void deletionend(){
    int i;
node *temp=new node;
node *ptr=new node ;
ptr=head ;
temp=head->link;
for(i=0;temp->link!=NULL;i++){
    ptr=temp;
    temp=temp->link;
}
ptr->link=NULL;
}
void deletionrandom(){
    int pos,i;
    cout<<"Enter the position of The element you want to delete";
    cin>>pos;
    if(pos==1){
         head =head->link;
    }
    else {
    pos=pos-1;
    node *temp=new node ;
    node *ptr=new node ;
    temp=head;
    for(i=0;i<pos;i++){
        ptr=temp;
        temp=temp->link;
    }
    ptr->link=temp->link;
}
}

int main()
{   int a,i,n,x,y;
  cout<<"Operations on Linked list\n1. Create a linked list\n2. Display linked list\n3. Insertion of New Element \n4. Delete an Existing Element from linked list \n5. Exit";
do{
	cout<<"\nEnter your choice : ";
	cin>>x;
	switch(x){
		case 1:{
    cout<<"Enter the no of element you want to insert ";
    cin>>n;
    for(i=0;i<n;i++)
    {
    cout<<"Enter the no you want to insert ";
    cin>>a;
    insertion (a);
    }
    display();
    cout<<"\n";
		}
		break ;
		case 2:{
			display();
		}
		break;
		case 3:{
		cout<<"1. Insert Element at Beginning\n2. Insert Element at the End\n3. Insert Element at any random position\n";
		cout<<"Enter your Choice : ";
		cin>>y;
		if(y==1)
        {
            insertionbegin();
            display();
        }
        else if (y==2){
            insertionend();
            display();
        }
        else if (y==3){
            insertionrandom();
            display();
        }
        else {
            cout<<"Wrong Choice";
        }
		}
		break;
		case 4:
            {
        cout<<"1. Delete element from Beginning\n2. Delete element from End\n3. Delete element from random position\n";
        cout<<"Enter your Choice : ";
        cin>>y;
        if (y==1){
            deletionbegin();
            display();
        }
        else if (y==2){
            deletionend();
            display();
        }
        else if (y==3){
            deletionrandom();
            display();
        }
        else {
            cout<<"Wrong Choice ";
        }
        }
        break;
		case 5:
		    {
			return(0);
		    }
	}

} while (x!=5);
return 0;

}
