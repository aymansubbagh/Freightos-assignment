from utilties.utils import fake_credit, get_card_info, format_float
import random

# Creating class instance
class SnackMachine:
    accepted_coins = [0.1, 0.2, 0.5, 1]
    accepted_notes = [20, 50]
    user_amount = 0

    items = list(range(1,26))
    prices = [float(str(random.uniform(0.1, 20))[:4:])
                for i in range(len(items)+1)]

    # genrated prices for each item
    items_prices = dict(zip(items, prices))
    # un-comment the list below for a static item price
    # items_prices = {1: 17.7, 2: 0.35, 3: 11.5, 4: 17.7, 5: 3.38,
    #                 6: 16.9, 7: 3.85, 8: 5.75, 9: 4.22, 10: 16.4,
    #                 11: 6.15, 12: 18.6, 13: 19.7, 14: 15.5, 15: 16.1,
    #                 16: 17.1, 17: 9.62, 18: 14.4, 19: 0.15, 20: 4.73,
    #                 21: 16.8, 22: 9.29, 23: 9.47, 24: 7.45, 25: 15.6}


    # Check if item exist
    def check_item(self, item):
        if item in self.items:
            return True
        else:
            return False

    def get_price(self, item):
        '''
            return the price of the item
        '''
        print(f"item {item} price is: {self.items_prices[item]}$.")
        return self.items_prices[item]

    def insert(self, money):
        if self.is_money_valid(money):
            self.user_amount += money
        else:
            print(f"The machine only accepts: {self.accepted_coins}, and {self.accepted_notes}.")



    # is money from any of the machine's category
    def is_money_valid(self, money):
        if money in self.accepted_coins:
            return True
        elif money in self.accepted_notes:
            return True
        else:
            return False

    # is the amount sufficient
    def is_amount_sufficient(self, item, money):
        if money >= self.items_prices[item]:
            return True
        else:
            return False

    def is_there_change(self, price, amount):
        if amount-price > 0:
            return True, format_float(amount-price)
        else:
            return False, format_float(amount-price)

    def pay_with_card(self, credit_card_info, item):
        card_balance = float(get_card_info(credit_card_info)['MoneyRange'])
        if self.is_amount_sufficient(item, card_balance):
            return True, float(
                            self.recur_change(
                                    format_float(
                                            card_balance - self.get_price(item)
                                        )
                                    )
                            )
        else:
            print("Card Declined Insufficient Money.")
            return False, 0.0

    def recur_change(self, change):
        '''
            Recursive function to return the change from the machine cash box.
        '''
        if change == 0 :
            return 0
        else:
            if change >= 50:
                return 50 + self.recur_change(format_float(change)-50)
            elif change < 50 and change >= 20:
                return 20 + self.recur_change(format_float(change)-20)
            elif change < 20 and change >= 1:
                return 1 + self.recur_change(format_float(change)-1)
            elif change > 1 and change >= 0.5:
                return 0.5 + self.recur_change(format_float(change)-0.5)
            elif change > 0.5 and change >= 0.3:
                return 0.3 + self.recur_change(format_float(change)-0.3)
            elif change > 0.3 and change >= 0.2:
                return 0.2 + self.recur_change(format_float(change)-0.2)
            elif change > 0.2 and change >= 0.1:
                return 0.1 + self.recur_change(format_float(change)-0.1)
