/*C++ program to demonstrate example of Default Argument.*/
#include  <iostream>
using namespace std;
 
//Default argument must be trailer.
int sum(int x, int y=10, int z=20)
{
    return (x+y+z);
}
 
int main()
{
    cout << "Sum is : " << sum(5)       << endl;
    cout << "Sum is : " << sum(5,15)    << endl;
    cout << "Sum is : " << sum(5,15,25) << endl;
    return 0;
}
