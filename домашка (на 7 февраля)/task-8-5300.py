from itertools import permutations

alf = "хочу в вуз"
count = -1
for val in set(permutations(alf, 10)):
    val = "".join(val)
    if "  " not in val and val[0] != " " and val[-1] != " " and val[0] != "у" and " у" not in val:
        count += 1
print(count)
