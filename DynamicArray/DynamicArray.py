class DynamicArray:
    def __init__(self):
        self.length = 0
        self.data = {}

    def get(self, index):
        # get an item at an index
        return self.data[index]
        pass

    def push(self, item):
        # add an item to the end of the array
        self.data[self.length] = item
        self.length += 1
        return self.length
        pass

    def pop(self):
        # remove the last item in the array
        popped_item = self.data[self.length - 1]
        del self.data[self.length - 1]
        self.length -= 1
        return popped_item
        pass

    def insert(self, index, item):
        # add an item at any index
        self.length += 1
        for i in range(self.length - 1, index, -1):
            self.data[i] = self.data[i - 1]
        self.data[index] = item
        return self.length
        pass

    def remove(self, index):
        # remove an item at any index
        removed_item = self.data[index]
        for i in range(index, self.length - 1):
            self.data[i] = self.data[i + 1]
        del self.data[self.length - 1]
        self.length -= 1
        return removed_item
        pass


array = DynamicArray()
array.push(1)
array.push(2)
array.push(3)
array.push(4)
array.push(5)
array.push(6)
array.push(7)


print(array.data)
print(array.length)
print(array.get(2))
print("Popped item: ", array.pop())
print(array.data)
print(array.length)
print("Inserted item: ", array.insert(2, 10))
print(array.data)
print(array.length)
print("Removed item: ", array.remove(2))
print(array.data)
