mult = lambda x,y: x*y
print(mult(2,7))

points2D = [(1,2),(15,1),(5,-1),(10,4)]
points2D_sorted = sorted(points2D)
points2D_sortedY = sorted(points2D,key=lambda x: x[1])

print(points2D_sorted)
print(points2D_sortedY)

# another example
a = [1,2,3,4,5]
b = map(lambda x: x*2, a)
print(list(b))
d= filter(lambda x: x%2 == 0,a)
print(list(d))

from functools import reduce
e = reduce(lambda x,y: x+y,a)
print(e)

# do the samething
c = [x*2 for x in a]
print(c)