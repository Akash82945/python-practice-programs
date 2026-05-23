#include <stdio.h>
#include <stdlib.h>
#include <conio.h>

struct node
{
    int data;
    struct node *next
} *head;

void createlist(int n);
void insertion_at_end(int data);
void displaylist();

int main()
{
    int n, data;
    printf("Enter the total no of nodes:");
    scanf("%d", &n);
    createlist(n);

    printf("\nData in the list\n");
    displaylist();

    printf("enter data insert at ebd of the list:");
    scanf("%d", &data);
    insertion_at_end(data);

    printf("\nData in the list\n");
    displaylist();

    return 0;
}

void createlist(int n)
{
    struct node *newnode, *temp;
    int data, i;
    head = (struct node *)malloc(sizeof(struct node));
    if (head == NULL)
    {
        printf("unable to allocate memory");
    }
    else
    {
        printf("Enter the data of node1:");
        scanf("%d", &data);

        head->data = data;
        head->next = NULL;
        temp = head;

        for (i = 2; i <= n; i++)
        {
            newnode = (struct node *)malloc(sizeof(struct node));
            if (newnode == NULL)
            {
                printf("unable to allocate memory.");
                break;
            }
            else
            {
                printf("enter the data of node%d:", i);
                scanf("%d", &data);

                newnode->data = data;
                newnode->next = NULL;

                temp->next = newnode;
                temp = temp->next;
            }
        }
        printf("singly linkedlist created successfully\n");
    }
}

void insertion_at_end(int data)
{
    struct node *newnode, *temp;
    newnode = (struct node *)malloc(sizeof(struct node));
    if (newnode == NULL)
    {
        printf("unable to allocate memaor");
    }
    else
    {
        newnode->data = data;
        newnode->next = NULL;
        temp = head;
        while (temp != NULL && temp->next != NULL)
            temp = temp->next;
        temp->next = newnode;
        printf("Data inserted successfully\n");
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
            printf("Data=%d\n", temp->data);
            temp = temp->next;
        }
    }
    return 0;
}