#include <iostream>
using namespace std;
class add
{
    private:
    int a;
    int b;
    public :
    void read(void);
    void print (void);
    int sum(void);
};
void add::read (void)
{
    cout << "Enter the First no.";
    cin>> a;
    cout<< "Enter the second no. ";
    cin>> b;
}
void add::print (void)
{
    cout<< "a = "<<a << "b = "<< b;
}
int add::sum (void)
{
    return (a+b);
}
int main()
{
    add a;
    int num;
    a.read ();
    num=a.sum();
    a.print();
    cout<<"Addition is "<<num;
    return 0;
}