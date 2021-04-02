class InsufficientBalanceError(Exception):
    def __init__(self, message="", balance=None, value=None, *args, **kwargs):
        self.balance = balance
        self.value = value
        msg = "Insufficient balance to execute the transaction \n" \
              f"Balance: {self.balance} and Amount to be withdrawn: {self.value}"
        super(InsufficientBalanceError, self).__init__(message or msg)
