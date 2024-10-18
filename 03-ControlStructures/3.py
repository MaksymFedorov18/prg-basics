total_tasks = 20
tasks_ok = int(input("Enter amount of tasks scored: "))
test_passed = False
    
if tasks_ok == 10 or tasks_ok >= total_tasks :
    test_passed = True
    
if test_passed:
    print('Congratulations! You passed the test.')
else:
    print('Unfortunately, you failed the test.')
   