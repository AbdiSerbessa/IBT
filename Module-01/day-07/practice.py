
#Exercise 1.

# 1. List Indexing
# Big-O: O(1) - Constant Time
# Explanation: Python lists are implemented as contiguous memory arrays. 
# Accessing an element by index calculates the memory address directly using math (base_address + index * element_size),
# taking the exact same amount of time regardless of how long the list is.
element = my_list[4]


# 2. Single Loop
# Big-O: O(n) - Linear Time
# Explanation: The loop executes its body once for each item in the list of length 'n'. 
# If the size of the list doubles, the number of operations doubles proportionally.
for item in my_list:
    print(item)


# 3. Nested Loop
# Big-O: O(n^2) - Quadratic Time
# Explanation: For every single iteration of the outer loop (n iterations), the inner loop runs completely (n iterations). 
# This results in n * n = n^2 total executions.
for i in range(len(my_list)):
    for j in range(len(my_list)):
        print(my_list[i], my_list[j])


# 4. Dictionary Lookup
# Big-O: O(1) - Average Constant Time
# Explanation: Python dictionaries use a hash table under the hood. 
# The key is passed through a hash function to find its bucket location directly, 
# allowing instantaneous retrieval regardless of how many key-value pairs exist in the dictionary.
value = my_dict["key"]


# 5. Binary Search
# Big-O: O(log n) - Logarithmic Time
# Explanation: With every step, binary search compares the target to the middle element 
# and cuts the remaining search area in half. Doubling the input size adds only one additional step.
low, high = 0, len(sorted_list) - 1
while low <= high:
    mid = (low + high) // 2
    if sorted_list[mid] == target:
        break
    elif sorted_list[mid] < target:
        low = mid + 1
    else:
        high = mid - 1



        ##Exercise 2

        import time

NUM_ITEMS = 100_000

account_list = [f"ACC_{i}" for i in range(NUM_ITEMS)]

account_dict = {f"ACC_{i}": i for i in range(NUM_ITEMS)}

target_account = "ACC_99998"


start_time = time.perf_counter()
found_in_list = target_account in account_list
end_time = time.perf_counter()

list_lookup_time = end_time - start_time
print(f"List Lookup Time: {list_lookup_time:.8f} seconds")


start_time = time.perf_counter()
found_in_dict = target_account in account_dict
end_time = time.perf_counter()

dict_lookup_time = end_time - start_time
print(f"Dict Lookup Time: {dict_lookup_time:.8f} seconds")

if dict_lookup_time > 0:
    speedup = list_lookup_time / dict_lookup_time
    print(f"\nResult: Dictionary lookup was approx {speedup:.1f}x faster!")



    ##Exercie 3

    class Stack:
    """A standard LIFO (Last-In, First-Out) Stack implementation."""
    def __init__(self):
        self._items = []

    def push(self, item):
        """Add an item to the top of the stack."""
        self._items.append(item)

    def pop(self):
        """Remove and return the top item from the stack."""
        if self.is_empty():
            raise IndexError("pop from an empty stack")
        return self._items.pop()

    def peek(self):
        """Return the top item without removing it."""
        if self.is_empty():
            raise IndexError("peek from an empty stack")
        return self._items[-1]

    def is_empty(self):
        """Check if the stack is empty."""
        return len(self._items) == 0

    def __len__(self):
        """Return the number of items in the stack."""
        return len(self._items)


def reverse_names(names_list):
    """Reverses a list of names using a Stack."""
    stack = Stack()

   
    for name in names_list:
        stack.push(name)

    reversed_list = []

    # Step 2: Pop all names off the stack until it's empty
    while not stack.is_empty():
        reversed_list.append(stack.pop())

    return reversed_list



original_names = ["Alice", "Bob", "Charlie", "Diana", "Ethan"]

print("Original list:", original_names)

reversed_names = reverse_names(original_names)

print("Reversed list:", reversed_names)




##Exercises 4

from collections import deque

bank_line = deque()


print("--- Customers Joining the Line ---")
customers = ["Alice", "Bob", "Charlie", "Diana", "Ethan"]

for customer in customers:
    bank_line.append(customer)  
    print(f"-> {customer} joined the line.")

print(f"\nCurrent line: {list(bank_line)}\n")


print("--- Serving Customers ---")
while bank_line:
   
    current_customer = bank_line.popleft()
    print(f"<- Serving: {current_customer}")

print("\nAll customers have been served! The line is empty.")






##Exercise 5


class Node:
    """Represents a single node in the linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None  


class LinkedList:
    """Represents the singly linked list structure."""
    def __init__(self):
        self.head = None 

    def push_front(self, data):
        """Inserts a new node containing 'data' at the beginning of the list."""
        new_node = Node(data)
        new_node.next = self.head  
        self.head = new_node      

    def print_all(self):
        """Traverses (walks) the chain and prints all elements."""
        current = self.head
        
        if current is None:
            print("List is empty.")
            return

        elements = []
        while current is not None:
            elements.append(str(current.data))
            current = current.next  # Advance pointer to the next node

        print(" -> ".join(elements) + " -> None")



llist = LinkedList()

llist.push_front("Node 3")
llist.push_front("Node 2")
llist.push_front("Node 1")

llist.print_all()

