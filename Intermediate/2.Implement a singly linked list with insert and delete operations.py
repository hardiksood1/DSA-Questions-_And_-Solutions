# 2.Implement a singly linked list with insert and delete operations.

# Node class to represent each element in the list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Singly Linked List class
class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # Insert a new node at the end
    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    # Delete a node by value
    def delete(self, key):
        current = self.head

        # Case 1: Empty list
        if not current:
            print("List is empty.")
            return

        # Case 2: The node to be deleted is the head
        if current and current.data == key:
            self.head = current.next
            current = None
            return

        # Case 3: The node to delete is in the middle or end
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next

        # If key was not found
        if not current:
            print(f"Value {key} not found in list.")
            return

        # Unlink the node
        prev.next = current.next
        current = None

    # Display the linked list
    def display(self):
        current = self.head
        if not current:
            print("List is empty.")
            return
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# Example usage
if __name__ == "__main__":
    ll = SinglyLinkedList()
    ll.insert(10)
    ll.insert(20)
    ll.insert(30)
    print("Initial list:")
    ll.display()

    print("\nAfter deleting 20:")
    ll.delete(20)
    ll.display()

    print("\nAfter inserting 40:")
    ll.insert(40)
    ll.display()


# Output 

# Initial list:
# 10 -> 20 -> 30 -> None

# After deleting 20:
# 10 -> 30 -> None

# After inserting 40:
# 10 -> 30 -> 40 -> None