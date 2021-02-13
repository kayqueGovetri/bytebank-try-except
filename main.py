

class Client:
    def __init__(self, name, cpf, job):
        self.name = name
        self.cpf = cpf
        self.job = job


class CheckingAccount:
    total_accounts_created = 0
    operation_fee = None

    def __init__(self, client, agency, number):
        self.balance = 100
        self.client = client
        self.agency = agency
        self.number = number
        CheckingAccount.total_accounts_created += 1
        CheckingAccount.operation_fee = 30 / CheckingAccount.total_accounts_created

    def transfer(self, value, favored):
        favored.deposit(value)

    def withdraw(self, value):
        self.balance -= value

    def deposit(self, value):
        self.balance += value


client2 = Client(name="Kayque", cpf="12345678900", job="Developer")
account_client2 = CheckingAccount(client=client2, agency="00", number="00")
