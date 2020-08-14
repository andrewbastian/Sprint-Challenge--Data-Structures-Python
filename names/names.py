import time
from bst import BSTNode


# Task 2. Runtime Optimization

"""
Navigate into the `names` directory. Here you will find two text files
containing 10,000 names each, along with a program `names.py` that compares
the two files and prints out duplicate name entries. Try running the code with
`python3 names.py`. Be patient because it might take a while: approximately
six seconds on my laptop. What is the runtime complexity of this code?

Six seconds is an eternity so you've been tasked with speeding up the code.
Your goal is to use one of the data structures we built out over the course of
this week in order to optimize and improve on the runtime so that it's more
efficient than O(n²).

A follow-up question to think about: _*once you've used one of the data
structures we implemented over the course of the week*_ in order to improve
the runtime of the implementation, what other data structures (including ones
from Python's standard library) are also possible candidates for improving the
runtime of the implementation?
"""


start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
"""for name_1 in names_1:
    for name_2 in names_2:
        if name_1 == name_2:
            duplicates.append(name_1)
"""
#           ^^^^ o(n)^2 ^^^^

nodes = BSTNode('')

for name in names_1:
    # add names from 1st list to BST
    nodes.insert(name)

for name in names_2:
    # If a name from the BST matches the name from the loop on 2nd list add
    # that name to the duplicates list.
    if nodes.contains(name):
        duplicates.append(name)

"""
o(n)
runtime: 0.12900376319885254 seconds
"""

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools allowing a efficient approach to this problem
# What's the best time you can accomplish?
# Thare are no restrictions on techniques or data structures,
# but you may not import additional libraries you did not write.

print('\nSEE `stretch_names.py` FOR STRETCH GOAL ANSWER\n')
