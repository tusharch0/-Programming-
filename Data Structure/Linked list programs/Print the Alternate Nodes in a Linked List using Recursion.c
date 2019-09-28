#include <stdio.h>
#include <stdlib.h>

typedef struct list //node structure
{
	int data;
	struct list *next;
}node;

//recursive function
void alternatedisp(node *temp); 

int main(){
	node *head=NULL,*temp,*temp1;
	int choice,count=0,key;

	//Taking the linked list as input
	do
	{
		temp=(node *)malloc(sizeof(node));
		if(temp!=NULL)
		{
			printf("\nEnter the element in the list : ");
			scanf("%d",&temp->data);
			temp->next=NULL;
			if(head==NULL)
			{	
				head=temp;
			}
			else
			{
				temp1=head;
				while(temp1->next!=NULL)
				{
					temp1=temp1->next;
				}
				temp1->next=temp;
			}
		}
		else
		{
			printf("\nMemory not avilable...node allocation is not possible");
		}
		printf("\nIf you wish to add m ore data on the list enter 1 : ");
		scanf("%d",&choice);
	}while(choice==1);
	
	//Now displaying the alternative nodes starting from the begining
	printf("\nDisplaying the alternative items of the list starting from the begining : \n");
	alternatedisp(head);
	printf("NULL\n");
	
	return 0;
}

//recursive function to display alternative nodes
void alternatedisp(node *temp) 
{
	if(temp!=NULL)
	{
		printf("%d->",temp->data);
		if(temp->next==NULL)	
			temp=NULL;
		else
			alternatedisp(temp->next->next);
	}
	else
		return;
}
