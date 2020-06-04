# Code your solution here
def push(stack_a):
    newlist = []
    newlist.append('Python')
    for elem in stack_a:
        newlist.append(elem)
    return newlist
stack_a=['C','Perl','C++','Java']
result=push(stack_a)
print(result)