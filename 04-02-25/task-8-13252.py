from itertools import permutations
alf = "кидала"
count = 0
for val in set(permutations(alf,5)):
    val = "".join(val)
    if "аа" not in val:
        count += 1
print(count)