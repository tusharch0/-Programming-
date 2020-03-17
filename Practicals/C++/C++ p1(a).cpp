//Assuming there are 7.481 gallons in a cubic foot, write a program that asks the user to enter a number of gallons, and then displays the equivalent in cubic feet.
#include <iostream>
using namespace std;
int main()
{
    float g, f = 0;
    cout << "Enter the the number of gallons : ";
    cin >> g;
    f = float(g / 7.481);
    cout << "Equivelent cubic feet :" << f;
}