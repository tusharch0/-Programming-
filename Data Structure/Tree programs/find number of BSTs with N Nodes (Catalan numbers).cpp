#include <iostream>
using namespace std;

int CN(int n){
	int Cn =0;
	// base case
	if(n==0) // empty tree
	{
		return 1;
	}
	for(int i=1;i<n+1;i++)
	{
		Cn+= CN(i-1)*CN(n-i);
	}
	return Cn;
}

int main(){
	int n;
	cout<<"Enter number of nodes: ";
	cin>>n;
	cout<<n<<endl;
	int trees=CN(n);
	cout<<trees<<" binary search trees are there for "<<n<<" nodes"<<endl;
	return 0; 
}
