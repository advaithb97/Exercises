# A LinkedList is either:
# None
# Node

class Node:
    # first: int
    # rest: LinkedList
    def __init__(self, first, rest = None):
        self.first = first
        self.rest = rest

# Write a function named count_evens that consumes a LinkedList ll and returns how many even numbers are in the list
# count_evens(Node(1, Node(2, Node(3, None)))) -> 1
def count_evens(ll):
    if not ll: return 0
    val = int(ll%2 == 0)
    return val + count_evens(ll.rest)

