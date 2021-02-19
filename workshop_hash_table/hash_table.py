# storage = [None] * 4
# value = 'Tim'
# idx = hash(value) % len(storage)
#
#
# print(storage)


class HashTable:
    _DEFAULT_LENGTH = 4

    def __init__(self, capacity=_DEFAULT_LENGTH):
        self.capacity = capacity
        self.array = [None] * self.capacity
        self.length = 0

    def hash(self, key: str):
        return hash(key) % len(self.array)

    def add(self, key: str, value):
        index = self.hash(key)
        if self.array[index] is None:
            self.array[index] = []

        self.length += 1
        self.array[index].append((key, value))

        filled = self.length / len(self.array)
        if filled > 0.5:
            self.increase_size()

    def get(self, key: str, default=None):
        idx = self.hash(key)
        if self.array[idx] is None:
            return default
        keys_values = self.array[idx]
        for k, value in reversed(keys_values):
            if k == key:
                return value
        return default

    def increase_size(self):
        new_table = HashTable(capacity=self.capacity * 2)
        for chain in self.array:
            if chain is None:
                continue
            for (key, value) in chain:
                new_table.add(key, value)

        self.array = new_table.array
        self.capacity = new_table.capacity


