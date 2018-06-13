

'''


    Group Anagram

    Write a method to sort an array of strings so that all the anagrams are
    next to each other.

        We created a hash table where the key is the sorted(anagram) and the
        value is a list that contains each anagram that matches the key

        After creating the hash/dict, we are iterate over each list in the hash and
        and then iterate over each value in the list appending it... all items in the resultant
        list are sorted/grouped together with their associated anagrams

'''


from collections import defaultdict



def ana_sort(anagrams):
    # create a dict/hash of lists
    words = defaultdict(list)
    sorted_anagrams = []

    # build the hash where the key is the sorted version of the anagram
    for ana in anagrams:
        # sort the anagram
        sorted_ana = ''.join(sorted(ana))
        # add the sorted_anagram to the hash and append the unsorted word to the list pointed to by this key
        words[sorted_ana].append(ana)

    for key, list_val in words.items():
        for uniq_ana in list_val:
            sorted_anagrams.append(uniq_ana)


    return sorted_anagrams



arr = ['pppaas', 'base', 'iht', 'aseb', 'besa', 'hit', 'thi', 'ebas', 'pappas']


print('anagram array before sort: \t{anas}'.format(anas=arr))

print(' ')

print('array after sort: \t\t{sorted_anas}'.format(sorted_anas=ana_sort(arr)))



