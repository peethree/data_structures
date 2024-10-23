def matchmake(queue, player):
    # queue instance

    # player: ("Bob", "join")

    # If the action is "leave", 
    # search the queue for the player and 
    # remove them if they are in the queue.
    if player[1] == "leave":
        queue.search_and_remove(player[0])

    if player[1] == "join":
        queue.push(player[0])

    if queue.size() >= 4:
        player1 = queue.pop()
        player2 = queue.pop()
        return f"{player1} matched {player2}!"
        
    return "No match found"


# don't touch below this line
class Queue:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.insert(0, item)

    def pop(self):
        if len(self.items) == 0:
            return None
        temp = self.items[-1]
        del self.items[-1]
        return temp

    def peek(self):
        if len(self.items) == 0:
            return None
        return self.items[-1]

    def size(self):
        return len(self.items)

    def search_and_remove(self, item):
        if item not in self.items:
            return None
        self.items.remove(item)
        return item

    def __repr__(self):
        return f"[{', '.join(self.items)}]"
