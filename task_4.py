num = int(input())
largest_digit = 0
while num > 0:
    digit = num % 10
    if digit > largest_digit:
        largest_digit = digit
    num //= 10
print(largest_digit)
