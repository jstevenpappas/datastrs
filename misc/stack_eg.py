




# use list as a Stack - (last in, first out)

'''

    Appends and pops from the end of list are fast, d

    Doing inserts or pops from the beginning of a list is slow
        (because all of the other elements have to be shifted by one).

'''


num_stack = []


for i in range(0, 5):
    num_stack.append(i)


print(num_stack.pop())  # print last one inserted
print(num_stack.pop(0)) # print first one inserted or bottome of stack