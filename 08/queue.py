
queue = []

def put(value):
    queue.append(value)

def get():
    if not empty():
        return queue.remove(queue[0])
    else:
        return None

def empty():
    return len(queue) == 0

def display():
    for i in queue:
        print(i,end = " ")
    print()