#include <stdio.h>
#include <stdlib.h>

struct node{
	int data; 
	struct node *next;
};

void display(struct node* head){
	struct node* current=head; 
	
	printf("traversing the list...\n");
	while(current!=NULL){ 
		printf("%d ",current->data);
		current=current->next;		
	}	
}

struct node* reverse_N(struct node* head,struct node* temp,int n){
	struct node *next=NULL,*cur=head,*prev=temp; 
	int count=0;
	while(cur!=NULL && (count++)<n){
		next=cur->next;
		cur->next=prev;
		prev=cur; 
		cur=next;
	}
    
	head=prev; 
	return head;
}

struct node* creatnode(int d){
	struct node* temp=malloc(sizeof(struct node));
	temp->data=d;
	temp->next=NULL;
	return temp;
}

int main(){
	printf("creating the linked list by inserting new nodes at the end\n");
	
	printf("enter 0 to stop building the list, else enter any integer\n");
	
	int k,count=0,x=1,n;
	
	struct node* curr,*temp;
	
	scanf("%d",&k);
	struct node* head=creatnode(k); 
	scanf("%d",&k);
	temp=head;
	while(k){
	curr=creatnode(k);
	temp->next=curr;
	temp=temp->next;
	x++;
	scanf("%d",&k);
	}
	display(head); 
	printf("\nInput N\n");
	while(1){
		scanf("%d",&n);
		if(n<x)
		break;
		printf("N greater than no of element, enter again\n");
	}
	
	printf("\nreversing upto first N elements...\n");
	
	
	temp=head;
	while((count++)<n){
		temp=temp->next;
	}
	
	head=reverse_N(head,temp,n);
	display(head); 
	
	return 0;
}
