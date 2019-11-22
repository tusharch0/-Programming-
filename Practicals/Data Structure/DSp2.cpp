#include<iostream>
using namespace std;
int main(){
    int a[20],n,x,i,flag=0,num,first, last, middle;
    cout<<"Enter the no. of elements"<<endl;
    cin>>n;
    cout<<"Enter the elements in the array"<<endl;
    for(i=0;i<n;i++)
    cin>>a[i];
    cout<<endl;

		cout<<"Enter your choice, which operations you want to operate ?"<<endl;
    cout<<" 1: Linear search"<<endl;
    cout<<" 2: Binary search"<<endl;
    cout<<" 3: exit";
    do{
			cout<<endl;
			cout<<"\nEnter your choice: ";
    cin>>x;
     cout<<endl;
    switch(x){

    case 1:
    cout<<"Enter the number that you want to search: ";
	cin>>num;
	
	for(i=0;i<n;++i)
	{
		if(a[i]==num)
		{
			flag=1;
			break;
		}
	}
	
	if(flag)
		cout<<"Element is found at position "<<i+1;
	else
		cout<<"Element not found";
    break;
  
    case 2:
    cout<<"Enter the number that you want to search: ";
        cin>>num;
first = 0;
last = n-1;
middle = (first+last)/2;
while (first <= last)
{
  if(a[middle] < num)
  {
first = middle + 1;

  }
  else if(a[middle] == num)
  {
cout<<"Element is found at position "<<middle+1<<"\n";
                break;
           }
           else {
                last = middle - 1;
           }
           middle = (first + last)/2;
        }
        if(first > last)
{
  cout<<num<<"Element not found";
}
    break;

 case 3:
    exit(0);
}
}
while(x!=3);
}
