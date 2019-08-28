#include <iostream>
using namespace std ;
int main()
{
    int n,i;
    long int fact=1;
    cout<<"Enter a number ";
    cin>>n;
    for (i=n;i>=1;i--)
    fact=fact*i;
    cout <<"Fatorial of "<<n<<" is = "<<fact;
    return 0;
}