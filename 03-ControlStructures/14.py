month = int(input('Enter month number (1..12): '))
if month in range(1,12,2):
    days = 31 
elif month == 2:
    days = 28
else :
    days = 30 ## months with 30 days


print(f'Month {month} has {days} days')