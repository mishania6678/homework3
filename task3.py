def two_max_sum(a, b, c):
    sorted_nums = sorted((a, b, c))
    return sorted_nums[-1] + sorted_nums[-2]


num1, num2, num3 = map(int, input().split())
print(two_max_sum(num1, num2, num3))

# test2

