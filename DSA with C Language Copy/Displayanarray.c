#include <stdio.h>
int main()
{
    int a[10], i;
    printf("enter the element of array\n");
    for (i = 0; i < 10; i++)
    {
        scanf("%d", &a[i]);
    }
    printf("The entered array is\n");
    for (i = 0; i < 10; i++)
    {
        printf("%d", a[i]);
    }
    printf("\n");
    return 0;
}