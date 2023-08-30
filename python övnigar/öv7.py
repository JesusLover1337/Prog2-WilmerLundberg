def is_prime(number):
    y = 2
    while number > y:
        if number % y == 0:
            return False
        y = y + 1
x = 0
n = 2
while x < 1000  :
    print(x)
    result = is_prime(n)
    if result == False:
        n = n + 1
        ...
    else:
        x = x + 1
        if x != 1000:
            n = n + 1
print(f"The 1000th prime number is {n}.")