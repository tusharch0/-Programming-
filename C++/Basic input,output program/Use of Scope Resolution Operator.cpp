/*C++ program to demonstrate use of Scope Resolution Operator,
Use global variable in local scope*/
 
#include  <iostream>
using namespace std;
int a = 20;
 
int main()
{
    int a = 10;
 
    cout << "Value of local  a: " << a << endl;
 
    //use of SRO (::) to access global variable.
    cout << "Value of global a: " << ::a << endl;
 
    return 0;
}
