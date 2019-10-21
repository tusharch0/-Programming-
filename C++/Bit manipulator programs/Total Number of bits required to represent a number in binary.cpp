#include<bits/stdc++.h>
using namespace std;

int countBits(int n)
{
	int count=0;
	// While loop will run until we get n = 0
	while(n)
	{
		count++;
		// We are shifting n to right by 1 
		// place as explained above
		n=n>>1;
	}
	return count;
}


int main()
{
	int n;
	cout << "Enter any Number\n";
	cin >> n;
	int count=countBits(n);
	cout << "Number of bits : " << count ;
	return 0;
}
