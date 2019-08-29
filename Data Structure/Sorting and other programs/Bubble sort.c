#include <stdio.h>
int main()
{
    int arr[100],limit,i,j,temp;
    printf("Enter the total no of element ");
    scanf ("%d",&limit);
    printf("Enter the array element ");
    for (i=0;i<limit;i++)
    {
        printf("Enter element %3d ",i+1);
        scanf("%d",&arr[i]);
    }
    for(i=0;i<(limit-1);i++)
    {
        for (j=0;j<(limit-i-1);j++)
        {
            if(arr[j]>arr[j+1])
            {
                temp=arr[j];
                arr[j]=arr[j+1];
                arr[j+1]=temp;
            }
        }
    }
    printf ("Array element in ascending order ");
    for (i=0;i<limit;i++)
    printf("%d",arr[i]);
    printf("/n");
    for (i=0;i<(limit-1);i++)
    {
        for(j=0;j<(limit-i-1);j++)
        {
            if(arr[j]<arr[j+1])
            {
                temp=arr[j];
                arr[j]=arr[j+1];
                arr[j+1]=temp;
            }
        }
    }
    printf ("Array element in descending order ");
    for (i=0;i<limit;i++)
    printf("%d",arr[i]);
    printf("/n");
    return 0;
}
