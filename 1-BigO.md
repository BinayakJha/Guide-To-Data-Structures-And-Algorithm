# Big O: A Beginner's Guide:

## What is Big O?

Big O is a way to measure the efficiency of an algorithm. It is a way to describe the performance or complexity of an algorithm. It is a way to compare the efficiency of different algorithms.

In Simple terms, **Big O is a way to measure how fast an algorithm is or As your input grows, how fast does the runtime of your algorithm grow.**

The Big O notation is expressed using a mathematical formula that uses the letter "O" and a function of "n," which represents the input size. 

The notation represents the rate of growth of an algorithm's runtime in terms of the input size.


## How To Calculate Big O?

The Simplest trick to know the Big O of a function is to look for the loops in the function. 

1) If there is a loop, then the Big O is O(n). 

2) If there are two loops, then the Big O is O(n^2).

3) If there are three loops, then the Big O is O(n^3). 

And so on. **(n is the number of items in the loop)**

For example, consider the following functions in C, Python and Java.

### **Example**

1) **C :** 
```C
int sum(int n) {
    int total = 0;
    for (int i = 0; i < n; i++) {
        total += i;
    }
    return total;
}
```

2) **Python :**
```Python
def sum(n):
    total = 0
    for i in range(n):
        total += i
    return total
```

3) **Java :**
```Java
public int sum(int n) {
    int total = 0;
    for (int i = 0; i < n; i++) {
        total += i;
    }
    return total;
}
```

This code has a loop that iterates n times, so the Big O notation for this code is O(n).


## Some Common Big O's Notations:

1) **O(1)** : Constant Time - No Loops

Examples of O(1):

```C
// C Code
int print_first_element(int[] lst) {
    printf("%d", lst[0]);
}
```

```Python
# Python Code
def print_first_element(lst):
    print(lst[0])
```

```Java
// Java Code
public void print_first_element(int[] lst) {
    System.out.println(lst[0]);
}
```

2) **O(n)** : Linear Time - 1 Loop

Examples of O(n):

```C
// C Code
int sum(int n) {
    int total = 0;
    for (int i = 0; i < n; i++) {
        total += i;
    }
    return total;
}
```

```Python
# Python Code
def sum(n):
    total = 0
    for i in range(n):
        total += i
    return total
```

```Java
// Java Code
public int sum(int n) {
    int total = 0;
    for (int i = 0; i < n; i++) {
        total += i;
    }
    return total;
}
```

3) **O(n^2)** : Quadratic Time - 2 Loops

Examples of O(n^2):

```C
// C Code
int sum_of_pairs(int n) {
    int total = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            total += i + j;
        }
    }
    return total;
}
```

```Python
# Python Code
def sum_of_pairs(n):
    total = 0
    for i in range(n):
        for j in range(n):
            total += i + j
    return total
```

```Java
// Java Code
public int sum_of_pairs(int n) {
    int total = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            total += i + j;
        }
    }
    return total;
}
```

4) **O(log n)** : Logarithmic Time - Usually searching algorithms have log n if they are sorted (Binary Search)

Examples of O(log n):

```C
// C Code
int binary_search(int[] lst, int target) {
    int low = 0;
    int high = lst.length - 1;
    while (low <= high) {
        int mid = (low + high) / 2;
        int guess = lst[mid];
        if (guess == target) {
            return mid;
        }
        if (guess > target) {
            high = mid - 1;
        } else {
            low = mid + 1;
        }
    }
    return -1;
}
```

```Python
# Python Code
def binary_search(lst, target):
    low = 0
    high = len(lst) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = lst[mid]
        if guess == target:
            return mid
        if guess > target:
            high = mid - 1
        else:
            low = mid + 1
    return -1
```

```Java
// Java Code
public int binary_search(int[] lst, int target) {
    int low = 0;
    int high = lst.length - 1;
    while (low <= high) {
        int mid = (low + high) / 2;
        int guess = lst[mid];
        if (guess == target) {
            return mid;
        }
        if (guess > target) {
            high = mid - 1;
        } else {
            low = mid + 1;
        }
    }
    return -1;
}
```

5) **O(n log n)** : Log Linear Time - Usually sorting operations

Examples of O(n log n):

```C
// C Code
void merge_sort(int[] lst) {
    if (lst.length < 2) {
        return;
    }
    int mid = lst.length / 2;
    int[] left = new int[mid];
    int[] right = new int[lst.length - mid];
    for (int i = 0; i < mid; i++) {
        left[i] = lst[i];
    }
    for (int i = mid; i < lst.length; i++) {
        right[i - mid] = lst[i];
    }
    merge_sort(left);
    merge_sort(right);
    merge(left, right, lst);
}
```

```Python
# Python Code
def merge_sort(lst):
    if len(lst) < 2:
        return
    mid = len(lst) // 2
    left = lst[:mid]
    right = lst[mid:]
    merge_sort(left)
    merge_sort(right)
    merge(left, right, lst)
```

