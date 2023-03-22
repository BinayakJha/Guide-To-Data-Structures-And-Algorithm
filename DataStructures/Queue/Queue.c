#include <stdio.h>
#define SIZE 100
int arr[SIZE];
// there will be two pointers front and rear
// front will point to the first element
// rear will point to the last element
int Front = -1; // Front will be -1 initially because there is no element in the queue
int Rear = -1; // Rear will be -1 initially because there is no element in the queue

void Enqueue(){
    int data;
    printf("Enter the data to be inserted in Queue: ");
    scanf("%d", &data);
    // if rear is equal to size-1 then queue is full
    if(Rear == SIZE-1){
        printf("Queue is full");
    }
    // if queue is not full then insert the data
    else{
        if(Front == -1){
            Front = 0;
        }
        Rear++;
        arr[Rear] = data;
        printf("Data inserted successfully \n");
    }

}

void Dequeue(){
    // if front is -1 then queue is empty
    if(Front == -1 || Front > Rear){
        printf("Queue is empty");
    }
    // if queue is not empty then delete the element
    else{
        printf("Deleted element is %d", arr[Front]);
        Front++; // increment front
    }
    
}

void Display(){
    // if front is -1 then queue is empty
    if(Front == -1){
        printf("Queue is empty");
    }
    // if queue is not empty then display the elements
    else{
        printf("Elements in the Queue are:  ");
        for(int i=Front; i<=Rear; i++){
            printf("%d ", arr[i]);
        }
    }
    
}

void exit(int status);

int main(){
    int choice, data;
    printf("\n 1. Enqueue Operation \n 2. Dequeue Operation \n 3. Display Operation \n 4. Exit");
    while(1){
        printf("\nEnter your choice: ");
        scanf("%d", &choice);
        switch(choice){
            case 1:
                Enqueue();
                break;
            case 2:
                Dequeue();
                break;
            case 3:
                Display();
                break;
            case 4:
                exit(0);
            default:
                printf("Invalid choice");
        }
    }
}