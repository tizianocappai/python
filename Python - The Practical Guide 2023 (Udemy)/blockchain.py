blockchain = []


def get_last_blockchain_value():
    # arr[-1] return last element of an array
    return blockchain[-1]


def add_value(transaction_amount, last_transaction=[1]):
    blockchain.append([last_transaction, transaction_amount])


def get_transaction_value():
    return float(input("\nInserisci l'importo della transazione: "))


def get_user_choice():
    user_input = input('Your choice: ')
    return user_input


def print_blockchain():
    for block in blockchain:
        print('\nOutputting Block')
        print(block)


tx_amount = get_transaction_value()
add_value(tx_amount)

while True:
    print('\nPlease choose')
    print('1: Add a new transaction value')
    print('2: Output the blockchain blocks')
    print('q: Quit')

    user_choice = get_user_choice()

    if user_choice == '1':
        tx_amount = get_transaction_value()
        add_value(tx_amount, get_last_blockchain_value())
    elif user_choice == '2':
        print_blockchain()
    elif user_choice == 'q':
        break
    else:
        print('Input was invaliid, please pick a value from the list!')


print('\n\nDone!')
