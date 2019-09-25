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


void reverse_display(struct node* head){
	if(head){
		reverse_display(head->next);
		printf("%d ",head->data);
	}
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

	int k,count=1,x;

	struct node* curr,*temp;

	scanf("%d",&k);
	struct node* head=creatnode(k); 
	scanf("%d",&k);
	temp=head;

	while(k){
		curr=creatnode(k);
		temp->next=curr;
		temp=temp->next;
		scanf("%d",&k);
	}
	
	display(head); 
	printf("\ndisplaying in reverse order...\n");
	reverse_display(head);
	return 0;
}
