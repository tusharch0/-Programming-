#include <stdio.h>
#define MAX 10
 
int QUEUE[MAX],front=-1,rear=-1;
 
void insert_in_Q(int queue[],int ele)
{
    if(rear==-1)
    {
        front=rear=0;
        queue[rear]=ele;
    }
    else if(rear==MAX-1)
    {
        printf("\nQUEUE is full.\n");
        return;
    }
    else
    {
        rear++;
        queue[rear]=ele;
    }
    printf("\nItem inserted..");
}
 
 
void display_Q(int queue[])
{       int i;
    if(rear==-1) { printf("\nQUEUE is Empty."); return; }
    for(i=front;i<=rear;i++)
    { printf("%d,",queue[i]); }
 
}

void remove_from_Q(int queue[])
{
    int ele;
    if(front==-1)
    {
        printf("QUEUE is Empty.");
        return;
    }
    else if(front==rear)
    {
        ele=queue[front];
        front=rear=-1;
    }
    else
    {
        ele=queue[front];
        front++;
    }
    printf("\nItem removed : %d.",ele);
}
 
int main()
{
    int ele,choice;
while(1)
{
    printf("\nQUEUE Elements are :");
    display_Q(QUEUE);
    printf("\n\nEnter choice (1:Insert,2:Display,3:Remove,0:Exit):");
    scanf("%d",&choice);
    switch(choice)
    {
        case 0:
            exit(1);
            break;
        case 1:
            printf("Enter an element to insert:");
            scanf("%d",&ele);
            insert_in_Q(QUEUE,ele);
            break;
        case 2:
            display_Q(QUEUE);
            break;
        case 3:
            remove_from_Q(QUEUE);
            break;
        default:
            printf("\nInvalid choice\n");
            break;
    }
 
} 
return 0;
}
