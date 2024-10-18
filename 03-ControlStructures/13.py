x = int(input('Enter first number: '))
y = int(input('Enter second number: '))

if x < 0 and y < 0 :
    print(f'At least one of the numbers {x} and {y} is not negative')
else:
    print("At least one number is negative")

for i in range(1,12,3):
    print(i)