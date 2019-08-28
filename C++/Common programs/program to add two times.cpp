#include <iostream>
using namespace std ;
int main ()
{
    int h1,m1,s1,h2,m2,s2,h,m,s;
    cout<< "Enter first time ";
    cout<<"hours : ";
    cin>>h1;
    cout<<"minutes : ";
    cin>>m1;
    cout<<"second : ";
    cin>>s1;
    cout<<"Enter second time ";
    cout<<"hours : ";
    cin>>h2;
    cout<<"minutes : ";
    cin>>m2;
    cout<<"second : ";
    cin>>s2;
    s=s1+s2;
    m=m1+m2+(s/60);
    h=h1+h2+(m/60);
    m=m%60;
    s=s%60;
    cout<<"time is : ";
    cout <<h<<" hour "<<m<<" minute "<<s<<" second ";
    return 0;
}