# Reads from file, line by line and prints with numbering
#
with open('countries.txt', 'r') as file:
    counter = 1
    for line in file:
        country_info = line.strip().split(',')  
        if len(country_info) == 3:  
            country, capital, population = country_info
    
            print(f"{counter}. {country}, {capital}, {population}")
            counter += 1
