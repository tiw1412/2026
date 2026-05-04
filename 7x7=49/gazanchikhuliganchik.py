a, b = 1, 2
summary = lambda a, b: a + b
print(summary(a, b))

numbers = [1, 2, 3, 4]
step = list(map(lambda x: x*x, numbers))
print(step)

chisla = [10, 20, 30, 40]
sieg = list(map(lambda y: y - 5, chisla))
print(sieg)
people = [
    {'name': 'Alice', 'age': 25},
    {'name': 'Gazan', 'age': 6767},
    {'name': 'Benjamin', 'age': 88}
]
sorted_list = list(sorted(people, key=lambda elem: elem['age']))
print(sorted_list)

prices = [137, 284, 3289, 411]
discounts = [0.137, 0.2, 0.15, 0.05]
cross = list(map(lambda x, y: round(x - x*y, 2), prices, discounts))
print(cross)

newlist = [3, 139, 31, 82]
even = list(filter(lambda x: x % 2 == 0, newlist))
print(even)

words = ['apple', 'cat', 'border', 'wall', 'failure', 'totenkompf']
longer_than_five = list(filter(lambda x: len(x) > 5, words))
print(longer_than_five)