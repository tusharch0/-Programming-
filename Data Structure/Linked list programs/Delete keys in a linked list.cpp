#include <iostream>
using namespace std;

struct node{
    int data;
    node* next;
};

struct node* create_node(int x){
    struct node* temp= new node;
    temp->data=x;
    temp->next=NULL;
    return temp;
}

void push(node** head,int x){
    struct node* store=create_node(x);
    if(*head==NULL){
        *head =store;
        return;
    }
    struct node* temp=*head;
    while(temp->next){
        temp=temp->next;
    }
    temp->next=store;
}

void delete_node(node** head,int x){
    if((*head)->next==NULL){
        *head=NULL;
        return;
    }
    struct node* temp=*head;
    if(temp->data==x){
    	temp=temp->next;
    	*head=temp;
    	return;
    }
    while(temp){
    	if(temp->data==x){
    		temp->data=temp->next->data;
    		temp->next=temp->next->next;
    		break;
    	}
    	temp=temp->next;
    }
}

void print(node* head){
	struct node* temp=head;
	while(temp){
		cout<<temp->data<<" ";
		temp=temp->next;
	}
}

int main()
{
    struct node* l=NULL;
    push(&l,1);
    push(&l,2);
    push(&l,3);
    push(&l,4);
    push(&l,5);
    push(&l,6);
    cout<<"Before the delete operation"<<endl;
    print(l);
    delete_node(&l,2);
    cout<<"\nAfter the delete operation"<<endl;
    print(l);
	
    return 0;
}
