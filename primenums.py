def prime_number_and_sum(num):
    if num <= 1:
        return -1
    for i in range(2, num):
        if num % i == 0:
            return -1
    else:
        return sum(range(num + 1))

result = prime_number_and_sum(7)
print(result)

result = prime_number_and_sum(10)
print(result)