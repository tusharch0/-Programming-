/*C++ program to demonstrate example of cascading cout & cin.*/
#include  <iostream>
using namespace std;
 
int main()
{
    int a,b;
 
    //without cascading cout
    cout << "Enter value of a and b : ";
 
    //cascading cin
    cin >>a >>b;
 
    //cascading cout
    cout<< "A : " << a << ", B : " << b << endl;
 
    return 0;
}
