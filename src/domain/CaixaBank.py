from src.domain.Client import Client
from src.domain.Banks_BDD import get_client


class CaixaBank:

    def __init__(self, name, commission, amount_of_money, client):
        self.__name = name
        self.__commission = float(commission)
        self.__amount_of_money = float(amount_of_money)
        self.__client = Client.create_by_string(get_client())
        # self.__client = client
        print(self)

    def __repr__(self):
        print(self.__client)
        return 'Bank:\n\t name: {}\n\tcommission: {}%\n\tmoney: ${}'\
            .format(self.__name, self.__commission, self.__amount_of_money)

    def __str__(self):
        return '{}-{}-{}'.format(self.name, self.commission, self.amount_of_money)

    @classmethod
    def create_by_string(cls, string):
        name, commission, amount_of_money = string.split('-')
        return cls(str(name), float(commission), float(amount_of_money), None)

    @property
    def name(self):
        return self.__name

    @property
    def commission(self):
        return self.__commission

    @property
    def amount_of_money(self):
        return self.__amount_of_money

    def op_deposit_money(self, money):
        print('Depositing money...')
        self.__amount_of_money += money

    def op_extract_money(self, money):
        print('Extracting money...')
        if money > self.__amount_of_money:
            raise Exception('Error: It cannot extract more money than ATM limit')
        self.__amount_of_money -= money

    def operation(self, str_operation, money):
        if str_operation == 'deposit':
            self.__client.deposit_money(money)
            self.op_deposit_money(money)
            print(self)

        elif str_operation == 'extract':
            self.__client.extract_money(money)
            self.op_extract_money(money)
            print(self)

        else:
            raise Exception('Error: the operation introduced was not successful')