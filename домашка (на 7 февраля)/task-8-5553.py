from itertools import permutations

alf = "соточка"
count = 0
for val in set(permutations(alf, 7)):
    val = "".join(val)
    if "оо" in val or "оа" in val or "ао" in val:
        count += 1
print(count)
