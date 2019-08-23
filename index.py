# Give the user the following options. Once the option that is selected is completed keep asking them until they hit 4 to quit:
#
# Hello, please choose one of following options:
# 1) Check balance
# 2) Add money to account
# 3) Withdraw money from account
# 4) Quit
# What will you like to do?

#Step one: create the menu.
# menu works -------------------------

#Step two:
menu = -1
account = 0 # Original ammount of money/
#kept saying variables weren't defined
addMoney = 0
takeAway = 0
display = 0
# new_money = account +
# new_balance = balance
while menu != 4:

    menu = int(input('Hello, please choose one of the following options \n'
                     '1) Check balance \n'
                     '2) Add money to account \n'
                     '3) Withdraw money from account \n'
                     '4) Quit \n'))
    if menu == 1:
        display = print(f'your account has a balance of ${account + addMoney - takeAway} dollars') # shows how much money user has
    elif menu == 2:
        addMoney = int(input('How much would you like to deposit')) # adds to the a
    if menu == 3:
        takeAway = int(input('How much would you like to withdraw'))
        if takeAway > display:
            print('insufficient funds')










    #
# select = -1
# while select != 3:
#     print(f' 1. send DM \n'
#           f' 2. Read DM \n'
#           f' 3. Quit ')
#     # get user selection
#     select = int(input('Enter the number menu option: '))
#
#     # check user selection
#     if select == 1:
#         # list contacts
#         print('send dm')
#         print(f' 1. A \n'
#               f' 2. B \n'
#               f' 3. C ')
