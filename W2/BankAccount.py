account = 0

# Deposit
desposit  = float(input("How much would you like to desposit? \n"))
account += desposit


# Withdrawl
withdrawl = float(input("How much would you like to withdrawl? \n"))


# Check if withdrawl is valid
if(withdrawl < account):
    account -= withdrawl
else:
    print("You cannot withdrawl that much money!")
    account -= 0.99 # fee for overdraft
   
# Display balance
print(f"The new balance of your account is: ${account:.2f}")
