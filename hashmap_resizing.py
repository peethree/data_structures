class HashMap:
    def insert(self, key, value):
        # Call resize() before inserting to make sure there's enough space. 
        # Then, insert the key-value pair into the hashmap as normal.
        self.resize()
        
        index = self.key_to_index(key)
        self.hashmap[index] = (key, value)

    def resize(self):
        # If the length of the underlying hashmap is 0, 
        # make the length 1 (by just adding a None entry).
        if len(self.hashmap) == 0:
            self.hashmap.append(None)

        """
        Get the current load. If it's less than 5%, do nothing, 
        we have plenty of space.
        Otherwise, create a new empty hashmap that's 10x the size of the current one, 
        then use the insert method to re-insert all the key-value pairs 
        from the old hashmap into the new one.
        """
        load = self.current_load()
        
        if load >= 0.05:
            current_size = len(self.hashmap)
            size_times_ten = 10 * current_size
            new_hashmap = HashMap(size_times_ten)

            for bucket in self.hashmap:
                if bucket is not None:
                    new_hashmap.insert(bucket[0], bucket[1])
                

            self.hashmap = new_hashmap.hashmap
 
    def current_load(self):
        # This method returns the number of filled buckets in the hashmap 
        # as a percentage of the total number of buckets.
        total_size = len(self.hashmap)

        if total_size == 0:
            return 1
        # If the length of the underlying list is zero, return 1. 
        # Otherwise, divide the number of filled buckets by the length of the underlying list and return it.
        count = 0
        for item in self.hashmap:
            if item is not None:
                count += 1

        load = count / total_size
        return load               
    

    def __init__(self, size):
        self.hashmap = [None for i in range(size)]

    def key_to_index(self, key):
        sum = 0
        for c in key:
            sum += ord(c)
        return sum % len(self.hashmap)

    def __repr__(self):
        final = ""
        for i, v in enumerate(self.hashmap):
            if v != None:
                final += f" - {str(v)}\n"
        return final
