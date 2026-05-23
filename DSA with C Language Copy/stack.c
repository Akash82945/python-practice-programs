#include <stdio.h>
int stack[100], choise, n, top, x, i;

void push(void);
void pop(void);
void display(void);

int main()
{
    top = 1;
    printf("Enter the size of stack (Max=100):");
    scanf("%d", &n);
    printf("stack operations are:\n 1.Push\n 2.Pop\n 3.Dislay\n 4.Exit\n");

    do
    {
        printf("Enter your choise:");
        scanf("%d", &choise);
        switch (choise)
        {
        case 1:
        {
            push();
            break;
        }
        case 2:
        {
            pop();
            break;
        }
        case 3:
        {
            display();
            break;
        }
        case 4:
        {
            printf("Exit point\n");
            break;
        }
        default:
        {
            printf("Kindly enter right choise\n");
            break;
        }
        }
    } while (choise != 4);
    return 0;
}

void push()
{
    if (top == n - 1)
    {
        printf("stack overflow\n");
    }
    else
    {
        printf("enter the value to be pushed:");
        scanf("%d", &x);
        top++;
        stack[top] = x;
    }
}

void pop()
{
    if (top == -1)
    {
        printf("Stack is underflow\n");
    }
    else
    {
        printf("the popped element is:%d\n", stack[top]);
        top--;
    }
}

void display()
{
    if (top >= 0)
    {
        printf("the element of stack are:\n");
        for (i = top; i >= 0; i--)
        {
            printf("%d\n", stack[i]);
        }
        printf("enter the next choise:\n");
    }
    else
    {
        printf("the stack is empty\n");
    }
}