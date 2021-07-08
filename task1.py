num1, num2 = float(input()), float(input())

print((lambda x, y: x / y)(num1, num2) if num2 != 0 else 'Нельзя делить на ноль')

# test2
