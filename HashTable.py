
class HashTable:
    def __init__(self):
        # array size 40
        self.size = 40
        # list in each cell of array
        self.map = [None] * self.size

        # hash function. Package ID is key. hash is key mod the size of the array
    def _get_hash(self, key):
        # return the index
        return key % self.size

    def add(self, key, value):
        key_hash = self._get_hash(key)
        # key value pair
        key_value = [key, value]

        # if cell is empty, add key value pair ELSE update if key is already there / add if not
        if self.map[key_hash] is None:
                self.map[key_hash] = list([key_value])
        else:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            self.map[key_hash].append(key_value)
            return True

    def get(self, key):
        key_hash = self._get_hash(key)
        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None

    def delete(self, key):
        key_hash = self._get_hash(key)
        if self.map[key_hash] is None:
            return False

        for i in range (0,len(self.map[key_hash])):
            if self.map[key_hash][i][0] == key:
                self.map[key_hash].pop(i)
                return True

    def _print(self):
        print('-----PACKAGES-----')
        for item in self.map:
            if item is not None:
                print(str(item))





