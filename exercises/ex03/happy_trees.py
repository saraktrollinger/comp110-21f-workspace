"""Drawing forests in a loop."""

__author__ = "730393060"

# The string constant for the pine tree emoji
TREE: str = '\U0001F332'

depth: int = int(input("Depth: "))
counter: int = 0
sequence = TREE + " "
final_sequence = TREE

if depth > 0:
    if counter == depth:
        print(sequence * counter + final_sequence)
    while counter < depth:
        print(sequence * counter + TREE)
        counter += 1