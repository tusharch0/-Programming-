#include <iostream>
using namespace std;
int sum(int a,int b);
int main()
{
    int a,b,add;
    cout<< "Enter the first no. ";
    cin>> a;
    cout<< "Enter the second no. ";
    cin>> b;
    add= sum(a,b);
    cout<<"Adition is "<<add;
    return 0;
}
int sum(int a ,int b)
{
    return (a+b);
}