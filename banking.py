import random
from database import get_connection


def open_account():
    conn = get_connection()
    cursor = conn.cursor()

    accnum = random.randint(1000000000, 9999999999)

    name = input("Enter name: ")
    password = input("Set password: ")
    phone = input("Phone: ")
    email = input("Email: ")
    address = input("Address: ")

    deposit = float(input("Initial deposit (>=1000): "))

    if deposit < 1000:
        print("Minimum deposit is 1000")
        return

    sql = """
    INSERT INTO accounts
    (accnum,password,name,phone,email,address,current_balance)
    VALUES (%s,%s,%s,%s,%s,%s,%s)
    """

    cursor.execute(sql, (accnum, password, name, phone, email, address, deposit))
    conn.commit()

    print("Account created successfully")
    print("Account Number:", accnum)


def deposit():
    conn = get_connection()
    cursor = conn.cursor()

    accnum = input("Enter account number: ")
    amount = float(input("Amount to deposit: "))

    sql = "UPDATE accounts SET current_balance = current_balance + %s WHERE accnum=%s"

    cursor.execute(sql, (amount, accnum))
    conn.commit()

    print("Deposit successful")


def withdraw():
    conn = get_connection()
    cursor = conn.cursor()

    accnum = input("Account number: ")
    amount = float(input("Withdraw amount: "))

    cursor.execute("SELECT current_balance FROM accounts WHERE accnum=%s", (accnum,))
    bal = cursor.fetchone()

    if bal and bal[0] >= amount:

        cursor.execute(
            "UPDATE accounts SET current_balance=current_balance-%s WHERE accnum=%s",
            (amount, accnum)
        )

        conn.commit()
        print("Withdrawal successful")

    else:
        print("Insufficient balance")


def balance():
    conn = get_connection()
    cursor = conn.cursor()

    accnum = input("Account number: ")

    cursor.execute("SELECT current_balance FROM accounts WHERE accnum=%s", (accnum,))
    result = cursor.fetchone()

    if result:
        print("Current Balance:", result[0])
    else:
        print("Account not found")