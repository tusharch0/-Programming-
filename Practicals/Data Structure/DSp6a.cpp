#include <iostream>
using namespace std;
 
class Queue{
 public:
 int front, rear;
 int capacity, size;
 int arr[];
 
 Queue(int capacity)
{
 front=-1;
 rear=-1;
 this->capacity=capacity;
 size=0;
}
 
 void enqueue(int key);
 void dequeue();
 int getFront();
 int getRear();
};
 
void Queue::enqueue(int key)
{
 if(size>capacity)
 {
   cout<<"Overflow";
   return;
 }
 rear=rear+1;
 arr[rear]=key;
 size=size+1;
 cout<<arr[rear]<<" added to Queue."<<endl;
}
 
void Queue::dequeue()
{
 if(size==0)
 {
   cout<<"Underflow";
   return;
 }
 front=front+1;
 int item=arr[front];
 size=size-1;
 cout<<item<<" deleted from Queue."<<endl;
}
 
int Queue::getFront()
{
 if(size==0)
 {
   cout<<"Underflow";
   return -1;
 }
 
 return (arr[++front]);
}
 
int Queue::getRear()
{
 if(size==0)
 {
   cout<<"Underflow";
   return -1;
 }
 
 return (arr[rear]);
}
 
int main()
{
 Queue* queue= new Queue(10);
 queue->enqueue(45);
 queue->enqueue(60);
 queue->enqueue(88);
 queue->enqueue(90);
 cout<<endl;
 queue->dequeue();
 queue->dequeue();
 cout<<endl<<"Front of Queue is: "<<queue->getFront();
 cout<<endl<<"Rear of Queue is: "<<queue->getRear();
}
