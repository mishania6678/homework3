def power(x, y):
    # return x ** y
    static_x = x
    for i in range(abs(y)):
        x *= 1 / static_x
    return x if x != 0 and y != 0 else '0^0 неопределено'


num1, num2 = int(input()), int(input())
print(power(num1, num2))

# test2
