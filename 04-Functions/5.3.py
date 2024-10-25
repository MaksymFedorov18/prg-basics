import mymodule

first_name = mymodule.input_string('Enter name: ')
last_name = mymodule.input_string('Enter last name: ')
age = mymodule.input_integer("Enter age: ")
salary = mymodule.input_integer("Enter salary: ")
is_salary_hidden = mymodule.input_boolean('Hide salary? (y/n) ')

print('DATA RECORD')
print('===========')
print('Name:',first_name)
print("Last name:", last_name)
print("Age:", age)
if is_salary_hidden == "n":
    print('Salary :',salary)