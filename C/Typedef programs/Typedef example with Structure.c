#include <stdio.h>
#include <string.h>

struct student_str 
{
	char name[30];
	int age;
};

typedef struct {
	char name[30];
	int age;
}employee_str;

int main()
{
    
	struct student_str std;
	employee_str emp;
	
	strcpy(std.name, "Tushar Choudhary");
	std.age = 21;
	
	strcpy(emp.name, "Tushar");
	emp.age = 20;
	
	printf("Student detail:\n");
	printf("Name: %s\n",std.name);
	printf("Age: %d\n",std.age);
	
	printf("Employee detail:\n");
	printf("Name: %s\n",emp.name);
	printf("Age: %d\n",emp.age);	
	
	return 0;
}
