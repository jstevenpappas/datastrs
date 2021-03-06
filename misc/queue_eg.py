


'''


    You can use a list as a queue (First in, First out) but...
        inserts and pops from beginning of list are slow b/c all the other Elements need to be shifted by 1


    Use a real queue in this case


'''


from collections import deque


queue = deque()


for i in range(0, 10):
    #print(i)
    queue.append(i)

#print(len(queue))


for i in range(0, len(queue)):
    print(queue.pop())
    #print(queue.popleft())


#print(queue.popleft()) # returns first one added to queue (e.g., 0)
#print(queue.popleft()) # returns second one added with is now at top of queue (e.g., 1)




d = dict()

for i in range(0, 10):
    d[str(i)] = i


for k, v in d.items():
    print('key = {k}, v = {v}'.format(k=k, v=v))