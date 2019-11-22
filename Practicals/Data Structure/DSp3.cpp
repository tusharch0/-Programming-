#include<iostream>
using namespace std;
void merge(int arr[], int l, int m, int r) 
{ 
    int i, j, k; 
    int n1 = m - l + 1; 
    int n2 =  r - m; 
    int L[n1], R[n2]; 
  
    for (i = 0; i < n1; i++) 
        L[i] = arr[ l+i]; 
    for (j = 0; j < n2; j++) 
        R[j] = arr[m + 1+ j]; 
  
    i = 0;  
    j = 0;  
    k = l;
    while (i < n1 && j < n2) 
    { 
        if (L[i] <= R[j]) 
        { 
            arr[k] = L[i]; 
            i++; k++;
        } 
        else
        { 
            arr[k] = R[j]; 
            j++; k++;
        }   
    } 
  
    while (i < n1) 
    { 
        arr[k] = L[i]; 
        i++; 
        k++; 
    } 
  
    while (j < n2) 
    { 
        arr[k] = R[j]; 
        j++; 
        k++; 
    } 
} 
  
void mergeSort(int arr[], int l, int r) 
{ 
    if (l < r) 
    { 
       int m=(l+r)/2; 
  
        mergeSort(arr, l, m); 
        mergeSort(arr, m+1, r); 
  
        merge(arr, l, m, r); 
    } 
} 
void insertionSort(int arr[],int sizeofarray){
int temp,j;
for(int i=0;i<sizeofarray;i++){
    temp=arr[i];
    for(j=i-1;j>=0&&temp<arr[j];j--){
        arr[j+1]=arr[j];
    }
    arr[j+1]=temp;
}
}
void bubbleSort(int arr[], int sizeofarray)
{
    int i, j;
    int temp;
    for (i = 0; i < sizeofarray-1; i++)
    for (j = 0; j < sizeofarray-i-1; j++)
        if (arr[j] > arr[j+1])
            {
                temp=arr[j];
                arr[j]=arr[j+1];
                arr[j+1]=temp;
            }
}
void selection(int arr[],int sizeofarray){
int i,j,temp,minimum,loc;
for(i=0;i<sizeofarray-1;i++){

    for(j=i+1;j<=sizeofarray-1;j++)
    {
        if(arr[j]<arr[i])
				{
        temp=arr[i];
        arr[i]=arr[j];
        arr[j]=temp;
        }

    }
    }
}
void display(int arr[],int sizeofarray){
cout<<endl<<"After sorting"<<endl;
for(int i=0;i<sizeofarray;i++){
    cout<<arr[i]<<" ";
}
}
int main(){
int arr[30];
int n,x,m;
cout<<"Enter the size of the array"<<endl;
cin>>n;
cout<<"Enter the elements in the array"<<endl;
for(int i=0;i<n;i++){
    cin>>arr[i];
}
cout<<endl<<"Entered  elements in the array"<<endl;
for(int i=0;i<n;i++){
    cout<<arr[i]<<""<<endl;
}
cout<<"\n1: For selection sort"<<endl;
cout<<"2: For bubble sort"<<endl;
cout<<"3: For insertion sort"<<endl;
cout<<"4: For merge sort"<<endl;
cout<<"5: For exit";

do{
cout<<endl;
cout<<"\nEnter which sorting are you prefer"<<endl;
cin>>m;
switch(m){
    case 1:
    selection(arr,n);
    break;
    case 2:
    bubbleSort(arr,n);
    break;
    case 3:
    insertionSort(arr,n);
    break;
    case 4:
    mergeSort(arr,0,n-1);
    break;
    case 5:
    exit(0);
}
 display(arr,n);}
 while(m!=5);
return 0;
}
