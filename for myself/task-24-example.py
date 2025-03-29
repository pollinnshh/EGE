with open('2407.txt', 'r') as file:
    data = file.readline()

n = len(data)
lt = 0  # Левый указатель
cnt = 0  # Количество вхождений 'FSRQ'
max_len = 0  # Максимальная длина подстроки

# Проходим по строке с правым указателем
for rt in range(n - 3):
    # Проверяем, есть ли 'FSRQ' на текущей позиции
    if data[rt:rt + 4] == 'FSRQ':
        cnt += 1

    # Если количество вхождений 'FSRQ' превышает 80,
    # сдвигаем левый указатель
    while cnt > 80:
        if data[lt:lt + 4] == 'FSRQ':
            cnt -= 1
        lt += 1

    # Если количество вхождений 'FSRQ' равно 80,
    # обновляем максимальную длину
    if cnt == 80:
        max_len = max(max_len, rt - lt + 4)

print(max_len)
