

'''

    Set - unordered collection with no duplicate elements

    Can perform membership tests, intersection, etc

'''
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']

fruit = set(basket)               # create a set without duplicates


print(basket)  # full list w/ dupes

print(fruit)   # only distinct members


poison_fruits = set(['dirty_apple', 'dirty_banana'])

good_fruits = set(['_apple', '_banana', 'dirty_apple'])



print(good_fruits.union(poison_fruits))


print(good_fruits.difference(poison_fruits))
print(poison_fruits.difference(good_fruits))