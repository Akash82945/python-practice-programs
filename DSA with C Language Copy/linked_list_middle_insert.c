#include <stdio.h>
#include <stdlib.h>

struct node {
    int data;
    struct node *next;
} *head;

void createlist(int n);
void insertnode_at_middle(int data, int position);
void displaylist();

int main() {
    int n, data, position;
    printf("Enter the total number of nodes: ");
    scanf("%d", &n);
    createlist(n);
    printf("\nData in the list:\n");
    displaylist();

    printf("\nEnter data to insert into the list: ");
    scanf("%d", &data);

    printf("Enter the position to insert the new node: ");
    scanf("%d", &position);
    insertnode_at_middle(data, position);
    printf("Data in the list:\n");

    displaylist();
    return 0;
}

void createlist(int n) {
    struct node *newnode, *temp;
    int data, i;
    head = (struct node *)malloc(sizeof(struct node));
    if (head == NULL) {
        printf("Unable to allocate memory\n");
        return;
    }

    printf("Enter the data of node 1: ");
    scanf("%d", &data);
    head->data = data;
    head->next = NULL;
    temp = head;

    for (i = 2; i <= n; i++) {
        newnode = (struct node *)malloc(sizeof(struct node));
        if (newnode == NULL) {
            printf("Unable to allocate memory\n");
            break;
        }
        printf("Enter the data of node %d: ", i);
        scanf("%d", &data);
        newnode->data = data;
        newnode->next = NULL;
        temp->next = newnode;
        temp = temp->next;
    }
    printf("Singly linked list created successfully\n");
}

void insertnode_at_middle(int data, int position) {
    int i;
    struct node *newnode, *temp;
    newnode = (struct node *)malloc(sizeof(struct node));
    if (newnode == NULL) {
        printf("Unable to allocate memory\n");
        return;
    }

    newnode->data = data;
    newnode->next = NULL;
    temp = head;

    // Handle insertion at the start
    if (position == 1) {
        newnode->next = head;
        head = newnode;
        printf("Data inserted successfully\n");
        return;
    }

    // Traverse to the position before where we want to insert
    for (i = 1; i < position - 1; i++) {
        if (temp == NULL) {
            printf("Unable to insert data at given location\n");
            free(newnode); // Free the allocated memory for newnode
            return;
        }
        temp = temp->next;
    }

    // Insert the new node
    newnode->next = temp->next;
    temp->next = newnode;
    printf("Data inserted successfully\n");
}

void displaylist() {
    struct node *temp = head;
    if (temp == NULL) {
        printf("The list is empty.\n");
        return;
    }

    while (temp != NULL) {
        printf("Data = %d\n", temp->data);
        temp = temp->next;
    }
}