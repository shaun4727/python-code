# collections: Counter, namedtuple, orderedDict, defaultdict, deque
from collections import Counter
from collections import ChainMap

# counter
a = "aaaabbbcc"
my_counter = Counter(a)

print(my_counter)

# ChainMap
baseline = {'music': 'bach', 'art': 'rembrandt'}

adjustments = {'art': 'van gogh', 'opera': 'carmen'}
list1 = list(ChainMap(baseline))

for i in range(len(list1)):
    print(baseline[list1[i]]);


# default dict
from collections import defaultdict
d = defaultdict(int)
d['a'] = 1
d['b'] = 2

print(d['c'])

# deque //look in the doc