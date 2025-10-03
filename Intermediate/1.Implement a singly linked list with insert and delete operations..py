# Implement a singly linked list with insert and delete operations.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Singly Linked List class
class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # Insert at the end
    def insert(self, data):
        new_node = Node(data)
        if not self.head:  # Empty list
            self.head = new_node
            return
        current = self.head
        while current.next:  # Traverse till last node
            current = current.next
        current.next = new_node

    # Delete first occurrence of a value
    def delete(self, key):
        current = self.head

        # Case 1: Head node is the one to be deleted
        if current and current.data == key:
            self.head = current.next
            current = None
            return

        # Case 2: Search for the key
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next

        # Key not found
        if not current:
            print(f"Value {key} not found in the list.")
            return

        # Unlink the node
        prev.next = current.next
        current = None

    # Print the linked list
    def display(self):
        current = self.head
        if not current:
            print("List is empty")
            return
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# Example Usage
if __name__ == "__main__":
    sll = SinglyLinkedList()
    sll.insert(10)
    sll.insert(20)
    sll.insert(30)
    print("Initial List:")
    sll.display()

    print("\nDeleting 20:")
    sll.delete(20)
    sll.display()

    print("\nDeleting 50 (not in list):")
    sll.delete(50)
    sll.display()



#Output

# Initial List:
# 10 -> 20 -> 30 -> None

# Deleting 20:
# 10 -> 30 -> None

# Deleting 50 (not in list):
# Value 50 not found in the list.
# 10 -> 30 -> None