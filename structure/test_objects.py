import unittest
from objects import Transaction, Account


class MyTestCase(unittest.TestCase):

    def test_a_transaction_can_be_constructed(self):
        tx = Transaction("DEBIT", "30.45")
        self.assertEqual("DEBIT", tx.type)
        self.assertEqual("30.45", tx.amount)

    def test_an_account_should_have_zero_balance_before_any_txs_are_added(self):
        account = Account()
        self.assertEqual("0.00", account.calculate_balance())

    def test_an_account_should_know_the_balance_of_its_transactions(self):
        account = Account()
        tx1 = Transaction("DEBIT", "20.34")
        account.register_transaction(tx1)
        self.assertEqual("20.34", account.calculate_balance())


if __name__ == '__main__':
    unittest.main()
