class Transaction:
    def __init__(self,amount):
        self.amount = amount


class Account:

    def __init__(self):
        self.transactions = []

    def calculate_balance(self):
        if len(self.transactions) == 0:
            return "0.00"

        return self.transactions[0].amount

    def register_transaction(self, tx1):
        self.transactions.append(tx1)
