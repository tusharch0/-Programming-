#include <iostream>
using namespace std;
int main()
{
    char str[100]={0};
    cout<< "Enter the string ";
    cin>> str ;     //cin does not take string after space 
    cout<< "Input string is "<<str;
    cout<< " Enter the string ";
    cin.getline (str,100);  //cin.getline read string with space 
    cout << "Input string is "<<str;
    return 0;
}