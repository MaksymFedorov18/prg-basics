###
# Calculates and prints the quarter of the year for a given
# month number (1..12)
#
month = int(input('Enter month number (1..12): '))

if month >= 10:
    quarter = "fourth"
elif month <= 3:
    quarter = "first"
elif month > 3 and month <= 6:
    quarter = "second"
elif month > 6 and month <= 9:
    quarter = "third"

print(f'Month {month} is in the {quarter} quarter of the year')