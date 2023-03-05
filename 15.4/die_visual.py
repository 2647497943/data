from die import Die

die = Die()

results = []
for i in range(1000):
    x = die.roll()
    results.append(x)

f = []
for i in range(1, die.num_sides+1):
    n = results.count(i)
    f.append(n)

print(f)
