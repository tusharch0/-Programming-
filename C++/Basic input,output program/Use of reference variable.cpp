/*C++ program to demonstrate use of reference variable.*/
#include <iostream>
using namespace std;
 
int main()
{
    int a=10;
 
    /*reference variable is alias of other variable, 
    It does not take space in memory*/
 
    int &b = a; 
 
    cout << endl << "Value of a: " << a;
    cout << endl << "Value of b: " << b << endl;
 
    return 0;
}
