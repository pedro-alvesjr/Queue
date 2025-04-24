class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def print_queue(self):
        temp = self.first
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def enqueue(self, value):
        new_node = Node(value)
        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1

    def dequeue(self):
        if self.first is None:
            return None
        temp = self.first
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
            temp.next = None
        self.length -= 1
        return temp

# Testing the Queue class and its methods
my_queue = Queue(1)

# Test 1: Print the initial queue (with one item)
print("Initial queue:")
my_queue.print_queue()

# Test 2: Enqueue values into the queue
print("\nEnqueuing values 2, 3, 4, 5, 6 into the queue...")
my_queue.enqueue(2)
my_queue.enqueue(3)
my_queue.enqueue(4)
my_queue.enqueue(5)
my_queue.enqueue(6)

# Test 3: Print the queue after enqueuing values
print("\nQueue after enqueuing 5 values:")
my_queue.print_queue()

# Test 4: Dequeue one value from the queue
print("\nDequeuing one value from the queue...")
dequeued_node = my_queue.dequeue()
if dequeued_node:
    print(f"Dequeued value: {dequeued_node.value}")
else:
    print("Queue is empty, nothing to dequeue.")

# Test 5: Print the queue after dequeuing one value
print("\nQueue after dequeuing one value:")
my_queue.print_queue()

# Test 6: Dequeue all elements and check behavior
print("\nDequeuing all elements from the queue...")
while my_queue.length > 0:
    dequeued_node = my_queue.dequeue()
    print(f"Dequeued value: {dequeued_node.value}")

# Test 7: Attempt to dequeue from an empty queue
print("\nAttempting to dequeue from an empty queue...")
dequeued_node = my_queue.dequeue()
if dequeued_node:
    print(f"Dequeued value: {dequeued_node.value}")
else:
    print("Queue is empty, nothing to dequeue.")

# Test 8: Print the queue when it's empty
print("\nQueue after dequeuing all values:")
my_queue.print_queue()