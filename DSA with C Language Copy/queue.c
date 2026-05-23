#include <stdio.h>
int queue[50], front = -1, rear = -1, n, i, x, choise;

void insert();
void delete();
void display();
void exit();

int main()
{
    printf("enter the size of the Queue:\n");
    scanf("%d", &n);
    printf("Queue operations are:\n 1.insert\n 2.delete\n 3.display\n 4.exit\n");

    do
    {
        printf("Enter your choise:\n");
        scanf("%d",&choise);
        switch (choise)
        {
        case 1:
            insert();
            break;
        case 2:
            delete ();
            break;
        case 3:
            display();
            break;
        case 4:
            exit(0);
            break;

        default:
            printf("Kindly enter the right choise");
            break;
        }
    } while (choise != 4);
    return 0;
}

void insert()
{
    if (front == n - 1)
    {
        printf("Queue is overload");
    }
    else if (front = rear = -1)
    {
        front = rear = 0;
    }
    else
    {
        printf("Element to be inserted:\n");
        scanf("%d", &x);
        rear = rear + 1;
        queue[rear] = x;
    }
}

void delete()
{
    if (front == n - 1)
    {
        printf("Queue is underflow");
    }
    else if (front = rear)
    {
        front = rear = -1;
    }
    else
    {
        printf("The delet elment is:%d\n", queue[front]);
        front = front + 1;
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
        printf("The element in the queue are:\n");
        for (i = front; i <= rear; i++)
        {
            printf("%d", queue[i]);
        }
    }
    printf("%n");
}