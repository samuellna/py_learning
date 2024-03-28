# Sets are like UNION-FIND algorithm
# It's a mutable type, but it only accepts imutable types as value

# How to create a set?

# x = {...} or x = set(...)
set1 = set('Samuel')
set1 = set()  # empty
set1 = {'Samuel', 1, 1.5, False}  # with values

# Sets are used to avoid duplicate values, it:

# - Doesn't accept unaterable values;
# - Doesn't has any indexes, because there's no sequence in the sets;
# - Is iterable.

l1 = [1, 2, 3, 3, 2, 1, "Samuel", "Samuel"] # This list contains repeated elements
set1 = set(l1) # The set1 has the 'l1' elements, removing repeated ones.
l2 = list(set1) # Now, 'l2' has all 'set1' attributes, without repeated elements too.
# So, that's a quickly and 'clean' (with less lines of code) way to remove all repeated elements in a list.

set1 = {1, 2, 3} 

# Iterating in the set: 
for number in set1:
    print(number)

# Useful methods: add, update, clear, discard

set_ = {"I", "date", "my", "boyfriend", "since", 2022}
set_.add('Hi') # It will add 'H' and 'i' separately.

complete_set = ['his', 'name', 'is', 'Arnaldo Junior', "he's", 61]

for word in complete_set:
    set_.add(word) # Adding new elements in the set_

set_2 = {'I', 'love', 'him', 'so', 'much', 'ABCDE'}
set_.update(set_2)
set_.discard('ABCDE') # Discards a element

print(set_)

set_.clear() # Clear the set

# Operadores úteis:
# s1 | s2 - union among two (or more than 2) sets;
# s1 & s2 - intersection among the sets;
# s1 - s2 - difference between two sets;
# s1 ^ s2 - "Simetric difference", what isn't in both sets.

s1 = {1, 2, 3}
s2 = {2, 3, 4}

s3 = [s1 | s2, s1 & s2, s2 - s1, s1 ^ s2]

print(s3)