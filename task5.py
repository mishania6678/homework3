row = input('Введите числа через пробел: ').strip().split()

while True:
    summ = counter = 0
    while counter < len(row):
        if not row[counter].isdigit():
            print(summ)
            quit()
        summ += int(row[counter])
        counter += 1
    row += input(f'Продолжите ряд {" ".join(row)} ').strip().split()
