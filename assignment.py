fizz = []
buzz = []
fizzbuzz = []

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        fizzbuzz.append(number)
    elif number % 3 == 0:
        fizz.append(number)
    elif number % 5 == 0:
        buzz.append(number)

print("Fizz numbers (divisible by 3):")
print(fizz)

print("\nBuzz numbers (divisible by 5):")
print(buzz)

print("\nFizzBuzz numbers (divisible by both 3 and 5):")
print(fizzbuzz)
