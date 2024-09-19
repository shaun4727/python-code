# itertools: product, permutations, combinations, accumulate, groupby and infinite iterators

from itertools import product

a = [1,2]
b = [3,4]
print(list(product(a,b)))

from itertools import permutations

c = [1,2,3]

print(list(permutations(c)))

from itertools import combinations

print(list(combinations(c,2)))

from itertools import accumulate
import operator

print(list(accumulate(c)))

from itertools import groupby

def smaller_than_3(x):
    return x<3

d = [1,2,3,4]
group_obj = groupby(d, key=smaller_than_3)

for key,value in group_obj:
    print(key, list(value))

# another group by example
persons = [{'name': 'Tim','age': 25},{'name':'Dan','age':25},{'name': 'Tisha', 'age': 27},{'name':'Claire','age': 28}]

group_obj1 = groupby(persons, key= lambda x: x['age'])

for key,value in group_obj1:
    print(key,list(value))