
def totalbill_and_sales_amount(amount):
    sales_amt = (amount * 0.1)
    total_amt = sales_amt + amount
    return round(total_amt,2)



# This function will return the tip amount. The function has NOT added the tip to the bill yet.
def tip_selection(total_bill):
    tip = float(input(f' How much would you like to tip  15% 20% 25% ? or please enter custom amount ' ))
    return  (tip /100) * total_bill 
   


# this functino will split the bill
def number_of_people(people,total_bill):
    return  round(total_bill /people, 2)
    
    

while True:
# Here I am going to ask the user how much the total is.
    amount = float(input(f'What is your total bill ? '))
# I will be asking how many people are paying.
    guest = int(input(f'How many people are paying ? '))
# Then I will be asking how much they want to tip 


# calculate sales tax and round the amount 2 decimal points.
    total_bill = totalbill_and_sales_amount(amount)
    tip_amount_only = tip_selection(total_bill)
    tip_and_total_bill = total_bill + tip_amount_only
    split_amount = number_of_people(guest,tip_and_total_bill)

    print(split_amount)
    user_input = input(f'Do you wish to continue ? Enter Yes or No ').strip().upper()
    while user_input not in ['YES','NO']:
        print('You must enter Yes or No ')
        user_input = input(f'Do you wish to continue ? Enter Yes or No ').strip().upper()
    if user_input == 'NO':
        break 
print('God Bless')