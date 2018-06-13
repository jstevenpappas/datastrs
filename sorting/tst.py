


#arr=[1, 2 ,3, 4]

'''
arr=[4, 3, 2, 1]

print(arr)

for passnum in range(len(arr)-1, 0, -1):
    print('{pn}'.format(pn=passnum))
    for idx in range(passnum):
        print('    {idx}'.format(idx=idx))

        if arr[idx] > arr[idx+1]:
            tmp = arr[idx]
            arr[idx] = arr[idx+1]
            arr[idx+1] = tmp


print(arr)
'''


# reset array
arr=[4, 3, 2, 1]


for fillslot in range(len(arr)-1, 0, -1):
    print('fillslot = {fs}'.format(fs=fillslot))
    pos_max = 0

    for location in range(1, fillslot + 1):
        print('    {loc}'.format(loc=location))

        if arr[location] > arr[pos_max]:


            print('idx={li} & val={lv}  >   idx={pi} w/ val={pv}'.format(li=location, lv=arr[location],
                                                                         pi=pos_max, pv=arr[pos_max]))
            pos_max = location

        print(arr)

        print('swapping w/ new pos_max val={pm}'.format(pm=pos_max))

        arr[fillslot], arr[pos_max] = arr[pos_max], arr[fillslot]

        print(arr)


#print(arr)