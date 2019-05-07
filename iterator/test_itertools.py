import itertools

print("chain")
print(list(itertools.chain([1, 2, 3, 4], range(5, 9), "the qucik and the slow")))

print("cycle")
cycler = itertools.cycle([1, 2, 3])
print(cycler.__next__())
print(cycler.__next__())
print(cycler.__next__())
print(cycler.__next__())
print(cycler.__next__())
print(cycler.__next__())
print(cycler.__next__())

print("zip longest")
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c', 'd', 'e']

zipped = itertools.zip_longest(list1, list2)
print(list(zipped))