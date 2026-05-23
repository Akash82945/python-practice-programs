#include <stdio.h>
#include <conio.h>
#include <stdlib.h>

struct node
{
    int data;
    struct node *next
} *head;

void createlist(int n);
void insertnode_At_begining(int data);
void displaylist();

int main()
{
    int n, data, i, clrscr();
    printf("enter  the total no of nodes:");
    scanf("%d", &n);

    createlist(n);
    printf("\nData in the list\n");

    displaylist();
    printf("\nEnter data to the insert begining of the list:");
    scanf("%d", &data);

    insertnode_At_begining(data);
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
        printf("unable to allocate mamory.");
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
                printf("Enter the data of node%d:", i);
                scanf("%d", &data);
                newnode->data = data;
                newnode->next = NULL;
                temp->next = newnode;

                temp = temp->next;
            }
        }
        printf("Singly linked list created successfully\n");
    }
}

void insertnode_At_begining(int data)
{
    struct node *newnode;
    newnode = (struct node *)malloc(sizeof(struct node));
    if (newnode == NULL)
    {
        printf("unable to allocate memeoy.");
    }
    else
    {
        newnode->data = data;
        newnode->next = head;
        head = newnode;
        printf("Data inserted successfully\n");
    }
}

void displaylist()
{
    struct node *temp;
    if (head == NULL)
    {
        printf("List is empty.");
    }
    else
    {
        temp = head;
        while (temp != NULL)
        {
            printf("Data %d\n", temp->data);
            temp = temp->next;
        }
    }
    return 0;
}