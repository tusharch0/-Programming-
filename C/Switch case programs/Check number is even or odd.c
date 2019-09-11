#include <stdio.h>
 
int main()
{
    int number;
     
    printf("Enter a positive integer number: ");
    scanf("%d",&number);
     
    switch(number%2) 
    {
        case 0:
            printf("%d is an EVEN number.\n",number);
            break;
        case 1:
            printf("%d is an ODD number.\n",number);
            break;
    }
     
    return 0;
}
