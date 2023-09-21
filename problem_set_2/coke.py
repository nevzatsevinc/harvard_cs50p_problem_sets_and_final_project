"""
Problem Set 2 - Coke Machine
https://cs50.harvard.edu/python/2022/psets/2/coke/
"""

amount_due = 50

# Loop to collect coins until the amount_due is zero or negative
while amount_due > 0:
    insert_coin = int(input('Insert Coin: '))
    
     # Check if the coin is an accepted
    if insert_coin == 25 or insert_coin == 10 or insert_coin == 5:
        amount_due -= insert_coin
        if amount_due > 0:
            print(f'Amount Due: {amount_due}')
        if amount_due <= 0:
            change_owed = abs(amount_due)
            print(f'Change Owed: {change_owed}')
    else:
        print(f'Amount Due: {amount_due}')