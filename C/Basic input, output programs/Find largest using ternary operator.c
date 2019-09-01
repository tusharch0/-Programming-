#include <stdio.h>
int main()
{ 
    int a,b,c;
    int largest;
 
    printf("Enter three numbers (separated by space):");
    scanf("%d%d%d",&a,&b,&c);
 
    largest =((a>b && a>c)?a:((b>a && b>c)?b:c));
 
    printf("Largest number is = %d",largest);
 
    printf("Largest number is = %d",largest);   
    return 0;
}
