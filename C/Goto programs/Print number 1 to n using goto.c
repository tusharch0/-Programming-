#include <stdio.h>

int main()
{
	int count,n;

	printf("Enter the ");
	scanf("%d",&n);

	count =1;

	start: 
	printf("%d ",count);
	count++;

	if(count<=n)
		goto start;

	return 0;
}