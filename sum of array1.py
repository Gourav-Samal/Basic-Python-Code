from functools import reduce
arr = [12, 32, 34, 56]
res = reduce(lambda a, b: a + b, arr)
print("Sum", res)
