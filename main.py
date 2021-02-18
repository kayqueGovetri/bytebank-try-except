

class Client:
    def __init__(self, name, cpf, job):
        self.name = name
        self.cpf = cpf
        self.job = job


class CheckingAccount:
    total_accounts_created = 0
    operation_fee = None

    def __init__(self, client, agency, number):
        self.__balance = 100
        self.client = client
        self.__agency = agency
        self.__number = number
        CheckingAccount.total_accounts_created += 1
        CheckingAccount.operation_fee = 30 / CheckingAccount.total_accounts_created

    @property
    def agency(self):
        return self.agency

    @property
    def number(self):
        return self.agency

    @property
    def balance(self):
        return self.balance

    def transfer(self, value, favored):
        favored.deposit(value)

    def withdraw(self, value):
        self.__balance -= value

    def deposit(self, value):
        self.__balance += value

    def __set_agency(self, value):
        if not isinstance(value, int):
            return
        if value <= 10:
            return
        self.__agency = value

    def __set_number(self, value):
        if not isinstance(value, int):
            return
        if value <= 10:
            return
        self.__number = value

    def __set_balance(self, value):
        if not isinstance(value, int):
            return
        if value <= 10:
            return
        self.__balance = value


client2 = Client(name="Kayque", cpf="12345678900", job="Developer")
account_client2 = CheckingAccount(client=client2, agency="00", number="00")
