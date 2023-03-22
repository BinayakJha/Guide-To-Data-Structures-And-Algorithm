# Linear Search:

Linear search is a very simple search algorithm. In this type of search, a sequential search is made over all items one by one. Every item is checked and if a match is found then that particular item is returned, otherwise the search continues till the end of the data collection.

**Time Complexity:** O(n) where n is the number of elements in the array, because the worst case scenario is that the element is not present in the array and we have to traverse the whole array.

## Image of Linear Search Searching an Array:

<img src="https://4.bp.blogspot.com/-Oe596xjTKlM/W5DgdquPiZI/AAAAAAAADlk/dGruMjP_JLI-gdXo2DRxVJeYbvirr8ZOACLcBGAs/s1600/linear_search.gif"  width="100%"  style="width:100%" alt="Image from bp.blogspot.com">

## Algorithm:

```
Step 1: Set i to 1
Step 2: if i > n then go to step 7
Step 3: if A[i] = x then go to step 6
Step 4: Set i to i + 1
Step 5: Go to Step 2
Step 6: Print Element x Found at index i and go to step 8
Step 7: Print element not found
Step 8: Exit
```

## Example:

```
A = [2, 4, 0, 1, 9]
x = 1
n = 5
```
### Solving the above example:
```
Step 1: i = 1
Step 2: 1 <= 5
Step 3: A[1] = 4 != 1
Step 4: i = 2
Step 5: 2 <= 5
Step 3: A[2] = 0 != 1
Step 4: i = 3
Step 5: 3 <= 5
Step 3: A[3] = 1 = 1
Step 6: Print Element 1 Found at index 3
```

## Pseudocode:

```
procedure linear_search (list, value)

   for each item in the list
      if match item == value
         return the item's location
      end if
   end for

end procedure
```

## Implementation:

### C:

```c
#include <stdio.h>
// Search an element in an array using linear search
void search(int arr[], int n, int x){
    int i;
    for(i=0; i<n; i++){
        if(arr[i] == x){
            printf("Element found at index %d", i+1);
            return;
        }
    }
    printf("Element not found");
}
// Main function
int main(){

    int arr[] = {10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60};
    int n = sizeof(arr)/sizeof(arr[0]);
    int x = 35;
    search(arr, n, x);
    return 0;
}
```

### Java:

```java
public class LinearSearchExample
{  
 public static int linearSearch(int[] arr, int key)
 {  
  for(int i=0;i<arr.length;i++)
  {  
   if(arr[i] == key)
   {  
     return i;  
   }  
  }  
  return -1;  
 }

 public static void main(String a[])
 {  
  int[] a1= {10,20,30,50,70,90};  
  int key = 50;  
  System.out.println(key+" is found at index: "+linearSearch(a1, key));  
 }  
}  
```

### Python:

```python
def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

arr = [2, 0, 1, 9]
x = 1

print("Element found at index " + str(linear_search(arr, x)))
```

### C++:

```cpp
#include <iostream>
using namespace std;

int linearSearch(int arr[], int n, int x)
{
    for (int i = 0; i < n; i++)
        if (arr[i] == x)
            return i;
    return -1;
}

int main(void)
{
    int arr[] = { 2, 0, 1, 9 };
    int x = 1;
    int n = sizeof(arr) / sizeof(arr[0]);
    int result = linearSearch(arr, n, x);
    (result == -1)
        ? cout << "Element is not present in array"
        : cout << "Element is present at index " << result;
    return 0;
}
```