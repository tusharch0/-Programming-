#include <bits/stdc++.h>
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

struct node* reverse(node* head, int k){
	if(head==NULL){
		return NULL;
	}
	struct node* next=NULL;
	struct node* prev=NULL;
	struct node* curr=head;
	int count=0;
	while(curr && count<k){
		next=curr->next;
		curr->next=prev;
		prev=curr;
		curr=next;
		count++;
	}
	head->next=reverse(curr,k);
	return prev;
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
    cout<<"Before the reverse operation"<<endl;
    print(l);
    l=reverse(l,2);
    cout<<"\nAfter the reverse operation"<<endl;
    print(l);
    return 0;
}
