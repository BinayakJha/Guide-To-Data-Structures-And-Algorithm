# Hash Table :

## Introduction :

A hash table is a data structure that maps keys to values for highly efficient lookup. In a hash table, the keys are not ordered. The hash table is created by a hash function that determines the location of a key.

The reason hash tables are so important is that they offer constant time <i>O(1)</i> **lookup / set / insert / delete**. They are frequently used with other data structures to improve the performance of our solution.

**Common names:** <i>hash, hash table, hash map, dictionary, associative array, map</i>

## Hash Function :

A hash function is a function that can be used to map data of arbitrary size to data of fixed size. The values returned by a hash function are called hash values, hash codes, digests, or simply hashes. The values are used to index a fixed-size table called a hash table. Use of a hash function to index a hash table is called hashing or scatter storage addressing.

## Working Method of Hash Table :

Hash tables are very similar to arrays. In fact, hash tables are actually implemented on top of arrays.

So when we initialize a hash table, we create an array beneath the hood. Then when we insert a key, we use a hash function to get an index. We then insert the key at that index. When we want to look up a key, we use the hash function to get the index, and then look up the key at that index.

<img src="https://skilled.dev/images/hashtable.gif" width="100%">


## Hash Table Implementation :

### Hash Table Class :

```python
def __init__(self, size):
    self.size = size
    self.keys = [None] * self.size
    self.values = [None] * self.size
```

#### Code Explanation :

* `self.size` : The size of the hash table.
* `self.keys` : The array that will hold the keys.
* `self.values` : The array that will hold the values.


### Hash Function :

```python
def hash_function(self, key):
    return key % self.size
```

#### Code Explanation :

The hash function is a simple modulo function. It takes the key and divides it by the size of the hash table. The result is the index of the array where the key is stored.


### Insert :

```python
def insert(self, key, value):
    index = self.hash_function(key)
    while self.keys[index] is not None:
        if self.keys[index] == key:
            self.values[index] = value
            return
        index = (index + 1) % self.size
    self.keys[index] = key
    self.values[index] = value
```

#### Code Explanation :

* `index = self.hash_function(key)` : Get the index of the array where the key is stored.

* `while self.keys[index] is not None:` : If the index is not empty, we need to find the next empty index.

* `if self.keys[index] == key:` : If the key already exists, we update the value.

* `index = (index + 1) % self.size` : If the key doesn't exist, we find the next empty index.

* `self.keys[index] = key` : We insert the key.

* `self.values[index] = value` : We insert the value.


### Search :

```python
def search(self, key):
    index = self.hash_function(key)
    while self.keys[index] is not None:
        if self.keys[index] == key:
            return self.values[index]
        index = (index + 1) % self.size
    return None
```

#### Code Explanation :

* `index = self.hash_function(key)` : Get the index of the array where the key is stored.

* `while self.keys[index] is not None:` : If the index is not empty, we need to find the next empty index.

* `if self.keys[index] == key:` : If the key already exists, we return the value.

* `index = (index + 1) % self.size` : If the key doesn't exist, we find the next empty index.

* `return None` : If the key doesn't exist, we return None.


### Delete :

```python
def delete(self, key):
    index = self.hash_function(key)
    while self.keys[index] is not None:
        if self.keys[index] == key:
            self.keys[index] = None
            self.values[index] = None
        index = (index + 1) % self.size
```

#### Code Explanation :

* `index = self.hash_function(key)` : Get the index of the array where the key is stored.

* `while self.keys[index] is not None:` : If the index is not empty, we need to find the next empty index.

* `if self.keys[index] == key:` : If the key already exists, we delete the key and the value.

* `index = (index + 1) % self.size` : If the key doesn't exist, we find the next empty index.


## Hash Table Complexity :

| Algorithm | Average | Worst Case |
|:---------:|:-------:|:----------:|
| Space     | O(n)    | O(n)       |
| Search    | O(1)    | O(n)       |
| Insert    | O(1)    | O(n)       |
| Delete    | O(1)    | O(n)       |

## Hash Table Applications :

* **Caches** : <i>Caches are used to store data that is frequently accessed. A cache is a hash table where the keys are the most recently used data. When we want to access data, we first check the cache. If the data is in the cache, we return it. If the data is not in the cache, we fetch it from the database, store it in the cache, and then return it.</i>

* **Databases** : <i> Databases are used to store data. A database is a hash table where the keys are the data. When we want to access data, we first check the database. If the data is in the database, we return it. If the data is not in the database, we fetch it from the database, store it in the database, and then return it.</i>

* **Sets** : <i> Sets are used to store unique data. A set is a hash table where the keys are the data. When we want to access data, we first check the set. If the data is in the set, we return it. If the data is not in the set, we add it to the set, and then return it.</i>

* **Dictionaries** : <i> Dictionaries are used to store key-value pairs. A dictionary is a hash table where the keys are the keys. When we want to access data, we first check the dictionary. If the key is in the dictionary, we return the value. If the key is not in the dictionary, we add it to the dictionary, and then return None.</i>

