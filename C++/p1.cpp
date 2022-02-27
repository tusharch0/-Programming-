#include <iostream>
using namespace std;
 
class first {
    public:
        void swapByValue(int a, int b){
            int c;

            c = a;
            a = b;
            b = c;
        }
        void swapByRef(int &a, int &b){
            int c;

            c = a;
            a = b;
            b = c;
        }
        void swapByAdr(int *a, int *b){
            int c;

            c = *a;
            *a = *b;
            *b = c;
        }
}  
 
int main()
{
    first f1;
    int x = 10;
    int y = 20;
 
    cout << endl;
    cout << "Value before Swapping x:" << x << " y:" << y << endl;
    f1.swapByValue( x , y  ); /*In call by value swapping does not reflect in calling function*/
    cout << "Value After  Swapping x:" << x << " y:" << y << endl << endl; 
 
    cout << "Value before Swapping x:" << x << " y:" << y << endl;
    f1.swapByRef( x , y  );  /*Swapping reflect but reference does not take space in memory*/
    cout << "Value After  Swapping x:" << x << " y:" << y << endl << endl; 
 
    x = 50;
    y = 100;
 
    cout << "Value before Swapping x:" << x << " y:" << y << endl;
    f1.swapByAdr( &x , &y  ); /*Swapping reflect but pointer takes space in memory*/
    cout << "Value After  Swapping x:" << x << " y:" << y << endl << endl;  
 
    return 0;
}

# this is the first AI program

#  Mission To Find Her 

# All information i have I met her on 10:55 am  sunday 11 july 2021 Location Vartmaan Online Services plot no.-348 Industrial area phase 1 chandigarh 160002.

# step to find
step 1 : all mobile phone active in that location in that time and she left within 45 mins with 2 more phones in car no.PB0D0376
step 2 : once you get the number its all done get linked fb,insta,