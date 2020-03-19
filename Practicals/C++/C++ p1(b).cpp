//The normal speed of a vehicle is less than 65kmph. If entered speed is less than 65kmph print within speed limit otherwise over speed limit.
#include <iostream>
using namespace std ;
int main()
{
    int speed;
    cout<<"Enter the speed of the vehicle in kmph :";
    cin>>speed;
    if (speed>65){
        cout<<"Over speed limit";
    }
    else {
        cout<<"With in speed limit";
    }
}