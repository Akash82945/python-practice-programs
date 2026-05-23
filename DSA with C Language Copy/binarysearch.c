#include <stdio.h>
int main()
{
    int i, first, last, middle, n, search, arr[50];
    printf("enter the number of element:");
    scanf("%d", &n);
    printf("enter the element of an array\n");
    for (i = 0; i < n; i++)
    {
        scanf("%d", &arr[i]);
    }
    printf("enter the value to be searched:");
    scanf("%d", &search);

    first = 0;
    last = n - 1;
    while(first <= last)

    {
        middle=(first + last) / 2;
        if (arr[middle] == search)
        {
            printf("elemrnt found at location:%d", middle + 1);
            break;
        }
        else if (search < arr[middle])
        {
            last = middle - 1;
        }
        else if (search > arr[middle])
        {
            first = middle + 1;
        }
    }
    if (first > last)
    {
        printf("element not found");
    }
    return 0;
}