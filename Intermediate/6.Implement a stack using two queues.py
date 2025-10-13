#Implement a stack using two queues.

from queue import Queue

class StackUsingQueues:
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def push(self, x):
        # Step 1: Push x to q2
        self.q2.put(x)

        # Step 2: Move all elements from q1 to q2
        while not self.q1.empty():
            self.q2.put(self.q1.get())

        # Step 3: Swap q1 and q2
        self.q1, self.q2 = self.q2, self.q1

    def pop(self):
        if self.q1.empty():
            print("Stack is empty!")
            return None
        return self.q1.get()

    def top(self):
        if self.q1.empty():
            print("Stack is empty!")
            return None
        top_element = self.q1.get()
        self.q2.put(top_element)
        # Move remaining elements to maintain order
        while not self.q1.empty():
            self.q2.put(self.q1.get())
        self.q1, self.q2 = self.q2, self.q1
        return top_element

    def is_empty(self):
        return self.q1.empty()

# Example usage:
if __name__ == "__main__":
    s = StackUsingQueues()
    s.push(10)
    s.push(20)
    s.push(30)

    print("Top element:", s.top())  
    print("Popped:", s.pop())       
    print("Popped:", s.pop())       
    print("Is empty:", s.is_empty()) 

# output

# Top element: 30
# Popped: 30     
# Popped: 20     
# Is empty: False