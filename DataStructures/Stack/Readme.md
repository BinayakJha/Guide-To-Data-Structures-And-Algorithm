# Stack in DSA:

## What is Stack?

A stack is a linear data structure that follows a particular order in which the operations are performed. 

The order is Last In First Out (LIFO).

A good example of a stack is any stack of objects like plates stacked over one another in the canteen. The plate which is at the top is the first one to be used i.e. the plate which has been placed at the topmost position is removed first.

## Image of Stack:

<img src= "https://upload.wikimedia.org/wikipedia/commons/b/b4/Lifo_stack.png" style="width:100%" alt="techiedelight.com/stack-implementation/">

## Algorithm:

```
Step 1: Start
Step 2: Declare a stack S
Step 3: Push elements into S
Step 4: Pop elements from S
Step 5: Stop
```

## Example:

```
S = [2, 4, 0, 1, 9]
```

### Solving the above example:

```
Step 1: Start
Step 2: S = []
Step 3: S = [2, 4, 0, 1, 9]
Step 4: S = [2, 4, 0, 1]
Step 5: Stop
```


## Implementation:

### C:

```c
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
```

### C++:

```cpp
#include <iostream>
using namespace std;

#define MAX 1000

class Stack{
    int top;

    public:
        int a[MAX];

        Stack(){
            top = -1;
        }

        bool push(int x);
        int pop();
        bool isEmpty();
};

bool Stack::push(int x){
    if (top >= (MAX-1)){
        cout << "Stack Overflow";
        return false;
    }
    else{
        a[++top] = x;
        cout << x << " pushed into stack\n";
        return true;
    }
}

int Stack::pop(){
    if (top < 0){
        cout << "Stack Underflow";
        return 0;
    }
    else{
        int x = a[top--];
        return x;
    }
}

bool Stack::isEmpty(){
    return (top < 0);
}

int main(){
    class Stack s;
    s.push(10);
    s.push(20);
    s.push(30);
    cout << s.pop() << " Popped from stack\n";
    return 0;
}
```

### Java:

```java
import java.util.Scanner;

class Stack{
    private int top;
    private int arr[];
    private int size;

    Stack(int size){
        this.size = size;
        arr = new int[size];
        top = -1;
    }

    public void push(int data){
        if (top == size-1){
            System.out.println("Stack is full !");
        }
        else{
            top++;
            arr[top] = data;
        }
    }

    public void pop(){
        if (top == -1){
            System.out.println("Stack is empty !");
        }
        else{
            System.out.println("Deleted element is " + arr[top]);
            top--;
        }
    }

    public void display(){
        if (top == -1){
            System.out.println("Stack is empty !");
        }
        else{
            System.out.println("Elements in the Stack are: ");
            for(int i=0; i<=top; i++){
                System.out.println(arr[i]);
            }
        }
    }

}

class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the size of the Stack: ");
        int size = sc.nextInt();
        Stack s = new Stack(size);
        int choice;
        System.out.println("1. Push");
        System.out.println("2. Pop");
        System.out.println("3. Display");
        System.out.println("4. Exit");
        while(true){
            System.out.println("Enter your choice: ");
            choice = sc.nextInt();
            switch(choice){
                case 1:
                    System.out.println("Enter the data to be inserted in Stack: ");
                    int data = sc.nextInt();
                    s.push(data);
                    break;
                case 2:
                    s.pop();
                    break;
                case 3:
                    s.display();
                    break;
                case 4:
                    System.exit(0);
                    break;
                default:
                    System.out.println("Invalid choice");
            }
        }
    }
}
```
