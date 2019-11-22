#include<iostream>
using namespace std;
int main(){
    int a[20],i,j,n,items,k,x;
    int position,f;
    cout<<"Enter the no. of elements"<<endl;
    cin>>n;
    cout<<"Enter the elements in the array"<<endl;
    for(i=0;i<n;i++)
    cin>>a[i];
    cout<<endl;

		cout<<"Enter your choice, which operations you want to operate ?"<<endl;
    cout<<" 1: Inserting element"<<endl;
    cout<<" 2: Deleting element"<<endl;
    cout<<" 3: Finding location of element"<<endl;
    cout<<" 4: Displaying element"<<endl;
    cout<<" 5: Exit";
    do{
			cout<<endl;
			cout<<"\nEnter your choice ";
    cin>>x;
     cout<<endl;
    switch(x){

    case 1:
    cout<<"Enter the element you want to inserts"<<endl;
    cin>>items;
    cout<<"Enter the location where you want to input"<<endl;
    cin>>k;
    for(i=n-1;i>=k;i--)
    {
        a[i+1]=a[i];
    }
    a[k]=items;
    cout<<"After insertion of elements:"<<endl;
    for(i=0;i<=n;i++)
    cout<<a[i]<<" ";
    break;
  
    case 2:
    cout<<"Enter the location where you want to delete"<<endl;
    cin>>k;
    for(i=k;i<n;i++)
    {
        a[i]=a[i+1];
    }
    cout<<"After deletion of elements: "<<endl;
    for(i=0;i<=n-2;i++)
    cout<<a[i]<<" ";

    break;

    case 3:
    cout<<"Enter the element that you want to search"<<endl;
    cin>>items;
   for(i=0;i<n;i++)
   {
    if(a[i]==items)
    {
        position=i;
        f=1;
        break;
    }
   }

if(f==1)
cout<<"Item is in the position of "<<position+1;
else
  cout<<"Item not found"<<endl;
  break;

 case 4:
     cout<<"Elements are: ";
    for(i=0;i<n;i++)
    cout<<endl<<a[i];
		cout<<" ";
    break;
 case 5:
    exit(0);
}
}
while(x!=5);
}
