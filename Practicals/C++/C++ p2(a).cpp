//Program to generate the Fibonacci series up to user specified limit.
#include <iostream>
using namespace std;
int main()
{
    int i = 1, n, sum = 1, j, b = 1;
    cout << "Enter the limit :";
    cin >> n;
    cout << i << " ";
    for (j = 0; sum < n; j++)
    {
        cout << sum << " ";
        sum = b + i;
        i = b;
        b = sum;
    }
    return 0;
}
