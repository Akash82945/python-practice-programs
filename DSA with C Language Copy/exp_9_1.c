#include <stdio.h>
#include <stdlib.h>

struct node {
    int data;
    struct node *next;
} *head = NULL; // Initialize head to NULL

void createlist(int n);
void insertion_at_end(int data);
void displaylist();

int main() {
    int n, data;
    printf("Enter the total number of nodes: ");
    scanf("%d", &n);
    createlist(n);

    printf("\nData in the list:\n");
    displaylist();

    printf("Enter data to insert at the end of the list: ");
    scanf("%d", &data);
    insertion_at_end(data); // Correct function name

    printf("\nData in the list after insertion:\n");
    displaylist();

    return 0;
}

void createlist(int n) {
    struct node *newnode, *temp;
    int data, i;
    head = (struct node *)malloc(sizeof(struct node));
    if (head == NULL) {
        printf("Unable to allocate memory\n");
        return; // Exit if memory allocation fails
    } else {
        printf("Enter the data of node 1: ");
        scanf("%d", &data);

        head->data = data;
        head->next = NULL;
        temp = head;

        for (i = 2; i <= n; i++) {
            newnode = (struct node *)malloc(sizeof(struct node));
            if (newnode == NULL) {
                printf("Unable to allocate memory.\n");
                break;
            } else {
                printf("Enter the data of node %d: ", i);
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

void insertion_at_end(int data) {
    struct node *newnode, *temp;
    newnode = (struct node *)malloc(sizeof(struct node));
    if (newnode == NULL) {
        printf("Unable to allocate memory.\n");
        return; // Exit if memory allocation fails
    }
    newnode->data = data;
    newnode->next = NULL;

    if (head == NULL) { // If the list is empty
        head = newnode; // Set head to new node
    } else {
        temp = head;
        while (temp->next != NULL) // Traverse to the end of the list
            temp = temp->next;
        temp->next = newnode; // Link the new node at the end
    }
    printf("Data inserted successfully\n");
}

void displaylist() {
    struct node *temp;
    if (head == NULL) {
        printf("List is empty\n");
    } else {
        temp = head;
        while (temp != NULL) {
            printf("Data = %d\n", temp->data);
            temp = temp->next;
        }
    }
}