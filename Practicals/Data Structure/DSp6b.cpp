#include<iostream>
using namespace std;
 
class Queue
{
 public:
  int rear, front;
  int size;
  int *arr;
 
  Queue(int s)
  {
    front = rear = -1;
    size = s;
    arr = new int[s];
  }
 
  void enQueue(int value);
  int deQueue();
  void displayQueue();
};
 
void Queue::enQueue(int value)
{
  if ((front == 0 && rear == size-1) ||
      (front==rear+1))
  {
    cout<<"\nQueue is Full";
    return;
  }
 
  else if (front == -1)
    front = rear = 0;
 
  else if (rear == size-1 && front != 0)
    rear = 0;
 
  else
    rear++;
    
 arr[rear] = value;
}
 
int Queue::deQueue()
{
  if (front == -1)
  {
    cout<<"\nQueue is Empty";
    return -1;
  }
 
  int data = arr[front];
  arr[front] = -1;
  if (front == rear)
  {
    front = -1;
    rear = -1;
  }
  else if (front == size-1)
    front = 0;
  else
    front++;
 
  return data;
}
 
void Queue::displayQueue()
{
  if (front == -1)
  {
    cout<<"\nQueue is Empty";
    return;
  }
  cout<<"\nElements in Circular Queue are: ";
  if (rear >= front)
  {
    for (int i = front; i <= rear; i++)
      cout<<arr[i]<<" ";
  }
  else
  {
    for (int i = front; i < size; i++)
      cout<<arr[i]<<" ";
 
    for (int i = 0; i <= rear; i++)
      cout<<arr[i]<<" ";
  }
}
 
int main()
{
  Queue q(5);
  q.enQueue(14);
  q.enQueue(22);
  q.enQueue(13);
  q.enQueue(48);
 
  q.displayQueue();
 
  cout<<"\nDeleted value = "<<q.deQueue();
  cout<<"\nDeleted value = "<<q.deQueue();
 
  q.displayQueue();
 
  q.enQueue(9);
  q.enQueue(20);
  q.enQueue(5);
 
  q.displayQueue();
 
  q.enQueue(20); 
}
