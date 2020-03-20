//Calculate Average of Numbers entered by user Using Arrays.
#include <iostream>
using namespace std;
int main()
{
    int i, n, sum = 0;
    cout << "Enter the number of entry :";
    cin >> n;
    int arr[n];
    cout << "Enter the numbers\n";
    for (i = 0; i < n; i++)
    {
        cin >> arr[i];
    }
    for (i = 0; i < n; i++)
    {
        sum = sum + arr[i];
    }
    sum = sum / n;
    cout << "Average of numbers entered by the user :" << sum;
    return 0;
}