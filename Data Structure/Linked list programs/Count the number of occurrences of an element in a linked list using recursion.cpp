#include <stdio.h>
#include <stdlib.h>

typedef struct list //linked list structure
{
	int data;
	struct list *next;
}node;

int key,c=0;
int occurence(node *temp); 

int main()
{
	node *head=NULL,*temp,*temp1;
	int choice,count;

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
		printf("\nIf you wish to add more data on the list enter 1 : ");
		scanf("%d",&choice);
	}while(choice==1);
	
	printf("\nEnter the data to find it's occurrence : ");
	scanf("%d",&key);
	count =occurence(head);
	printf("%d occured %d times in the list",key,count);
	
	return 0;
}

int occurence(node *temp) 
{
	if(temp==NULL)
		return c;
	else
	{
		if(temp->data==key)
			c=c+1;
		occurence(temp->next);
	}
}
