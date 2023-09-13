def add_this(*numbers):
    sum = 0
    for number in numbers:
        sum = sum + number
    return sum

print(add_this(1, 2, 3))    # 6
print(add_this(1, 2, 3, 4, 5))  # 15