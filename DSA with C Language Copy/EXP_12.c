#include <stdio.h>
#include <conio.h>
#include <stdlib.h>

struct node
{
    int data;
    struct node *next;
} *head;

void createlist(int n);
void delete_last_node();
void displaylist();

int main()
{
    int n, choise, clrscr();
    printf("Enter the total no of nodes:");
    scanf("%d", &n);

    createlist(n);
    printf("\nPress 1 to delete last node");
    scanf("%d", &choise);

    if (choise == 1)
        delete_last_node();
    printf("\nData in the list\n");
    displaylist();
    getch();
    return 0;
}

// to be continued