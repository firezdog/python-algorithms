class HashMap:
    """Hash map with linear probing."""
    def __init__(self, capacity=11, skip=3):
        self.load = 0
        self.capacity = capacity
        self.skip = skip
        self.list = [None] * capacity

    def put(self, key, value):
        self.load += 1
        key_hash = self.make_hash(key)
        result = self.list[key_hash]
        while result is not None:
            if result[0] is key:
                self.load -= 1
                break
            key_hash = self.rehash(key_hash)
            result = self.list[key_hash]
        self.list[key_hash] = (key, value)

    def get(self, key):
        key_hash = self.make_hash(key)
        result = self.list[key_hash]
        while result is not None:
            if result[0] == key:
                return result[1]
            else:
                key_hash = self.rehash(key_hash)
                result = self.list[key_hash]

    def rehash(self, old_hash):
        return (old_hash + self.skip) % self.capacity

    def make_hash(self, key):
        return hash(key) & 0x7fffffff % self.capacity

    def __getitem__(self, item):
        return self.get(item)

    def __setitem__(self, key, value):
        return self.put(key, value)

    def __len__(self):
        return self.load

    def __str__(self):
        rep = ''
        for item in self.list:
            if item is None:
                continue
            rep += "{}: {}\n".format(item[0], item[1])
        return rep


if __name__ == "__main__":
    h = HashMap()
    h2 = HashMap()
    h[(1, 3)] = 4
    h[h2] = "The key for this entry is a hashmap."
    for (index, letter) in enumerate("hashmap"):
        h[letter] = index
    print("hashmap has {}/{} items".format(len(h), h.capacity))
    print(h)
