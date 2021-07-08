int_func = lambda text: text.title() if False not in [i in 'qwertyuiopasdfghjklzxcvbnm ' for i in text] \
    else 'Неправильный формат входных данных'

print(int_func(input()))

# test3