* **Hashing** : <i> Hashing is used to store data in a hash table. A hash table is a hash table where the keys are the data. When we want to access data, we first check the hash table. If the data is in the hash table, we return it. If the data is not in the hash table, we add it to the hash table, and then return None.</i>

* **Sorting** : Sorting is used to sort data. A sorting algorithm is a hash table where the keys are the data. When we want to access data, we first check the sorting algorithm. If the data is in the sorting algorithm, we return it. If the data is not in the sorting algorithm, we add it to the sorting algorithm, and then return None.


Hash Table Implementation on other languages :

## C Language

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define SIZE 10

struct hash {
    int key;
    int value;
    struct hash *next;
};

struct hash *hash_table[SIZE];

int hash_function(int key) {
    return key % SIZE;
}

void insert(int key, int value) {
    int index = hash_function(key);
    struct hash *new_hash = malloc(sizeof(struct hash));
    new_hash->key = key;
    new_hash->value = value;
    new_hash->next = NULL;
    if (hash_table[index] == NULL) {
        hash_table[index] = new_hash;
    } else {
        struct hash *current_hash = hash_table[index];
        while (current_hash->next != NULL) {
            current_hash = current_hash->next;
        }
        current_hash->next = new_hash;
    }
}

int search(int key) {
    int index = hash_function(key);
    struct hash *current_hash = hash_table[index];
    while (current_hash != NULL) {
        if (current_hash->key == key) {
            return current_hash->value;
        }
        current_hash = current_hash->next;
    }
    return -1;
}

void delete(int key) {
    int index = hash_function(key);
    struct hash *current_hash = hash_table[index];
    struct hash *previous_hash = NULL;
    while (current_hash != NULL) {
        if (current_hash->key == key) {
            if (previous_hash == NULL) {
                hash_table[index] = current_hash->next;
            } else {
                previous_hash->next = current_hash->next;
            }
            free(current_hash);
            return;
        }
        previous_hash = current_hash;
        current_hash = current_hash->next;
    }
}

int main() {
    insert(1, 10); // 10
    insert(2, 20); // 10 20
    search(1); // 10
    delete(1); // 10
}

```
## JAVA
```java
import java.util.ArrayList;
import java.util.List;

public class HashTable {
    private List<List<Integer>> hashTable;

    public HashTable() {
        hashTable = new ArrayList<>();
        for (int i = 0; i < 10; i++) {
            hashTable.add(new ArrayList<>());
        }
    }

    public void insert(int key, int value) {
        int index = hashFunction(key);
        hashTable.get(index).add(value);
    }

    public int search(int key) {
        int index = hashFunction(key);
        List<Integer> list = hashTable.get(index);
        for (int i = 0; i < list.size(); i++) {
            if (list.get(i) == key) {
                return list.get(i);
            }
        }
        return -1;
    }

    public void delete(int key) {
        int index = hashFunction(key);
        List<Integer> list = hashTable.get(index);
        for (int i = 0; i < list.size(); i++) {
            if (list.get(i) == key) {
                list.remove(i);
                return;
            }
        }
    }

    private int hashFunction(int key) {
        return key % 10;
    }
}

```

## Python
```python

def hash_function(key):
    return key % 10

class HashTable:
    def __init__(self):
        self.hash_table = [[] for _ in range(10)]

    def insert(self, key, value):
        index = hash_function(key)
        self.hash_table[index].append(value)

    def search(self, key):
        index = hash_function(key)
        for value in self.hash_table[index]:
            if value == key:
                return value
        return -1

    def delete(self, key):
        index = hash_function(key)
        for i, value in enumerate(self.hash_table[index]):
            if value == key:
                del self.hash_table[index][i]
                return

a = HashTable()
a.insert(1, 10)
a.insert(2, 20)
a.search(1)
a.delete(1)
```

## C++
```cpp

#include <iostream>
#include <list>
#include <vector>

using namespace std;

class HashTable {
    vector<list<int>> hash_table;

    int hash_function(int key) {
        return key % 10;
    }

public: 
    HashTable() {
        hash_table.resize(10);
    }

    void insert(int key, int value) {
        int index = hash_function(key);
        hash_table[index].push_back(value);
    }

    int search(int key) {
        int index = hash_function(key);
        for (auto value : hash_table[index]) {
            if (value == key) {
                return value;
            }
        }
        return -1;
    }

    void delete_key(int key) {
        int index = hash_function(key);
        for (auto it = hash_table[index].begin(); it != hash_table[index].end(); it++) {
            if (*it == key) {
                hash_table[index].erase(it);
                return;
            }
        }
    }
};

int main() {
    HashTable hash_table;
    hash_table.insert(1, 10);
    hash_table.insert(2, 20);
    hash_table.search(1);
    hash_table.delete_key(1);
}

```

