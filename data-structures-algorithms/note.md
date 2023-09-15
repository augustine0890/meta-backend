# The Big O Notation
- Operation with constant complexity:
    - Simple variable assignments
    - Arithmetic operations and comparisons
    - Reference to a specific memory location (accessing elements in a list by index or in a dictionary by key)
- O(n) complexity indicates that the effort to run an algorithm grows proportionally to the amount of items being processed.
- O(n2) (quadratic) is running in quadratic time would do n2 number of operations.
- Auxiliary space complexity: The memory an algorithm needs to run, without counting the memory needed to store the input
- Finding the complexity of an algorithm:
    - Ignore non-dominant terms
    - Ignore constants
    - Simple variable assignments, arithmetic operations and comparisons are usually constant time operations
    - Simple loops over the input are running in linear time
    - Nested loops over the input are running in quadratic time
    - Logarithmic time happens when we disregard large parts of the input with each loop

# Recursion
- A stack is a linear data structure, with only one access point (LIFO)
- Stack Frame (Execution Frame, Activation Record):
    - local variable and arguments
    - link to previous frame
    - last instruction reference
    - return value
- In most languages iteration is faster recursion requires call-stack management
- Recursion can use more memory because of all the stack frames
- Some languages optimize recursive calls
- Recursion usually has the advantage in code simplicity
- Manual management of a stack in iteration can be error-prone
- What to consider in determining the complexity of recursive functions:
    - the number of stack frames
    - the number of recursive calls
    - the other operations done inside the function
    - the space complexity (the max number of stack frames)

# Hash Maps - Tables (Dictionaries)
- Needs to be fast
- Needs to always give the same result (given the same input)
- Needs to distribute keys uniformly
- The require more memory for storing keys and values