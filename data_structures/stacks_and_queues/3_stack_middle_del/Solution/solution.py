# code to delete middle of a stack 
# without using additional data structure. 

# Deletes middle of stack of size n. Curr is current item number 
class Stack: 
	def __init__(self): 
		self.items = [] 
	
	def isEmpty(self): 
		return self.items == [] 
	
	def push(self, item): 
		self.items.append(item) 
	
	def pop(self): 
		return self.items.pop() 
	
	def peek(self): 
		return self.items[len(self.items)-1] 
	
	def size(self): 
		return len(self.items) 
		
def deletemid(st) : 
	vals = []
	while not st.isEmpty():
		vals.append(st.pop())
	vals = sorted(vals)
	midval = vals[len(vals)//2]
	idx = vals.index(midval)
	for i in range(idx):
		st.push(vals[i])
	for i in range(idx+1, len(vals)):
		st.push(vals[i])

if __name__ == '__main__': 
    st = Stack() 

# push elements into the stack 
    st.push('1') 
    st.push('2') 
    st.push('3') 
    st.push('4') 
    st.push('5') 
    st.push('6') 
    st.push('7') 

    deletemid(st) 

# Printing stack after deletion 
# of middle. 
    while (st.isEmpty() == False) : 
	    p = st.peek() 
	    st.pop() 
	    print (p, end=" ") 