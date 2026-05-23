#include<stdio.h>
int main()
{
    int array[100],search,i,n,flay=0;
    printf("enterr the number of element in the array:");
    scanf("%d",&n);
    printf("enter the element of array\n");
    for(i=0;i<n;i++)
    {
        scanf("%d",&array[i]);
    }
    printf("enter the number to be searched:");
    scanf("%d",&search);
    for(i=0;i<n;i++)
    {
        if(array[i]==search)
        {
            printf("element found at the location: %d",i);
            flay=1;
            break;
        }
    }
    if(flay==0)
    {
        printf("element not found");
    }
    return 0;
}