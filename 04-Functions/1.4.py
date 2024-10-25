def sum_digits(number):
    number = abs(number)
    number_str = str(number)
    sum=0
    for digit in number_str:
        digit = int(digit)
        sum += digit
    return sum

any_number = int(input('Enter integer number: '))
result = sum_digits(any_number)
print(f'The sum of the digits in the number {any_number} is {result}')