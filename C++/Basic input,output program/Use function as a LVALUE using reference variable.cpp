/*C++ program to use function as a LVALUE using reference 
variable.*/
 
#include  <iostream>
using namespace std;
 
int var ;
 
int& fun()
{
    return var;
}
 
int main()
{
    //Function used as LVALUE
    fun() = 10;
 
    cout << "Value of var : " << var << endl; 
 
    return 0;
}
