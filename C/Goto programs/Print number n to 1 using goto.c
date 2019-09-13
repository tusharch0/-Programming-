#include <stdio.h>
int main()
{

	int count,n;

	printf("Enter value of n: ");
	scanf("%d",&n);

	count =n;

	start: 
	printf("%d ",count);
	count--;

	if(count>=1)
		goto start;

	return 0;
}
