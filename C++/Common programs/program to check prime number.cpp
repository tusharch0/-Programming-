#include <iostream>
using namespace std;
int prime (int n);
int main()
{
    int n;
    cout<< "Enter a number: ";
    cin>>n;
    if(prime(n))
    cout<<n<<" is a prime number ";
    else 
    cout<<n<<" is not a prime number";
    return 0;
}
int prime (int n)
{
    int i,prime =1;
    for (i=2;i<(n/2);i++)
    {
        if (n%i==0)
        {
            prime=0;
            break;
        }
    }
    return prime ;
}