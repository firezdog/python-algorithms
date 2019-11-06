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
        self.load += 1
        if self.load / self.capacity > 0.5:
            self.resize(self.capacity * 2)
        key_hash = self.make_hash(key)
        result_key, _ = self.list[key_hash]
        while result_key is not None:
            if result_key == key:
                self.load -= 1
                break
            key_hash = self.rehash(key_hash)
            result_key, _ = self.list[key_hash]
        self.list[key_hash] = (key, value)

    def get(self, key):
        key_hash = self.make_hash(key)
        result_key, result_value = self.list[key_hash]
        while result_key is not None:
            if result_key == key:
                return result_value
            else:
                key_hash = self.rehash(key_hash)
                result = self.list[key_hash]

    def rehash(self, old_hash):
        return (old_hash + self.skip) % self.capacity

    def make_hash(self, key):
        return hash(key) & 0x7fffffff % self.capacity

    # TODO -- this doesn't actually work right now.
    def __delitem__(self, key):
        hashed_key = self.make_hash(key)
        rehashed_key = self.rehash(hashed_key)
        next_key, _ = self.list[hashed_key]
        while next_key != key:
            if next_key is None:
                return
            rehashed_key = self.rehash(rehashed_key)
            next_key, _ = self.list[rehashed_key]
        # now we replace each kv pair with the next kv pair in the cluster
        # OOPS -- this doesn't work because we don't get to loop back around the array.
        # This is more like deleting a link from a linked list WITH A CYCLE
        while next_key is not None:
            current_hash = rehashed_key
            rehashed_key = self.rehash(rehashed_key)
            next_key, next_value = self.list[rehashed_key]
            self.list[current_hash] = (next_key, next_value)
        self.load -= 1

    def __getitem__(self, item):
        return self.get(item)

    def __setitem__(self, key, value):
        return self.put(key, value)

    def __len__(self):
        return self.load

    def __str__(self):
        rep = 'Hashmap has {}/{} items:\n'.format(self.load, self.capacity)
        for key, value in self.list:
            if key is None:
                continue
            rep += "{}: {}\n".format(key, value)
        return rep


if __name__ == "__main__":
    h = HashMap()
    for (index, letter) in enumerate("ab"):
        h[letter] = index
    print(h)
    del h['a']
    print(h)
