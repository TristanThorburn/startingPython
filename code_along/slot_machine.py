# Code along to: https://youtu.be/th4OBktqK1I

import random

# This is a global constant value, done in all caps
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8,
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2,
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]

        for column in columns:
            symbol_to_check = column[line]

            if symbol != symbol_to_check:
                break
        
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
    
    return winnings, winning_lines

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    # .items gives key and value pair in a dictionary
    for symbol, symbol_count in symbols.items():
        # _ is an anon variable in python to be used when you dont care about the count and just need to loop
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        # slice operator to copy the original list
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        
        columns.append(column)

    return columns

def print_slot_machine(columns):
    # transposing to change the direction of the print from horizontal to vertical making columns
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            # enumerate to get index
            if i != len(columns) - 1:
                # end tells print where to end on, and we dont want new line \n
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        
        print()

def deposit():
    while True:
        amount = input("What amount would you like to deposit? $$ ")
        # check to see if this is a valid whole number, also cannot use negative number, can be used on strings
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than zero.")
        else:
            print("Please enter a number")

    return amount

def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Please enter a valid number of lines")
        else:
            print("Please enter a number")

    return lines

def get_bet():
    while True:
        amount = input("What amount would you like to bet on each line? $$ ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between {MIN_BET}$ and {MAX_BET}$.")
        else:
            print("Please enter a number")

    return amount

def spin(balance):
    lines = get_number_of_lines()

    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You do not have enough to bet that amount. Your current balance is {balance}$")
        else:
            break

    print(f"You are betting {bet}$ on {lines} lines. Total bet is equal to: {total_bet}$")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won {winnings}$!")
    # unpack operator, passes every line from winning lines list to the print
    print(f"You won on lines:", *winning_lines)

    return winnings - total_bet

# Put into main function so if we end the game we can call main again to re-start the game
def main():
    balance = deposit()
    
    while True:
        print(f"Current balance is {balance}$")
        answer = input("Press enter to play, or q to quit.")

        if answer == "q":
            break
        # spin returns balance change
        balance += spin(balance)
    
    print(f"You left with {balance}$")

main()