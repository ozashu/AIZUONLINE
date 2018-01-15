def fizzbuzz(num):
    if num % 3 == 0 & num % 5 == 0:
        return "fizzbuzz"
    elif num % 3 == 0:
        return "fizz"
    elif num % 5 == 0:
        return "buzz"
    else:
        return int(num)

for i in range(1, 100):
    print(fizzbuzz(i))
