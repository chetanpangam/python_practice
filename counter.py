# counter.py
from collections import Counter

myList = [1,1,2,3,4,5,3,2,3,4,2,1,2,3]
print(Counter(myList))

myDict= dict(Counter(myList))
for k, v in myDict.items():
    print(k, v)
