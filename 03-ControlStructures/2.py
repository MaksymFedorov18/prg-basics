account_balance = 500
total_payment = (input(f"Enter payment amount: "))
    
if total_payment <= account_balance:
    print('Payment completed')
else: 
    print('No funds')