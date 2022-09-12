from tests.tests import Test
from snackMachine.snackMachine import SnackMachine
from utilties.utils import *

# Check if app is being executed directly
if __name__ == '__main__':
    snackMachine = SnackMachine()
    print(snackMachine.items_prices)
    print("Please press an item of your choice between 1-25.")
    pressed_keypad = int(input())
    state = False

    try:
        # Check if item exist
        if snackMachine.check_item(pressed_keypad):
            # Customer select the payment method
            print('Would you like to pay with credit card? ')
            print('1: Yes.')
            print('2: No.')
            try:
                if input() == '1':
                    credit_card_info = "4325-8497-9560-9817"
                    # validate card
                    if validate_card(credit_card_info):
                        # complete payment
                        state, change = snackMachine.pay_with_card(credit_card_info, pressed_keypad)

                else:
                    # keep looping until amount is sufficient
                    while not snackMachine.is_amount_sufficient(pressed_keypad, snackMachine.user_amount):
                        money = input(f"Insert money; Machine accepts {snackMachine.accepted_coins} and {snackMachine.accepted_notes}.")

                        # Check currency
                        if money.startswith('$') or money.endswith('$'):
                            snackMachine.insert(extract(
                                                    money,
                                                    money.find('$')
                                                ))
                            print(f"\tHere's Your amount of money: {snackMachine.user_amount}$")
                            state, change = snackMachine.is_there_change(
                                                        snackMachine.get_price(pressed_keypad),
                                                        snackMachine.user_amount
                                                        )
                        else:
                            print('The Machine only accepts US dollars')
            # Handle KeyboardInterrupt Error
            except KeyboardInterrupt:
                print('\naborted')

            print(f"item number {pressed_keypad} dispensed successfully.")

            # Check for change
            if state:
                print(f"You have change of amount {change}.")
                print("Change dispensed successfully.")
                snackMachine.user_amount = 0
    # Handle KeyboardInterrupt Error
    except KeyboardInterrupt:
        if snackMachine.user_amount > 0:
            print(f"\nYour money has been dispensed successfully: {snackMachine.user_amount}$.")
    # Run Test cases
    Test.main()
