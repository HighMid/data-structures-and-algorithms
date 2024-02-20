class Hashtable:
    def __init__(self, size=100):
        self.size = size
        self.table = [None] * size

    def hash(self, key):
        """Simple hash function."""
        return hash(key) % self.size

    def set(self, key, value):
        """Set key-value pair, handling collisions with chaining."""
        index = self.hash(key)
        if self.table[index] is None:
            self.table[index] = []
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                return
        self.table[index].append((key, value))

    def get(self, key):
        """Get value by key."""
        index = self.hash(key)
        if self.table[index] is not None:
            for k, v in self.table[index]:
                if k == key:
                    return v
        return None

    def has(self, key):
        """Check if key exists."""
        index = self.hash(key)
        if self.table[index] is not None:
            for k, _ in self.table[index]:
                if k == key:
                    return True
        return False

    def keys(self):
        """Return all keys."""
        keys_list = []
        for item in self.table:
            if item is not None:
                for k, _ in item:
                    keys_list.append(k)
        return keys_list
    
    