```Java
// Java Code
public void merge_sort(int[] lst) {
    if (lst.length < 2) {
        return;
    }
    int mid = lst.length / 2;
    int[] left = new int[mid];
    int[] right = new int[lst.length - mid];
    for (int i = 0; i < mid; i++) {
        left[i] = lst[i];
    }
    for (int i = mid; i < lst.length; i++) {
        right[i - mid] = lst[i];
    }
    merge_sort(left);
    merge_sort(right);
    merge(left, right, lst);
}
```

6) **O(2^n)** : Exponential Time - Usually recursive algorithms that solves a problem of size N

**Examples of O(2^n):**

```C
// C Code
int fibonacci(int n) {
    if (n == 0) {
        return 0;
    } else if (n == 1) {
        return 1;
    } else {
        return fibonacci(n - 1) + fibonacci(n - 2);
    }
}
```

```Python
# Python Code
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
```

```Java
// Java Code
public int fibonacci(int n) {
    if (n == 0) {
        return 0;
    } else if (n == 1) {
        return 1;
    } else {
        return fibonacci(n - 1) + fibonacci(n - 2);
    }
}
```

7) **O(n!)** : Factorial Time - Usually recursive algorithms that solves a problem of size N

**Examples of O(n!):**

```C
// C Code
int permutation(int[] lst, int k) {
    if (k == 1) {
        return 1;
    } else {
        return k * permutation(lst, k - 1);
    }
}
```

```Python
# Python Code
def permutation(lst, k):
    if k == 1:
        return 1
    else:
        return k * permutation(lst, k - 1)
```

```Java
// Java Code
public int permutation(int[] lst, int k) {
    if (k == 1) {
        return 1;
    } else {
        return k * permutation(lst, k - 1);
    }
}
```

### Big O Graph:

<img src="https://misc-flexiple.s3.amazonaws.com/bon_cheat_sheet.jpg">

You can see in the graph that the time complexity of the algorithm increases as the input size increases except for O(1) and O(log n) which are constant and logarithmic time complexity respectively.


### The Big O Cheat Sheet: (Time Complexity) :

**Note**: The Big O Cheat Sheet is a summary of the most common time complexities of algorithms. It is not a complete list of all the time complexities of all the algorithms.

<center>

| Big O | Name | Example |
| --- | --- | --- |
| O(1) | Constant | Accessing an element in an array |
| O(log n) | Logarithmic | Binary Search |
| O(n) | Linear | Simple Search |
| O(n log n) | Log Linear | Merge Sort |
| O(n^2) | Quadratic | Bubble Sort |
| O(2^n) | Exponential | Fibonacci Sequence |
| O(n!) | Factorial | Permutation |
</center>

### Big O of Common Data Structures: (Access, Search, Insertion, Deletion) :

<center>

| Data Structure | Access | Search | Insertion | Deletion |
| --- | --- | --- | --- | --- |
| Array | O(1) | O(n) | O(n) | O(n) |
| Linked List | O(n) | O(n) | O(1) | O(1) |
| Stack | O(n) | O(n) | O(1) | O(1) |
| Queue | O(n) | O(n) | O(1) | O(1) |
| Hash Table | O(1) | O(1) | O(1) | O(1) |
| Binary Search Tree | O(log n) | O(log n) | O(log n) | O(log n) |

</center>


## Advanced Cheat Sheet

### Calculating Time Complexity:

**Note**: The following are the steps to calculate the time complexity of an algorithm.

1) **Dropping the Constants:** Drop the constants in the time complexity. For example, O(2n) is the same as O(n).

2) **Dropping the Non Dominants:** Drop the non dominants in the time complexity. For example, O(n + n^2) is the same as O(n^2).

3) **Dropping the Less Significant Terms:** Drop the less significant terms in the time complexity. For example, O(n^2 + n) is the same as O(n^2).

For example, the time complexity of the following algorithm is O(n^2):

```C
// C Code
int sum = 0; // O(1)
for (int i = 0; i < n; i++) { // O(n)
    for (int j = 0; j < n; j++) { // O(n)
        sum += 1; // O(1)
    }
}
```

```Python
# Python Code
sum = 0 # O(1)
for i in range(n): # O(n)
    for j in range(n): # O(n)
        sum += 1 # O(1)
```

```Java
// Java Code
int sum = 0; // O(1)
for (int i = 0; i < n; i++) { // O(n)
    for (int j = 0; j < n; j++) { // O(n)
        sum += 1; // O(1)
    }
}
```

**Calculating Time Complexity:** O(1) + O(n) + O(n) + O(1) = O(2n) = O(n)


## Conclusion

In this article, we have learned about the Big O Notation and how to calculate the time complexity of an algorithm. We have also learned about the Big O Cheat Sheet and the Big O of common data structures.
