#include <iostream>
using namespace std;
int prime (int n);
int main()
{
    int i,n;
    cout<< "Enter max limit ";
    cin>>n;
    cout<< "Prime number ";
    for (i=2;i<n;i++)
    {
        if(prime(i))
        cout<<i<<" ";
    }
    cout<<endl;
    return 0;
}
int prime (int n)
{
    int i,prime =1;
    for (i=2;i<(n/2);i++)
    {
        if(n%i==0)
        {
            prime =0;
            break;
        }   
    }
    return 0;
}