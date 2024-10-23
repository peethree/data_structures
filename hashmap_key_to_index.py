class HashMap:
    def key_to_index(self, key):
        sum = 0
        
        for char in key:
            sum += ord(char)

        index = sum % len(self.hashmap)        
        return index 

    def __init__(self, size):
        self.hashmap = [None for i in range(size)]

    def __repr__(self):
        buckets = []
        for v in self.hashmap:
            if v != None:
                buckets.append(v)
        return str(buckets)
