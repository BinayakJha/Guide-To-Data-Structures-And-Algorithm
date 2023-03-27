# Bubble Sort Algorithm:

Bubble sort is a simple sorting algorithm. This sorting algorithm is comparison-based algorithm in which each pair of adjacent elements is compared and the elements are swapped if they are not in order. 

This algorithm is not suitable for large data sets as its average and worst case complexity are of **Ο(n^2)** where n is the number of items.

## Image of Bubble Sort Sorting an Array:

<img src="https://upload.wikimedia.org/wikipedia/commons/c/c8/Bubble-sort-example-300px.gif" width="100%" style="width:100%" alt="Image from Wikipedia">


## Algorithm:

```
Step 1: Repeat Step 2 for i = 0 to n-1
Step 2: Repeat Step 3 for j = 0 to n-i-1
Step 3: if A[j] > A[j+1] then
            swap A[j] and A[j+1]
        end if
Step 4: end repeat
Step 5: end repeat
```

## Example:

```
A = [64, 34, 25]
```

### Solving the above example:

1) **First iteration**: 

    Compare 64 and 34. Since 64 is greater than 34, swap them to get ```[34, 64, 25]```. Compare 64 and 25. Since 64 is greater than 25, swap them to get ```[34, 25, 64]```.

2) **Second iteration**: 

    Compare 34 and 25. Since 34 is greater than 25, swap them to get ```[25, 34, 64]```. Compare 34 and 64. Since they are already in the correct order, do not swap them.

3) **Third iteration**: 

    Compare 25 and 34. Since they are already in the correct order, do not swap them. Compare 34 and 64. Since they are already in the correct order, do not swap them.


Now, the array is sorted in ascending order, and the Bubble Sort algorithm is complete. The sorted array is ```[25, 34, 64]```.


## Pseudocode:

```
procedure bubbleSort( A : list of sortable items )
   n = length(A)
   repeat 
     swapped = false
     for i = 1 to n-1 inclusive do
       /* if this pair is out of order */
       if A[i-1] > A[i] then
         /* swap them and remember something changed */
         swap( A[i-1], A[i] )
         swapped = true
       end if
     end for
   until not swapped
end procedure
```

## Implementation:

### C:

```c
#include <stdio.h>

void bubbleSort(int array[], int size) {
  for (int step = 0; step < size - 1; ++step) {
    for (int i = 0; i < size - step - 1; ++i) {
      // To sort in descending order, change > to < in this line.
      // Select the largest element in each loop.
      if (array[i] > array[i + 1]) {
        // swap if greater is at the rear position
        int temp = array[i];
        array[i] = array[i + 1];
        array[i + 1] = temp;
      }
    }
  }
}

void printArray(int array[], int size) {
  for (int i = 0; i < size; ++i) {
    printf("%d  ", array[i]);
  }
    printf(" \n");
}

int main() {
  int data[] = {20, 12, 10, 15, 2};
  int size = sizeof(data) / sizeof(data[0]);
  bubbleSort(data, size);
  printf("Sorted Array in Ascending Order:\n");
  printArray(data, size);
}
```

### C++:

```cpp
#include <iostream>
using namespace std;

void bubbleSort(int array[], int size) {
  for (int step = 0; step < size - 1; ++step) {
    for (int i = 0; i < size - step - 1; ++i) {
      // To sort in descending order, change > to < in this line.
      // Select the largest element in each loop.
      if (array[i] > array[i + 1]) {
        // swap if greater is at the rear position
        int temp = array[i];
        array[i] = array[i + 1];
        array[i + 1] = temp;
      }
    }
  }
}

void printArray(int array[], int size) {
  for (int i = 0; i < size; ++i) {
    cout << array[i] << "  ";
  }
  cout << " \n";
}

int main() {
  int data[] = {20, 12, 10, 15, 2};
  int size = sizeof(data) / sizeof(data[0]);
  bubbleSort(data, size);
  cout << "Sorted Array in Ascending Order:\n";
  printArray(data, size);
}
```

### Java:

```java
import java.util.Arrays;

public void bubbleSort(int[] arr) {
  int n = arr.length;
  int temp = 0;
  for(int i=0; i < n; i++){
    for(int j=1; j < (n-i); j++){
      if(arr[j-1] > arr[j]){
        //swap elements
        temp = arr[j-1];
        arr[j-1] = arr[j];
        arr[j] = temp;
      }
    }
  }
}

public static void main(String[] args) {
  int arr[] ={3,60,35,2,45,320,5};

  System.out.println("Array Before Bubble Sort");
  System.out.println(Arrays.toString(arr));

  bubbleSort(arr);//sorting array elements using bubble sort

  System.out.println("Array After Bubble Sort");
  System.out.println(Arrays.toString(arr));
}
```

### Python:

```python

def bubbleSort(array):
    for i in range(len(array)):
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp
    print("Sorted array is:")
    print(array)

data = [64, 34, 25, 12, 22, 11, 90]

bubbleSort(data)
```

