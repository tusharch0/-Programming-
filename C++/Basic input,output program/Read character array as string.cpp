#include <iostream>
using namespace std;

int main()
{
	char firstName[30], secondName[30];

	//input values
	cout<<"What is your first name? ";
	cin>>firstName;
	cout<<"What is your second name? ";
	cin>>secondName;

	//printing
	cout<<"Hi "<<firstName<<" "<<secondName<<endl;
	
	return 0;
}
