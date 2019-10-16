/*
    program to implement Binary Searching,
    to find an element in array.
*/
 
#include <stdio.h>
 
/*  function    : BinaryrSearch() */
  
int BinaryrSearch(int x[],int n,int item) 
{ 
    int L=0;        /*LOWER LIMIT   */
    int U=n-1;      /*UPPER LIMIT   */
    int mid;        /*MIDDLE INDEX  */
  
    while( L< U) 
    { 
        mid=(L+U)/2; 
        if(x[mid]==item)     return mid; 
        else if(x[mid] < item)    L=mid+1; 
        else if(x[mid] > item)    U=mid-1; 
    } 
    return -1; 
} 
  
int main() 
{ 
    int num=0,pos=0; 
     
    int ar[10],i; 
  
    printf("\nEnter array elements (in ASC Order...):\n"); 
    for(i=0;i<10;i++) 
    { 
        printf("Enter element %02d :",i+1); 
        scanf("%d",&ar[i]); 
    } 
  
    printf("\nEnter element to be searched :"); 
    scanf("%d",&num); 
  
    pos=BinaryrSearch(ar,10,num); 
    if(pos!=-1) { printf("\nItem found @ %02d location.\n",pos);} 
    else        { printf("\nItem not found.\n"); } 
    printf("\n"); 
    return 0;
}
