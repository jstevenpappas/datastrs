


"""Set of Plates.

I did this w/out looking at the solution - it took an hour and sucked.

"""


from mystack import MyStack


class Plates(MyStack):

    def __init__(self):
        super(Plates, self).__init__()
        self.plates = MyStack()
        self.number_plates = 0


class SetOfPlates(object):

    def __init__(self):
        self.plate_stacks = list()
        self.stack_capacity = 4
        self.total_plates = 0

    def push(self, data):
        num_stacks = len(self.plate_stacks)
        print('we currently have the following number of plate stacks: {num_stacks}'.format(num_stacks=num_stacks))

        if num_stacks == 0:
            print('No plate stacks yet so adding the first one!')
            # create a stack and append to list
            plates = Plates()
            plates.push(data)
            plates.number_plates += 1
            self.plate_stacks.append(plates)

        else:
            # we have multiple stacks possible in the list
            # which one stack in the list do we add the curr plate to?
            stack_idx = num_stacks - 1
            plates = self.plate_stacks[stack_idx]

            if plates.number_plates >= self.stack_capacity:
                print('\tYikes - we are at capacity with {num} plates, need another stack to add to...'.format(num=plates.number_plates))
                # curr stack at this idx is at capacity, create a new one
                new_plate_stack = Plates()
                new_plate_stack.push(data)
                new_plate_stack.number_plates += 1
                self.plate_stacks.append(new_plate_stack)
                print('\tPhew... now we have the following number of plate stacks: {num_stacks}'.format(num_stacks=len(self.plate_stacks)))

            else:
                plates.push(data)
                plates.number_plates += 1

            # increment the total across stacks
            self.total_plates += 1


    def pop(self):
        num_stacks = len(self.plate_stacks)
        stack_idx = num_stacks - 1

        if num_stacks > 0:
            plates = self.plate_stacks[stack_idx]
            ret_val = plates.pop()
            plates.number_plates -= 1

            if plates.number_plates == 0:
                print('\tOk... the plates in this stack are all gone - removing it from the list...')
                # this stack is empty, remove from list
                self.plate_stacks.remove(plates)
                print('\tWe now have the following number of plate stacks: {num_stacks}'.format(
                    num_stacks=len(self.plate_stacks)))

            # decrement the total across stacks
            self.total_plates -= 1
            return ret_val



ms = SetOfPlates()

for i in range(13):
    print('pushing the following value: {push}'.format(push=i))
    ms.push(i)


print('')

for i in range(13):
    print('just popped the following value: {pop}'.format(pop=ms.pop()))
