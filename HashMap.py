class HashMap:
    """Hash map with linear probing."""
    def __init__(self, capacity=11, skip=3):
        self.load = 0
        self.capacity = capacity
        self.skip = skip
        self.list = [None] * capacity

    def resize(self, new_size):
        old_list = self.list
        old_load = self.load
        self.capacity = new_size
        self.list = [None] * new_size
        for kv_pair in old_list:
            if kv_pair is not None:
                key, value = kv_pair
                self.put(key, value)
        self.load = old_load

    def put(self, key, value):
        self.load += 1
        if self.load / self.capacity > 0.5:
            self.resize(self.capacity * 2)
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

    # noinspection PyTupleAssignmentBalance
    # TODO
    def __delitem__(self, key):
        # Easy case and hard case.  Easy: None or hit -- set to None if hit (!). Hard: no hit but not None.
        # Then you have to rehash everything in a potential cluster.
        # This duplicates some of the get() logic above
        # -- but that method doesn't distinguish between initial hit and later hit.
        # (!) not quite -- if you set a hash at the start of a chain to None, gets
        # for everything in the chain will fail from then on. Everything in the chain if it exists always has to be
        # moved "down".  This is just like removing a node from a linked list, considered under a certain light.
        hashed_key = self.make_hash(key)
        entry = self.list[hashed_key]
        if entry is None:
            return
        next_key, _ = entry
        rehashed_key = self.rehash(hashed_key)
        # move down the chain until we get a hit or None; if the former, start adjustment; if the latter, escape
        while next_key != key:
            entry = self.list[rehashed_key]
            next_key, _ = entry
            rehashed_key = self.rehash(rehashed_key)
        self.load -= 1

    def __getitem__(self, item):
        return self.get(item)

    def __setitem__(self, key, value):
        return self.put(key, value)

    def __len__(self):
        return self.load

    def __str__(self):
        rep = 'Hashmap has {}/{} items:\n'.format(self.load, self.capacity)
        for item in self.list:
            if item is None:
                continue
            rep += "{}: {}\n".format(item[0], item[1])
        return rep


if __name__ == "__main__":
    h = HashMap()
    for (index, letter) in enumerate("abcdefghijklmnopqrstuvwxyz"):
        h[letter] = index
    print(h)
    del h['a']
    print(h)
