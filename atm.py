import time

print("Please insert your CARD")
time.sleep(2)

password = 1234
balance = 5000

pin = int(input("Enter your ATM PIN: "))

if pin == password:
    while True:
        print("""
1 == Check Balance
2 == Withdraw Balance
3 == Deposit Balance
4 == Exit
        """)

        try:
            option = int(input("Please enter your choice: "))
        except:
            print("Please enter a valid option")
            continue

        if option == 1:
            print(f"Your current balance is ₹{balance}")

        elif option == 2:
            withdraw_amount = int(input("Enter withdrawal amount: "))
            
            if withdraw_amount <= balance:
                balance = balance - withdraw_amount
                print(f"₹{withdraw_amount} debited from your account")
                print(f"Remaining balance is ₹{balance}")
            else:
                print("Insufficient Balance!")

        elif option == 3:
            deposit_amount = int(input("Enter deposit amount: "))
            balance = balance + deposit_amount
            print(f"₹{deposit_amount} credited to your account")
            print(f"Updated balance is ₹{balance}")

        elif option == 4:
            print("Thank you for using ATM")
            break

        else:
            print("Invalid option. Please try again.")

else:
    print("Wrong PIN! Please try again.")
