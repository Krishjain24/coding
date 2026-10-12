
"""
# Q. ATM Machine Simulation
#
# Write a Python program to simulate an ATM machine with the following rules:
#
# 1. PIN Verification:
#    - Default correct PIN is 1234.
#    - User gets a maximum of 3 attempts to enter the correct PIN.
#    - If entered incorrectly 3 times, print "Card Blocked! Please contact your bank." and terminate.
#
# 2. Main Menu (runs continuously until user exits):
#    - Initial Account Balance = ₹5000. 
#    - If PIN is correct, show the menu options:
#        1. Check Balance
#        2. Deposit Cash
#        3. Withdraw Cash
#        4. Exit
#
# 3. Operations:
#    - Option 1: Display the current balance.
#    - Option 2: Ask for deposit amount, add it to balance, and display updated balance.
#    - Option 3: Ask for withdrawal amount.
#                If amount <= balance, deduct and print "Withdrawal Successful".
#                Otherwise, print "Insufficient Balance!".
#    - Option 4: Print "Thank you for using our ATM. Have a nice day!" and exit the loop.
#    - Any other option: Print "Invalid Choice! Please choose 1 - 4."
"""




"""
under attempts
pin input
pin check
under attempts -> menu 1,2,3,4
menu_select_option input
basis of the menu work krna hai 
exit -> 4 code stop
"""





correct_pin = 3605
balance = 500000
attempts = 10
pin_pass = False
pin_length = 0
#  this while is for checking user pin is correct or not 
# if correct we are doing this pin_pass a varaible as True otherwise False
while attempts > 0:
    input_pin = int(input("enter the pin : "))
    
    temp_pin = input_pin
    while temp_pin >0:
        pin_length+=1
        temp_pin= temp_pin//10
    
    # 1234 // 10 -> 123 -> 123//10 -> 12 -> 12//10 ->1 -> 1//10 ->0
    
    if pin_length == 4:
        
        if input_pin == correct_pin:
           # main menu open krna
          print("opening main menu")            
          pin_pass = True 
          break
        else:
                attempts-=1
                if attempts >0:
                    print(f"pin is incorrect password you have just {attempts}")
                else:
                    print("card blocked")
      
    elif pin_length>4:
        print(f"your pass greater than 4 is of {pin_length}password should be in 4 digits")
    elif pin_length <4:
        print(f"your pass is smaller than 4 of {pin_length}password should be in 4 digits")

            
atm_used =0
if pin_pass == True:
    while True:
        print("ATM MENU Welcome")
        print("1 Check Balance")
        print("2 Deposit Cash")
        print("3 Withdraw Cash")
        print("4 Exit")
        
        option = int(input("enter your choice (1-4)"))
        
        if option ==1:
            print(f"Your current balance is {balance}")
            atm_used+=1
        elif option ==2:
            atm_used+=1
            deposit_amount = int(input("enter the ammount to deposit"))
            if deposit_amount >0:
                balance += deposit_amount
                print(f"{deposit_amount} deposited done")
                print(f"Updated Balance {balance}")
            else:
                print("Invalid Deposit amount")
        elif option ==3:
            atm_used+=1
            withdraw_amount = int(input("enter the amount to withdraw"))
            if withdraw_amount > balance:
                print("Insufficient Balance")
            elif withdraw_amount <=0:
                print("Invalid Amount to withdraw")
            else:
                balance -= withdraw_amount
                print(f"congo sir collect your cash{withdraw_amount}")
                print(f"remaining balance is {balance}")
        elif option ==4:
            if atm_used == 0:
                print(" get lost you waste atm electricity")
            else:
                print("Thank you for using our ATM. Have a nice day!")
            break
        else:
            print(f"Invalid Option be in the options limits (1-4)")
               
                
            
# first time 4  -> get lost you waste atm electricity



"""

# user password - > 4 digit 
# userpassword 4 se kaam ya jyda -> password should be 4 digit
user -> 3 digit -> your password is of 3 digit it should of 4
user -> 10 digit -> your password is of 10 digit it should of 4
# 4 -> 1000 se 9999

"""