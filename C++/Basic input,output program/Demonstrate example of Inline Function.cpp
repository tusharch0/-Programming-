/*C++ program to demonstrate Inline Function.*/
#include  <iostream>
using namespace std;
 
//inline keyword is only use in declaration.
inline int fun();
 
int main()
{
    fun();
    return 0;
}
 
int fun()
{
    cout << "I am from inline function " << endl;
    return 0;
}
