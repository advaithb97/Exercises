# A LinkedList is either:
# None
# Node

class Node:
    # first: int
    # rest: LinkedList
    def __init__(self, first, rest = None):
        self.first = first
        self.rest = rest

# Write a function named create_list that consumes a number n and returns a LinkedList of 1,2,..,n 
# create_list(3) -> Node(1, Node(2, Node(3, None)))
def create_list(n):
    if n == 0: return None
    ll = Node(1)
    x = helper(ll, 1, n+1)
    x = x.rest
    return x

def helper(node, counter, n):
    if counter == n: return node
    nodeval = Node(counter)
    node.rest = helper(nodeval, counter+1, n)
    return node

def printlist(ll):
    if not ll: return None
    cur = ll
    while cur:
        print(cur.first)
        cur = cur.rest

printlist(create_list(10))