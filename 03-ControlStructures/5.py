basic_salary = 5000
total_salary = 0
is_bonus = True # does the employee receive a bonus
bonus = 0.15 # 15%
    
if is_bonus:
    total_salary = basic_salary * bonus
else:
     total_salary = basic_salary   
    
print(f'Basic salary: {basic_salary}')
print(f'Bonus included? {bonus}')
print(f'Total salary: {total_salary}')