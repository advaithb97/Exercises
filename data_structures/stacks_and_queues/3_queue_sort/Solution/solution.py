from queue import Queue 

def min(Q):
    P = Queue()
    R = Queue()
    while not Q.empty():
        value = Q.get()
        P.put(value)
        R.put(value)
    if P.empty(): return -1
    minval = P.get()
    index = 0
    currentidx = 0
    while not P.empty():
        val = P.get()
        currentidx += 1
        if val <= minval:
            minval = val
            index = currentidx
    while not R.empty():
        Q.put(R.get())
    return index

def mintorear(Q, minidx):
    if minidx == -1: return Q
    P = Queue()
    for i in range(minidx):
        value = Q.get()
        P.put(value)
    minval = Q.get()
    while not Q.empty():
        value = Q.get()
        P.put(value)
    P.put(minval)
    return P

def sort(q): 
    p = Queue()
    length = q.qsize()
    return helper(q, p, length)

def helper(q, p, length):
    if p.qsize() == length: return p
    minidx = min(q)
    q = mintorear(q, minidx)
    return helper(q,p,length)

if __name__ == '__main__': 
    from queue import Queue 
    q = Queue() 
    q.put(20)
    q.put(11)  
    q.put(51)  
    q.put(7)
    q.put(1)
    q.put(25)
    minidx = min(q)
    q = mintorear(q,minidx)
    
    q = sort(q)
    # Presorted queue  
    while (q.empty() == False): 
        print(q.queue[0], end = " ")  
        q.get() 