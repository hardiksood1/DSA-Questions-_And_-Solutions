# Implement a queue using two stacks.

class QueueUsingStacks:
    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def enqueue(self, x):
        # Push element onto the input stack
        self.stack_in.append(x)

    def dequeue(self):
        # If output stack is empty, move all items from input stack
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        
        if not self.stack_out:
            print("Queue is empty!")
            return None
        return self.stack_out.pop()

    def peek(self):
        # Ensure elements are in output stack to get the front
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        
        if not self.stack_out:
            print("Queue is empty!")
            return None
        return self.stack_out[-1]

    def is_empty(self):
        return not (self.stack_in or self.stack_out)

# Example usage
if __name__ == "__main__":
    q = QueueUsingStacks()
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)

    print("Front element:", q.peek())   # Output: 10
    print("Dequeued:", q.dequeue())     # Output: 10
    print("Dequeued:", q.dequeue())     # Output: 20
    print("Is empty:", q.is_empty())    # Output: False


# output
# Front element: 10
# Dequeued: 10
# Dequeued: 20
# Is empty: False