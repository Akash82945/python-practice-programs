#include <stdio.h>

int queue[50], front = -1, rear = -1, n, i, x, choise;

void insert();
void delete();
void display();

int main()
{
    printf("Enter the size of the Queue:\n");
    scanf("%d", &n);
    printf("Queue operations are:\n 1. Insert\n 2. Delete\n 3. Display\n 4. Exit\n");

    do
    {
        printf("Enter your choice:\n");
        scanf("%d", &choise);
        switch (choise)
        {
        case 1:
            insert();
            break;
        case 2:
            delete();
            break;
        case 3:
            display();
            break;
        case 4:
            printf("Exiting the program.\n");
            break;

        default:
            printf("Kindly enter the right choice\n");
            break;
        }
    } while (choise != 4);
    return 0;
}

void insert()
{
    if (rear == n - 1) // Check for overflow
    {
        printf("Queue is overflow\n");
    }
    else if (front == -1) // Queue is empty
    {
        front = rear = 0; // Initialize front and rear
        printf("Element to be inserted:\n");
        scanf("%d", &x);
        queue[rear] = x; // Insert the first element
    }
    else
    {
        printf("Element to be inserted:\n");
        scanf("%d", &x);
        rear++; // Move rear to the next position
        queue[rear] = x; // Insert the element
    }
}

void delete()
{
    if (front == -1) // Check for underflow
    {
        printf("Queue is underflow\n");
    }
    else if (front == rear) // Only one element was in the queue
    {
        printf("The deleted element is: %d\n", queue[front]);
        front = rear = -1; // Reset the queue
    }
    else
    {
        printf("The deleted element is: %d\n", queue[front]);
        front++; // Move front to the next position
    }
}

void display()
{
    if (front == -1)
    {
        printf("Queue is empty\n");
    }
    else
    {
        printf("The elements in the queue are:\n");
        for (i = front; i <= rear; i++)
        {
            printf("%d ", queue[i]); // Print each element
        }
        printf("\n"); // New line after displaying all elements
    }
}