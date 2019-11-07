class HashMap:
    """Hash map with linear probing."""
    def __init__(self, capacity=11, skip=3):
        self.load = 0
        self.capacity = capacity
        self.skip = skip
        self.list = [(None, None)] * capacity

    def resize(self, new_size):
        old_list = self.list
        old_load = self.load
        self.capacity = new_size
        self.list = [(None, None)] * new_size
        for kv_pair in old_list:
            key, value = kv_pair
            if key is not None:
                self.put(key, value)
        self.load = old_load

    def put(self, key, value):
        if key is None or value is None:
            raise ValueError("Key / value cannot be None.")
        self.load += 1
        if self.load / self.capacity > 0.5:
            self.resize(self.capacity * 2)
        key_hash = self.make_hash(key)
        result_key, _ = self.list[key_hash]
        while result_key is not None:
            if result_key == key:
                self.list[key_hash] = (key, value)
                self.load -= 1
                break
            key_hash = self.rehash(key_hash)
            result_key, _ = self.list[key_hash]
        self.list[key_hash] = (key, value)

    def get(self, key):
        if key is None:
            raise ValueError("Invalid search value: None.")
        key_hash = self.make_hash(key)
        result_key, result_value = self.list[key_hash]
        while result_key is not None:
            if result_key == key:
                break
            else:
                key_hash = self.rehash(key_hash)
                result_key, result_value = self.list[key_hash]
        return result_value

    def rehash(self, old_hash):
        return (old_hash + self.skip) % self.capacity

    def make_hash(self, key):
        return hash(key) & 0x7fffffff % self.capacity

    '''should be very simple: go through all the entries in the cluster -- take out and put each one back in
    except the delendum'''
    def __delitem__(self, key):
        rehash = self.make_hash(key)
        next_key, next_value = self.list[rehash]
        while next_key is not None:
            self.load -= 1  # canceled out if it gets put back in
            self.list[rehash] = (None, None)
            if next_key != key:
                self.put(next_key, next_value)
            rehash = self.rehash(rehash)
            next_key, next_value = self.list[rehash]
        if (self.load / self.capacity) < (1/8):
            self.resize(int(self.capacity / 2))

    def __getitem__(self, item):
        return self.get(item)

    def __setitem__(self, key, value):
        return self.put(key, value)

    def __len__(self):
        return self.load

    def defines(self, item):
        return self.get(item) is not None

    def __str__(self):
        rep = 'Hashmap has {}/{} items:\n'.format(self.load, self.capacity)
        for key, value in self.list:
            if key is None:
                continue
            rep += "{}: {}\n".format(key, value)
        return rep


if __name__ == "__main__":
    h = HashMap()
    for (index, letter) in enumerate("abcdefghijklmnopqrstuvwxyzzzzzzzzzz"):
        h[letter] = index
    print(h)
    for (index, letter) in enumerate("abcdefghijklmnopqrstuvwxyz"):
        del h[letter]
    print(h)
    for (index, letter) in enumerate("abcdefghijklmnopqrstuvwxyz"):
        h[letter] = index
    print(h)
