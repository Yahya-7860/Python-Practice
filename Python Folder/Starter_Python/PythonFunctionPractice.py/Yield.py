def evenGenerator(limit):
    for i in range(2, limit+1, 2):
        yield i


for i in evenGenerator(10):
    print(i)
