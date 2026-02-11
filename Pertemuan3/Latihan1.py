class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # This is the function from your image
    def delete_node(self, key):
        temp = self.head

        # 1. Case: The head node itself holds the key to be deleted
        if temp and temp.data == key:
            self.head = temp.next
            temp = None
            return

        # 2. Case: Search for the key to be deleted, keep track of prev node
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        # 3. Case: Key was not present in the linked list
        if temp is None:
            return

        # 4. Unlink the node from the linked list
        prev.next = temp.next
        temp = None

    # Helper function to add nodes at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # Helper function to print the list
    def print_list(self):
        temp = self.head
        while temp:
            print(f"{temp.data} ->", end=" ")
            temp = temp.next
        print("Null")

# --- Example Usage ---
llist = LinkedList()
llist.push(7)
llist.push(1)
llist.push(3)
llist.push(2)

print("Created Linked List:")
llist.print_list()

print("\nDeleting node with value 3:")
llist.delete_node(3)
llist.print_list()