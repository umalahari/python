import logging as lg
lg.basicConfig(
    filename="app.log",
    level=lg.DEBUG,
    format = "[%(asctime)s - %(levelname)s] - %(message)s"
)
# total Operations
operations = (
    "1. Balance\n",
    "2. withdraw\n",
    "3. deposite\n",
    "4. Transfer\n",
    "5. History\n",
    "6.exit\n"
)
# account table 
account_table = {12345:6789}

# Checking valid user
def valid_user(user_name:int, password:int):
    lg.debug("User in login page")
    if user_name in account_table:
        if account_table[user_name] == password:
            lg.info("User successfully logined")
            print("User successfully logined")
            return True
        else:
            lg.warning("Please check your login credentials")
            print("Please check your login credentials")
            return False
    else:
        lg.warning("Please check check your login credentials")
        print("Please check check your login credentials")
        return False
    
# balence function
def balence(user_name):
    lg.info("User in balence page")
    pass

# withdraw function
def withdraw(user_name):
    lg.info("User in withdraw page")
    pass

# deposite function
def deposite(user_name):
    lg.info("User in deposite page")
    pass

# transer function
def transfer(user_name):
    lg.info("User in transfer page")
    pass

# history function
def history(user_name):
    lg.info("User in history page")
    pass

# exit function
def exit_fun():
    lg.info("User in exit page")
    pass

# chose_operation function
def chose_operation(account_no, choice):
    lg.info(f"selected operation is {operations[choice-1]}")
    if choice == 1:
        balence(user_name=account_no)
    elif choice == 2:
        withdraw(user_name= account_no)
    elif choice == 3:
        deposite(user_name= account_no)
    elif choice == 4:
        transfer(user_name= account_no)
    elif choice == 5:
        history(user_name= account_no)
    elif choice == 6:
        exit_fun()
    else:
        print("Please selct between 1-6")

if __name__ == "__main__":
    print("Welcome to the online codegnan Banking")
    lg.info("Welcome to the online codegnan Banking")
    account_no = int(input("Please, enter account number: "))
    pin =int(input("Please enter pin number: "))
    lg.info(f"User credenctials are {account_no} and {pin}")
    if valid_user(user_name=account_no,password=pin):
        print(*operations)
        lg.info(operations)
        choice = int(input("Please select operation (1-6): "))
        chose_operation(account_no=account_no, choice=choice)
    else:
        lg.warning("User not found, please check with your login credentials")
        print("User not found, please check with your login credentials")