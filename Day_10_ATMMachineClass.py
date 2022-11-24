#Programme for ATM Machine Functionality

class ATM:

    def __init__(self):
        self.pin="1234"
        self.balance=500
        self.menu()

    def menu(self):
        user_input = input(""" What would you like to do ? 
        Enter 1 for Setting PIN
        Enter 2 for Deposit
        Enter 3 for Withdrawal
        Enter 4 for Check Balance
        Enter 5 for Exit :  """)

        if user_input=='1':
            self.setpin()
        if user_input=='2':
            print("Welcome to Deposit Your Money")
            self.deposit()
        if user_input=='3':
            print("Welcome to Withdrawal Your Money")
            self.withdrawal()
        if user_input=='4':
            print("Welcome to Check Your Balance")
            self.check_balance()
        if user_input=='5':
            print("Good Bye!!! Have a Nice Day!!")

    def setpin(self):
        old_pin=input("Enter you old PIN :")
        if old_pin!=self.pin:
            print("PIN not matched")
        else:
            new_pin=input("Enter your new PIN :")
            self.pin=new_pin
            print("PIN set Successfully")
            self.menu()

    def deposit(self):
        deposit_Amount = int(input("Enter an amount to Deposit : "))
        bal=self.check_balance()
        self.balance+=deposit_Amount
        print("Money Deposited Successfully. New Balance is : "+ str(self.check_balance()))

    def withdrawal(self):
        withdraw_amt=int (input("Enter an amount to Withdraw !!! : "))
        bal = self.check_balance()
        if withdraw_amt > bal:
            print("Insufficient Balance !!!!")
        else:
            self.balance -= withdraw_amt
        print("Money Withdraw Successfully. Please collect your Rs. : " + str(self.check_balance()))

    def check_balance(self):
        print("Your current balance is : " + str(self.balance))

    def bye(self):
        print("Thank you for Using ATM Machine !!!!!")

a=ATM()