class BankAccounts:
    current_users = {
        1: {
            "NAME": "NIZAMUDHEEN MJ",
            "BANK NO.": "12412432421",
            "ADDRESS": "MARAYIL HOUSE ERNAKULAM",
            "BALANCE": 24234234
        },
        2: {
            "NAME": "AMJAD K JABIR",
            "BANK NO.": "132423432",
            "ADDRESS": "SDK ALUVA",
            "BALANCE": 234342
        },
        3: {
            "NAME": "PUNYA LALU",
            "BANK NO.": "23423423423",
            "ADDRESS": "KIZHILLUM , MUVATUPUZHA",
            "BALANCE": 99898989
        }
    }

    def __init__(self):
        pass

    def add_users(self):
        new_user_id = max(self.current_users) + 1
        self.current_users[new_user_id] = {
            "NAME": input("Enter the name in cap"),
            "BANK NO.": input("Enter the bank no:"),
            "ADDRESS": input("Enter the address"),
            "BALANCE": int(input("Enter the balance"))
        }

    def display_users(self):
        for users, user_info in self.current_users.items():
            print(f"User ID: {users}")
            for key, value in user_info.items():
                print(f"{key}: {value}")
            print()

    def balance(self, user_id):
        print(self.current_users[user_id]["BALANCE"])


class Bank(BankAccounts):

    def __init__(self):
        super().__init__()

    def withdraw_cash(self):
        user_id = int(input("Enter the User ID: "))
        if user_id not in BankAccounts.current_users:
            print("invalid user id..")
            return
        else:
            amount = int(input("Enter the amount: "))
            if BankAccounts.current_users[user_id]["BALANCE"] >= amount:
                BankAccounts.current_users[user_id]["BALANCE"] -= amount
                print("Transaction succesfull")
            else:
                print("Insufficient balance")
                return

    def deposit_cash(self):
        user_id = int(input("Enter the User ID: "))
        if user_id not in BankAccounts.current_users:
            print("invalid user id..")
            return
        else:
            amount = int(input("Enter the amount: "))
            BankAccounts.current_users[user_id]["BALANCE"] = BankAccounts.current_users[user_id]["BALANCE"].__add__(amount)
            print("Transaction successful")

    def balance_view(self):
        n = int(input("Enter the User ID: "))
        super().balance(n)


bank = Bank()
bank.balance_view()
bank.deposit_cash()1
bank.withdraw_cash()
bank.balance_view()
