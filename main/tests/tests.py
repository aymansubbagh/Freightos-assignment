from snackMachine.snackMachine import SnackMachine
from utilties.utils import *
import unittest
class Test(unittest.TestCase):

    # Test that item exist
    def testItemExist(self):
        # item exist case
        res = SnackMachine().check_item(2)
        self.assertEqual(True, res)

    # Test that item doesn't exist
    def test_item_not_exist(self):
        # item doesn't exist case
        res = SnackMachine().check_item(-1)
        self.assertEqual(False, res)

    # Test that coins is valid
    def test_insert_valid_coins(self):
        # cois is valid
        res = SnackMachine().is_money_valid(0.2)
        self.assertEqual(True, res)

    # Test that notes is valid
    def test_insert_valid_notes(self):
        # notes is valid
        res = SnackMachine().is_money_valid(50)
        self.assertEqual(True, res)

    # Test that money isn't valid
    def test_insert_not_valid_coins(self):
        # money isn't valid
        res = SnackMachine().is_money_valid(100)
        self.assertEqual(False, res)

    # Test if the amount sufficient
    def test_amount_not_sufficient(self):
        # amount is not sufficient
        res = SnackMachine().is_amount_sufficient(7,1)
        self.assertEqual(False, res)

    # Test if the amount sufficient
    def test_amount_sufficient(self):
        # amount is sufficient
        res = SnackMachine().is_amount_sufficient(12,20)
        self.assertEqual(True, res)

    # Test if there's change
    def test_theres_change(self):
        # the amount exceeded the price and there is a change
        state, amount = SnackMachine().is_there_change(18.6, 20)

        self.assertEqual(True, state)
        self.assertEqual(True, 1.399)
        self.assertIsInstance(amount, float)

    # Test if there's change
    def test_theres_change(self):
        # there is no change
        state, amount = SnackMachine().is_there_change(18.6, 18.6)
        self.assertEqual(False, state)
        self.assertIsInstance(amount, float)

    # Test extract function
    def test_extract(self):
        money = extract("10$", "10$".find('$'))
        self.assertIsInstance(money, float)

    # Test extract function
    def test_extract(self):
        money = extract("10$", "10$".find('$'))
        self.assertIsInstance(money, float)

    # validate card info
    def test_validate_card(self):
        res = validate_card(fake_credit[0]['CardNumber'])
        self.assertEqual(True, res)

    # tests the card payment method
    def test_pay_with_card(self):
        state, change = SnackMachine().pay_with_card(fake_credit[0]['CardNumber'], 3)
        self.assertEqual(True, state)
        self.assertIsInstance(change, float)

    # tests card declined due to insufficient balance
    def test_card_declined(self):
        state, change = SnackMachine().pay_with_card(fake_credit[2]['CardNumber'], 3)
        self.assertEqual(False, state)
        self.assertIsInstance(change, float)


    def main():
        unittest.main()
