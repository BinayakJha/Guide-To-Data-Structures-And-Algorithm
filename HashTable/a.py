class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def get(self, key):
        """
        If the bucket is not empty, then loop through the bucket and return the value if the key matches
        
        :param key: The key to be searched for
        :return: The value of the key
        """
        index = self.hash(key)
        bucket = self.table[index]
        if len(bucket) > 0:
            for i in range(len(bucket)):
                k = bucket[i]["key"]

                if k == key:
                    return bucket[i]["value"]
            return None
        return None

    def insert(self, key, value):
        """
        If the key already exists, update the value, otherwise append the new key/value pair to the
        bucket
        
        :param key: The key to be inserted
        :param value: The value to be inserted into the hash table
        """
        index = self.hash(key)
        current_value = self.get(key)
        if current_value != None:
            bucket = self.table[index]

            for i in range(len(bucket)):
                if bucket[i]["key"] == key:
                    bucket[i]["value"] = value
        else:
            self.table[index].append({ "key": key, "value": value })


    def remove(self, key):
        """
        It removes the key from the hash table.
        
        :param key: The key to be inserted
        :return: The value of the key that is being removed.
        """
        value = self.get(key)
        self.insert(key, None)
        return value


    def hash(self, key):
        """
        The hash function takes a key, converts it to a string, and then loops through each character in
        the string, adding the ASCII value of each character to a running total. The function then
        returns the total modulo the size of the hash table
        
        ']
        :param key: The key to be hashed
        :return: The hash value of the key.
        """
        hash = 0
        key = str(key)
        for i in range(len(key)):
            hash = (hash + ord(key[i])) % self.size
        return hash


a = HashTable(100)
a.insert("hello", 6)
print(a.get("hello"))
print(a.hash("hello0"))
