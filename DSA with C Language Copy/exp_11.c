#include <stdio.h>
#include <conio.h>
#include <stdlib.h>

struct node
{
    int data;
    struct node *next;
} *head;

void createlist(int n);
void delete_first_node();
void displaylist();

int main()
{
    int n, choise;

    printf("Enter the total no of nodes:");
    scanf("%d", &n);
    createlist(n);

    printf("\nData in the list\n");
    displaylist();

    printf("\nPress 1 to delete first node:");
    scanf("%d", &choise);

    if (choise == 1)

        delete_first_node();
    printf("\nData in the list\n");

    displaylist();
    getch();
    return 0;
}

void createlist(int n)
{
    struct node *newnode, *temp;
    int data, i;
    head = (struct node *)malloc(sizeof(struct node));
    if (head == NULL)
    {
        printf("Unnable to allocate memory.");
    }
    else
    {
        printf("Enter the data of node 1: ");
        scanf("%d", &data);

        head->data = data;
        head->next = NULL;
        temp = head;

        for (i = 2; i <= n; i++)
        {
            newnode = (struct node *)malloc(sizeof(struct node));
            if (newnode == NULL)
            {
                printf("Unnable to allocate memory.");
                break;
            }
            else
            {
                printf("enter the data of node%d", i);
                scanf("%d", &data);

                newnode->data = data;
                newnode->next = NULL;
                temp->next = newnode;

                temp = temp->next;
            }
        }
        printf("Singly linkedlist create successfully\n");
    }
}

void delete_first_node()
{
    struct node *to_delete;
    if (head == NULL)
    {
        printf("List is already empty");
    }
    else
    {
        to_delete = head;
        head = head->next;
        printf("\nData deleted=%d\n", to_delete->data);
        free(to_delete);

        printf("Successfully deleted first node from list\n");
    }
}

void displaylist()
{
    struct node *temp;
    if (head == NULL)
    {
        printf("List is empty");
    }
    else
    {
        temp = head;
        while (temp != NULL)
        {
            printf("Data =%d\n", temp->data);
            temp = temp->next;
        }
    }
}