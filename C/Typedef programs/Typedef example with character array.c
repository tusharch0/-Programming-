#include <stdio.h>
#include <string.h>

#define MAXLEN 50

typedef char CHRArray[MAXLEN];
typedef unsigned char BYTE;

int main()
{
	CHRArray name;
	CHRArray city;
	BYTE age;
	
	strcpy(name, "Tushar Choudhary");
	strcpy(city, "Chandigarh, UT, India");
	age = 21;
	
	printf("Name: %s\n", name);
	printf("city: %s\n", city);
	printf("Age : %u\n", age);
	
	return 0;
}
