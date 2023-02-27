genesis_block = {
    'previous_hash': '',
    'index': 0,
    'transactions': [],
}
blockchain = [genesis_block]
open_transaction = []
owner = 'Tiz'


def hash_block(block):
    return '-'.join([str(block[key]) for key in block])


def get_last_blockchain_value():
    # arr[-1] return last element of an array
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def add_transaction(sender, recipient, amount=1.0):
    """" Append a new value as well as the last blockchain value to the blockchain

        Arguments:
            :sender: The sender of the coins.
            :recipient: The recipient of the coins.
            :amount: The amount of coins sent with transaction (default = 1)
    """
    transaction = {
        'sender': sender,
        'recipient': recipient,
        'amount': amount
    }

    open_transaction.append(transaction)


def mine_block():
    last_block = blockchain[-1]
    hashed_block = hash_block(last_block)
    print(hashed_block)

    block = {
        'previous_hash': hashed_block,
        'index': len(blockchain),
        'transactions': open_transaction,
    }
    blockchain.append(block)


def get_transaction_value():
    tx_recipient = input("\nEnter the recipient of the transaction: ")
    tx_amount = float(input("\nEnter the amount of the transaction: "))
    return (tx_recipient, tx_amount)


def get_user_choice():
    user_input = input('Your choice: ')
    return user_input


def print_blockchain():
    for block in blockchain:
        print('\nOutputting Block')
        print(block)
    else:
        print('-' * 20)


def verify_chain():
    for index, block in enumerate(blockchain):
        if index == 0:
            continue
        if block['previous_hash'] != hash_block(blockchain[index - 1]):
            return False
    return True


waiting_for_input = True

while waiting_for_input:
    print('\nPlease choose')
    print('1: Add a new transaction value')
    print('2: Mine new block')
    print('3: Output the blockchain blocks')
    print('h: Manipulate the chain')
    print('q: Quit')

    user_choice = get_user_choice()

    if user_choice == '1':
        tx_data = get_transaction_value()
        recipient, amount = tx_data
        add_transaction(owner, recipient, amount)
        print(open_transaction)
    elif user_choice == '2':
        mine_block()
    elif user_choice == '3':
        print_blockchain()
    elif user_choice == 'h':
        if len(blockchain) >= 1:
            blockchain[0] = {
                'previous_hash': '',
                'index': 0,
                'transactions': [{
                    'sender': 'Ciccio',
                    'recipient': 'Carlo',
                    'amount': 13.2
                }],
            }
    elif user_choice == 'q':
        waiting_for_input = False
    else:
        print('Input was invaliid, please pick a value from the list!')

    if not verify_chain():
        print_blockchain()
        print('Invalid blockchain!')
        break
else:
    print('User left!')

print('\n\nDone!')
