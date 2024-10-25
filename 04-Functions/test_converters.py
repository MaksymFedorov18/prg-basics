import converters

print('### Test converters')
print(f'Three meters is {converters.m_to_cm(3)} cm')  # Converts 3 meters to cm
print(f'Ten centimeters is {converters.cm_to_inches(10):.2f} inches')  # Converts 10 cm to inches
print(f'5 feet 8 inches is {converters.feet_and_inches_to_cm(5, 8)} cm')  # Converts 5 feet 8 inches to cm
