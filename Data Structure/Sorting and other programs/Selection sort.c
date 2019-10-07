#include <stdio.h>
#define MAX 100
 
int main()
{
    int arr[MAX],limit;
    int i,j,temp,position;
     
    printf("Enter total number of elements: ");
    scanf("%d",&limit);
     
    printf("Enter array elements: \n");
    for(i=0; i<limit; i++)
    {
        printf("Enter element %3d: ",i+1);
        scanf("%d",&arr[i]);
    }
     
    for(i=0; i<(limit); i++)
    {
        position=i;
        for(j=i+1; j<limit; j++)
        {
            if(arr[position]>arr[j])
            {
                position=j;
            }
            if(position!=i)
            {
                temp=arr[i];
                arr[i]=arr[position];
                arr[position]=temp;                
            }
        }
    }
 
    printf("Array elements in Ascending Order:\n");
    for(i=0; i<limit; i++)
        printf("%d ",arr[i]);
     
    printf("\n");
         
    for(i=0; i<(limit); i++)
    {
        position=i;
        for(j=i+1; j<limit; j++)
        {
            if(arr[position]<arr[j])
            {
                position=j;
            }
            if(position!=i)
            {
                temp=arr[i];
                arr[i]=arr[position];
                arr[position]=temp;                
            }
        }
    }
 
    printf("Array elements in Descending Order:\n");
    for(i=0; i<limit; i++)
        printf("%d ",arr[i]);
         
    printf("\n");
     
    return 0;
}
