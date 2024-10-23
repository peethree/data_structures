class Trie:
    def words_with_prefix(self, prefix):
        
        words = []                  
        current = self.root       
        
        # traverse trie to last char of prefix
        for char in prefix:            
            if char in current:   
               
                current = current[char]                 
            # if prefix not in trie
            else:
                return []                
        # at last character of prefix, call search_level(current_level, current_prefix, words)
        return self.search_level(current, prefix, words)
        
        
    def search_level(self, cur, cur_prefix, words):
        if self.end_symbol in cur:
            words.append(cur_prefix)

        keys = cur.keys()

        for key in sorted(keys):
            if key != self.end_symbol:    
                # cur[key] will give you the next level in the trie.
                # cur_prefix remains the same for each key in the current node 
                # and is only modified within the context of the recursive call.
                self.search_level(cur[key], cur_prefix + key, words)
        return words
                
 

    def __init__(self):
        self.root = {}
        self.end_symbol = "*"

    def add(self, word):
        current = self.root
        for letter in word:
            if letter not in current:
                current[letter] = {}
            current = current[letter]
        current[self.end_symbol] = True
