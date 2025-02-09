from itertools import permutations
alf = "макака"
count = 0
for val in set(permutations(alf,6)):
    val = "".join(val)
    if "аа" not in val:
        count += 1
print(count)