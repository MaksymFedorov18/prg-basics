import queue

expression1 = "[(2+3)*4+5]/6-{(7*8)+[4]}"  # brackets ok
expression2 = "[(2+3]/4)"                 # brackets not correct
expression3 = "(2-3*4+(5/6)"              # brackets not correct

def brackets_ok(expression):
    stack = queue.LifoQueue()

    matching_bracket = {')': '(', ']': '[', '}': '{'}

    # Loop through each character in the expression
    for char in expression:
        if char in "([{":
            stack.put(char)
        elif char in ")]}":
            if stack.empty():
                return False
            top = stack.get()
            if top != matching_bracket[char]:
                return False

    # After processing, the stack should be empty if all brackets were properly closed
    return stack.empty()

if brackets_ok(expression1):
    print(f"Expression 1: '{expression1}' has balanced brackets.")
else:
    print(f"Expression 1: '{expression1}' has unbalanced brackets.")

if brackets_ok(expression2):
    print(f"Expression 2: '{expression2}' has balanced brackets.")
else:
    print(f"Expression 2: '{expression2}' has unbalanced brackets.")

if brackets_ok(expression3):
    print(f"Expression 3: '{expression3}' has balanced brackets.")
else:
    print(f"Expression 3: '{expression3}' has unbalanced brackets.")
