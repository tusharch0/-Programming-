//Write a program that reads two nos. from keyboard and gives their addition, subtraction, multiplication, division and modulus
#include <stdio.h>
#include <conio.h>
int main()
{
    int a, b;
    printf("Enter two numbers\n");
    scanf("%d%d", &a, &b);
    printf("The sum of two numbers is %d\n", a + b);
    printf("The subtraction of two numbers is %d\n", a - b);
    printf("The Multiplication of two numbers is %d\n", a * b);
    printf("The devision of two numbers is %d\n", a / b);
    printf("The Modulus of two numbers is %d\n", a % b);
    return 0;
}