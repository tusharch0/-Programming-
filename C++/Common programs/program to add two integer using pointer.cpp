#include <iostream>
using namespace std;
int main()
{
    int *p1=new int ;
    int *p2=new int ;
    int *sum=new int ;
    cout<< "Enter the first no.";
    cin>> (*p1);
    cout<< " Enter the second no.";
    cin>> (*p2);
    *sum =*p1+*p2;
    cout<<"Addition is "<<*sum;
    return 0;
}