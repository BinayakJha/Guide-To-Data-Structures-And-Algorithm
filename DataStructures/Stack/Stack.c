#include <stdio.h>
#define SIZE 100
int arr[SIZE];
int top = -1;

void push(){
    int data;

    if (top == SIZE-1){
        printf("\n Stack is full !");
    }
    else{
        printf("\n Enter the data to be inserted in Stack: ");
        scanf("%d", &data);
        top++;
        arr[top] = data;
    }

}

void pop(){
    if (top == -1){
        printf("\n Stack is empty !");
    }
    else{
        printf("\n Deleted element is %d", arr[top]);
        top--;
        printf("\n");
    }

}

void display(){
    if (top == -1){
        printf(" \nStack is empty !");
    }
    else{
        printf("\n Elements in the Stack are:  ");
        for(int i=0; i<=top; i++){
            printf("%d ", arr[i]);
        }
        printf("\n");
    }

}

void exit(int status);

int main(){
    int choice;
    printf("\n 1. Push");
    printf("\n 2. Pop");
    printf("\n 3. Display");
    printf("\n 4. Exit");
    while(1){
        printf("\n Enter your choice: ");
        scanf("%d", &choice);
        switch(choice){
            case 1:
                push();
                break;
            case 2:
                pop();
                break;
            case 3:
                display();
                break;
            case 4:
                exit(0);
                break;
            default:
                printf("\n Invalid choice");
        }
    }
    return 0;
}