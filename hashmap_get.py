class HashMap:
    def get(self, key):
        # It takes a key (a string)
        index = self.key_to_index(key)
        
        try:
            # returns the value stored at that location 
            # (not the whole key/value tuple).
            return self.hashmap[index][1]
        except:
            # no key was found
            raise Exception("sorry, key not found")
            

    def __init__(self, size):
        self.hashmap = [None for i in range(size)]

    def key_to_index(self, key):
        sum = 0
        for c in key:
            sum += ord(c)
        return sum % len(self.hashmap)

    def insert(self, key, value):
        i = self.key_to_index(key)
        self.hashmap[i] = (key, value)

    def __repr__(self):
        final = ""
        for i, v in enumerate(self.hashmap):
            if v != None:
                final += f" - {str(v)}\n"
        return final
