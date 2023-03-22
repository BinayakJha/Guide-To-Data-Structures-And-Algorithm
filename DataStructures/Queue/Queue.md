# Queue in DSA:

## What is Queue?

A queue is a linear data structure that follows a particular order in which the operations are performed. 

The order is First In First Out (FIFO). 

A good example of a queue is any queue of consumers for a resource where the consumer that came first is served first. The difference between stacks and queues is in removing. In a stack we remove the item the most recently added; in a queue, we remove the item the least recently added.

## Image of Queue:

<img src="https://miro.medium.com/v2/resize:fit:1280/0*E33E-AjyAUTFjVmM.gif" width="100%" style="width:100%" alt="miro.medium.com">

## Algorithm:

```
Step 1: Start
Step 2: Declare a queue Q
Step 3: Enqueue elements into Q
Step 4: Dequeue elements from Q
Step 5: Stop
```

## Example:

```
Q = [2, 4, 0, 1, 9]
```

### Solving the above example:

```
Step 1: Start
Step 2: Q = []
Step 3: Q = [2, 4, 0, 1, 9]
Step 4: Q = [4, 0, 1, 9]
Step 5: Stop
```

## Implementation:

### C:

```c

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
```

### C++:

```cpp

#include <iostream>
using namespace std;

#define SIZE 100
int arr[SIZE];
// there will be two pointers front and rear
// front will point to the first element
// rear will point to the last element

int Front = -1; // Front will be -1 initially because there is no element in the queue
int Rear = -1; // Rear will be -1 initially because there is no element in the queue

void Enqueue(){
    int data;
    cout<<"Enter the data to be inserted in Queue: ";
    cin>>data;
    // if rear is equal to size-1 then queue is full
    if(Rear == SIZE-1){
        cout<<"Queue is full";
    }
    // if queue is not full then insert the data
    else{
        if(Front == -1){
            Front = 0;
        }
        Rear++;
        arr[Rear] = data;
        cout<<"Data inserted successfully \n";
    }

}

void Dequeue(){
    // if front is -1 then queue is empty
    if(Front == -1 || Front > Rear){
        cout<<"Queue is empty";
    }
    // if queue is not empty then delete the element
    else{
        cout<<"Deleted element is "<<arr[Front];
        Front++; // increment front
    }
    
}

void Display(){
    // if front is -1 then queue is empty
    if(Front == -1){
        cout<<"Queue is empty";
    }
    // if queue is not empty then display the elements
    else{
        cout<<"Elements in the Queue are:  ";
        for(int i=Front; i<=Rear; i++){
            cout<<arr[i]<<" ";
        }
    }
    
}

int main(){
    int choice, data;
    cout<<"\n 1. Enqueue Operation \n 2. Dequeue Operation \n 3. Display Operation \n 4. Exit";
    while(1){
        cout<<"\nEnter your choice: ";
        cin>>choice;
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
                cout<<"Invalid choice";
        }
    }
} 
```

### Java:

```java
import java.util.Scanner;

public class Queue {
    static int SIZE = 100;
    static int arr[] = new int[SIZE];
    static int Front = -1; // Front will be -1 initially because there is no element in the queue
    static int Rear = -1; // Rear will be -1 initially because there is no element in the queue

    static void Enqueue(){
        int data;
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the data to be inserted in Queue: ");
        data = sc.nextInt();
        // if rear is equal to size-1 then queue is full
        if(Rear == SIZE-1){
            System.out.println("Queue is full");
        }
        // if queue is not full then insert the data
        else{
            if(Front == -1){
                Front = 0;
            }
            Rear++;
            arr[Rear] = data;
            System.out.println("Data inserted successfully \n");
        }

    }

    static void Dequeue(){
        // if front is -1 then queue is empty
        if(Front == -1 || Front > Rear){
            System.out.println("Queue is empty");
        }
        // if queue is not empty then delete the element
        else{
            System.out.println("Deleted element is "+arr[Front]);
            Front++; // increment front
        }
        
    }

    static void Display(){
        // if front is -1 then queue is empty
        if(Front == -1){
            System.out.println("Queue is empty");
        }
        // if queue is not empty then display the elements
        else{
            System.out.println("Elements in the Queue are:  ");
            for(int i=Front; i<=Rear; i++){
                System.out.print(arr[i]+" ");
            }
        }
        
    }

    public static void main(String[] args) {
        int choice, data;
        System.out.println("\n 1. Enqueue Operation \n 2. Dequeue Operation \n 3. Display Operation \n 4. Exit");
        while(true){
            System.out.println("\nEnter your choice: ");
            Scanner sc = new Scanner(System.in);
            choice = sc.nextInt();
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
                    System.exit(0);
                default:
                    System.out.println("Invalid choice");
            }
        }
    }
}
```

### Python:

```python
SIZE = 100
arr = [None] * SIZE
Front = -1 # Front will be -1 initially because there is no element in the queue
Rear = -1 # Rear will be -1 initially because there is no element in the queue

def Enqueue():
    data = int(input("Enter the data to be inserted in Queue: "))
    # if rear is equal to size-1 then queue is full
    if Rear == SIZE-1:
        print("Queue is full")
    # if queue is not full then insert the data
    else:
        if Front == -1:
            Front = 0
        Rear += 1
        arr[Rear] = data
        print("Data inserted successfully \n")

def Dequeue():
    # if front is -1 then queue is empty
    if Front == -1 or Front > Rear:
        print("Queue is empty")
    # if queue is not empty then delete the element
    else:
        print("Deleted element is ", arr[Front])
        Front += 1 # increment front

def Display():
    # if front is -1 then queue is empty
    if Front == -1:
        print("Queue is empty")
    # if queue is not empty then display the elements
    else:
        print("Elements in the Queue are:  ")
        for i in range(Front, Rear+1):
            print(arr[i], end=" ")

print("\n 1. Enqueue Operation \n 2. Dequeue Operation \n 3. Display Operation \n 4. Exit")

while True:
    choice = int(input("\nEnter your choice: "))
    if choice == 1:
        Enqueue()
    elif choice == 2:
        Dequeue()
    elif choice == 3:
        Display()
    elif choice == 4:
        break
    else:
        print("Invalid choice")
```

