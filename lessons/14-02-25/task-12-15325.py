str = "8" * 45
while "1111" in str or "8888" in str:
    if "1111" in str:
        str = str.replace("1111", "88",1)
    else:
        str = str.replace("8888", "11",1)
print(str)