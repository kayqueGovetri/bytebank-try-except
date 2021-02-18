

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
        self.__agency = agency
        self.__number = number

        self.__set_agency(agency)
        self.__set_number(number)
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
        self.balance -= value

    def deposit(self, value):
        self.balance += value

    def __set_agency(self, value):
        if not isinstance(value, int):
            raise ValueError("O atributo agencia deve ser um inteiro")
        if value <= 0:
            raise ValueError("O atributo agencia deve ser maior que zero")
        self.__agency = value

    def __set_number(self, value):
        if not isinstance(value, int):
            raise ValueError("O atributo numero deve ser um inteiro")
        if value <= 0:
            raise ValueError("O atributo numero deve ser maior que zero")
        self.__number = value

    @balance.setter
    def balance(self, value):
        self._balance = value


def main():
    import sys

    accounts = []
    while True:
        try:
            name = input("Name client:\n")
            agency = input("Number agency:\n")
            number = input("Number account:\n")
            client = Client(name=name, cpf=None, job=None)
            account_checking = CheckingAccount(client=client, agency=agency, number=number)
            accounts.append(account_checking)
        except KeyboardInterrupt:
            print(f"\n\n{len(accounts)} create accounts")
            sys.exit()


if __name__ == "__main__":
    main()
