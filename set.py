# sets: unordered, mutable, no duplicates
# myset = set({1,2,2,3})
myset = set("hello")

# insert 
myset.add(1)
# remove
myset.remove("l")

# discard is better than remove 
myset.discard("h") # if it does not find "h", it won't raise any error

# pop also work in set. gives arbitrary value
print(myset)

# calculating union
odds = {1,3,5,7,9}
even = {2,4,6,8,10}
primes = {2,3,5,7}

u = odds.union(even)

print(u)