import queue

# Create a stack
stack = queue.LifoQueue()

# Push elements onto the stack
stack.put(2)
stack.put(3)
stack.put(7)
stack.put(4)
stack.put(1)
stack.put(9)
stack.put(8)

# Print the number of elements in the stack
print('Number of stack elements:', stack.qsize())

# Sum the last two numbers and print the result
if stack.qsize() >= 2:
    last_two_sum = stack.get() + stack.get()
    print('Sum of the last two numbers:', last_two_sum)

# Sum the remaining elements in the stack using a while loop
remaining_sum = 0
while not stack.empty():
    remaining_sum += stack.get()

print('Sum of the remaining stack elements:', remaining_sum)
