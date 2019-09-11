#include <stdio.h>

typedef int I;
typedef char C;
typedef float F;

int main()
{
	I intVar = 10;
	C charVar = 'X';
	F floatVar = 10.23f;
	
	printf("intVar = %d\n",intVar);
	printf("charVar = %c\n",charVar);
	printf("floatVar = %f\n",floatVar);
	
	return 0;
}
