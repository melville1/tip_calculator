# returns total bill with tax added
def sales_tax(amount):
    return (amount * 0.10)
   
# This function will return the tip amount. The function has NOT added the tip to the bill yet.
def tip_selection(total_bill):
    try: 
        tip = float(input(f'How much would you like to tip  15% 20% 25% ? or please enter custom amount ' ))
        tip_total_amount = total_bill * (0.01*tip)
    except:
        print('Wrong value please enter a float')
    return tip_total_amount

user_input = "YES"
while user_input == "YES":
    try: 
    # Here I am going to ask the user how much the total is.
        amount = float(input(f'What is your total bill ? '))
    # I will be asking how many people are paying.
        guest = int(input(f'How many people are paying ? '))
    # Then I will be asking how much they want to tip 


    # calculate sales tax and round the amount 2 decimal points.
        salesTax = sales_tax(amount)
        tip_amount_only = tip_selection(amount)
        final_bill = (amount + tip_amount_only + salesTax) / guest
        
        print(round(final_bill,2))
        user_input = input(f'Do you wish to continue ? Enter Yes or No ').strip().upper()
        while user_input not in ['YES','NO']:
            print('You must enter Yes or No ')
            user_input = input(f'Do you wish to continue ? Enter Yes or No ').strip().upper()
    except ValueError:
        print("Please enter a valid number")
print('God Bless')