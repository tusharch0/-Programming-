#include <stdio.h>
#include <math.h>

int  main()
{

    int a,cube;
    
    printf("Enter any integer number: ");
    scanf("%d",&a);
    cube = pow(a,3);
    printf("CUBE is: %d\n",cube);
    
    return 0;
}
