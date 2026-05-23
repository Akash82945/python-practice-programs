#include<stdio.h>
int main()
{
    int i,arr[50],data,n;
    printf("enter the number of element in the array:");
    scanf("%d",&n);
    printf("enter the element of the array\n");
    for(i=0;i<n;i++)
    {
        scanf("%d",&arr[i]);
    }
    for(i=0;i>0;i--)
    {
        arr[i]=arr[i-1];
    }
    printf("enter the value of new element to:");
    scanf("%d",&data);
    arr[0]=data;
    printf("the array after updation is\n");
    for(i=0;i<n;i++)
    {
        printf("%d",arr[i]);
    }
    return 0;
}