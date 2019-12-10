bal=10000
pin=1234
class atm:
    def balance():
        return bal
    def withdraw(amount,bal):
        if(amount>bal):
            print("Insufficient Funds")
        else:
            bal=bal-amount
            print("Account balance is",bal)
    def deposit(amount,bal):
        bal=bal+amount
        print("Account balance is:",bal)
epin = int(input("Enter first number: "))
count=0
while(epin!=pin):
    epin=int(input("Wrong pin entered,enter pin again:"))
    count=count+1
    if(count==2):
        print("Your account has been blocked!")
        break
if(count!=2):
    choice=1
    while(choice!=0):
        print("0.Exit")
        print("1.Check Balance")
        print("2.Withdraw")
        print("3.Deposit")
        choice = int(input("Enter choice: "))
        if choice == 1:
            print("Result: ", atm.balance())
        elif choice == 2:
            amount=int(input("Enter amount"))
            print("Result",atm.withdraw(amount,bal))
        elif choice == 3:
            amount=int(input("Enter amount"))
            print("Result: ",atm.deposit(amount,bal))
        elif choice == 0:
             print("Exiting")
                


        else:
            print("Invalid choice!")
