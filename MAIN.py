from banking import *

def menu():

    while True:

        print("\n--- BANK MANAGEMENT SYSTEM ---")
        print("1. Open Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Balance Enquiry")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            open_account()

        elif choice == "2":
            deposit()

        elif choice == "3":
            withdraw()

        elif choice == "4":
            balance()

        elif choice == "5":
            print("Thank you for using the system")
            break

        else:
            print("Invalid option")

if __name__ == "__main__":
    menu()