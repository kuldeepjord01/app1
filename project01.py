######
#project 1
#######
 
accounts = {
    '102012': {
        'name': 'mike',
        'balance': 10000
    },
    '102013': {
        'name': 'vamsi',
        'balance': 34.5
    },
    '102014': {
        'name': 'arun',
        'balance': 230500
    }
}

def show_menu():
        
    while True:
        print('''
            1. View Account Balance
            2. Transfer Amount
            3. Withdraw Amount
            4. Deposit Amount
            5. Exit
        ''')
        option = int(input('Choose an option:'))
        if option == 1:
            acc = input('Enter Acc number:')
            if acc in accounts:
                b = accounts[acc]['balance']
                print(f"Your balance is Rs.{b}/-")
            else:
                print('Account not found')
        elif option == 2:
            sa = input('Enter Source Account:')
            da = input('Enter Destination Account:')
            amount = int(input('Amount to Transfer: '))
            accounts[sa]['balance'] -= amount
            accounts[da]['balance'] += amount
            print('Transfer successful.')
        
        elif option == 3:
            acc =input('Enter acc number: ')
            amount = int(input("Enter amount:"))
            if acc in accounts:
                accounts[acc]["balance"] -=amount
                print("withdrawal successfull..")
        elif option == 4:
            acc = input("Enter acc number: ")
            depo =int(input("Enter deposit amount:"))
            if acc in accounts:
                accounts[acc]["balance"] += depo
                print("deposit successfull....")
        elif option == 5:
            print("Exitig......thankyou")
            break
        else:
            print('Invalid option..., try again!')

def main():
        show_menu()

if __name__ == "__main__":
    main()