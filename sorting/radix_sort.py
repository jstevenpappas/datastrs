


def radix_sort(array, base=10):
    def list_to_buckets(array, base, iteration):
        print('arr={arr} base={base} iteration={it}'.format(arr=array, base=base, it=iteration))
        buckets = [[] for x in range(base)]
        for number in array:
            # Isolate the base-digit from the number
            digit = (number // (base ** iteration)) % base
            # Drop the number into the correct bucket
            buckets[digit].append(number)
            print(buckets)
        return buckets

    def buckets_to_list(buckets):
        print('buckets_to_list()')
        numbers = []
        for bucket in buckets:
            # append the numbers in a bucket
            # sequentially to the returned array
            for number in bucket:
                numbers.append(number)
        return numbers

    maxval = max(array)

    it = 0
    # Iterate, sorting the array by each base-digit
    while base ** it <= maxval:
        array = buckets_to_list(list_to_buckets(array, base, it))
        it += 1

    return array




arr = [8, 1000000, 5]


print(radix_sort(arr))