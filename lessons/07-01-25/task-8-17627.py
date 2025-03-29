from string import digits, ascii_lowercase
from itertools import product
alf = digits + ascii_lowercase
for val in product(alf[:15], repeat = 5):
    if val.count("8") == 1 and val.count("")