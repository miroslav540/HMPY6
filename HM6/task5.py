collection = [2, 3, 4, 9, 1, 3]
length = len(collection)
print(list(map(lambda i: collection[i] * collection[length - i - 1], range(length // 2 + length % 2))))