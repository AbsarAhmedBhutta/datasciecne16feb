l1 = [int(x) for x in input("enter  numbers").split()]

sum = 0

for num in l1:
    if num > 1:
        for i in range(2,num):
            if num % i == 0:
                print(num, "not prime")
                break
        else:
            print(num, "prime number")
            sum = sum+num
    else:
        print(num,"not prime")

print(sum,"sum of prime numbers")

