
# Task 1
DataBase = {}


def func1(name, customer_list, balance=0):
    if name not in customer_list.keys():
        customer_list[name] = 0
        customer_list[name] = balance
        return customer_list
    else:
        raise "customer name already exists"


func1("Reza", DataBase)
func1("Ali", DataBase, balance=10215)
# func1("Ali", DB, balance=547)
print(DataBase)


# DB2 = {}
# lamdafunc = (lambda name, customer_list={}, balance=0: customer_list.update(name, balance)("Ted", DB2, 300))
# print(DB2)

# we can use dict1.update(name, ballance) to update each user's ballance and use dict1.pop(name) to remove one of the users.

def deposit(user, db1, amount):
    db = db1.copy()
    if user in db.keys():
        balance0 = db[user]
        balance2 = balance0 + amount
        db[user] = balance2

        return db1.update(db), print(f"Depositing {amount} Euros, new account balance for {user} is {balance2} Euros")

    else:
        raise "user not found in customer's list. "


def withdraw(name, db1, amount):
    db = db1.copy()
    if name in db:
        balance0 = db[name]
        if balance0 - amount >= 0:
            balance2 = balance0 - amount
            db[name] = balance2
            print(f"withdrawing {amount} Euros. new account balance of {name} is {balance2} Euros")
        else:
            print(f"cannot with draw {amount} Euros, account balance for user {name} is {balance0} Euros")

        return db1.update(db)

    else:
        raise "user not found in customer's list. "


deposit("Ali", DataBase, 300)
withdraw("Ali", DataBase, 500)
withdraw("Reza", DataBase, 1)

print("\n"
      "\n"
      "Empty space \n"
      "\n"
      "\n")

# Task 2

class Customer:

    __database__ = {}

    def __init__(self, name, initial_balance=0):
        self.user = name
        self.init_balance = initial_balance

        if name not in self.__database__.keys():
            self.__database__[name] = 0
            self.__database__[name] = initial_balance

            print(f"New user {self.user} has been registered.")
        else:
            print(f"user {self.user} is already registered.")

    def deposit(self, amount):
        if self.user in self.__database__:
            self.__database__[self.user] += amount
            print(f"The {amount} Euros has been successfully deposited to {self.user} Current account \n"
                  f"New Current account balance is {self.__database__[self.user]}")
        else:
            print(f"the user {self.user} not found in our database: ")
        return self.__database__

    def withdraw(self, amount):
        if self.user in self.__database__:
            if self.__database__[self.user] >= 0:
                self.__database__[self.user] -= amount
                print(f"The {amount} Euros has been successfully withdrawn from {self.user} Current account \n"
                      f"New Current account balance is {self.__database__[self.user]}")
            else:
                print(f"Failed! \n"
                      f"Mr.|Ms. {self.user}, you have insufficient amount to withdraw \n"
                      f"your account balance is {self.__database__[self.user]} Euros.")
        else:
            print(f"the user {self.user} not found in our database, \n"
                  f"Please try to register first using: .register(#username#) ")


class SavingsCustomer(Customer):

    __savings__ = {}

    def __init__(self, name):
        super().__init__(name)
        self.Curr_balance = Customer.__database__[self.user]
        if name in self.__savings__:
            pass
        else:
            self.__savings__[name] = 0

    def withdraw_from_savings(self, amount1):
        state = self.__savings__[self.user] >= amount1
        if state:
            self.__savings__[self.user] -= amount1
            print(f"New Savings account balance for {self.user} is {self.__savings__[self.user]}")
            self.deposit(amount1)
        else:
            print("insufficient funds in Savings account")

    def deposit_to_savings(self, amount1):
        state = self.Curr_balance >= amount1
        if state:
            self.withdraw(amount1)
            self.__savings__[self.user] += amount1
            print(f"New Savings account balance for {self.user} is {self.__savings__[self.user]}")

        else:
            print("insufficient funds in Current account")


C1 = Customer("user2")
C1.deposit(2000)
C1.withdraw(100)

print("\n"
      "\n"
      "Empty space \n"
      "\n"
      "\n")

C2 = SavingsCustomer("user2")
C2.withdraw_from_savings(2000)
C2.deposit_to_savings(540)
C2.withdraw_from_savings(500)
