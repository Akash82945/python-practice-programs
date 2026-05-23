#include<stdio.h>
int main()
{
    int i,arr[10],data,n;
    printf("enter the number of element in the array:");
    scanf("%d",&n);

    printf("enter the element of array\n");
    for(i=0;i<n;i++)
    {
        scanf("%d",&arr[i]);
    }
    printf("enter the element to be inserted at the end:");
    scanf("%d",&data);
    arr[n]=data;
    n++;
    printf("the array after updation is\n");
    for(i=0;i<n;i++)
    {
        printf("%d",arr[i]);

    }
    printf("\n");
    return 0;
}