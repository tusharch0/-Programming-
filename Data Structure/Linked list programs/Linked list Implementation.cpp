#include <iostream>
using namespace std;
 
struct Node{
    int num;
    Node *next;
};
 
struct Node *head=NULL;
 
void insertNode(int n){
    struct Node *newNode=new Node;
    newNode->num=n;
    newNode->next=head;
    head=newNode;
}
 
void display(){
    if(head==NULL)
    {
        cout<<"List is empty!"<<endl;
        return;
    }
    struct Node *temp=head;
    while(temp!=NULL)
    {
        cout<<temp->num<<" ";
        temp=temp->next;
    }
    cout<<endl;
} 

void deleteItem()
{
    if(head==NULL)
    {
        cout<<"List is empty!"<<endl;
        return;
    }
    cout<<head->num<<" is removed."<<endl;
    head=head->next;
}
int main()
{
    display();
    insertNode(10);
    insertNode(20);
    insertNode(30);
    insertNode(40);
    insertNode(50);
    display();
    deleteItem(); 
    deleteItem(); 
    deleteItem(); 
    deleteItem(); 
    deleteItem();
    deleteItem();
    display();
    return 0;
}
