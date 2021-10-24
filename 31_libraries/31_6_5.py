import itertools

counter = 0
decimals = "1234567890"
for i in itertools.product(decimals, repeat=4):
    print(i)
    counter += 1

print(counter)
