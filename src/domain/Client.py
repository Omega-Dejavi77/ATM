from src.domain.Banks_BDD import set_client_info, save


class Client:

    def __init__(self, first_name, last_name, physical_money):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__physical_money = physical_money

    def __repr__(self):
        return 'Client: \n\tfirst name: {}\n\tlast name: {}\n\tmoney: ${}'\
            '\n---------------------------------------------------------'.\
            format(self.first_name, self.last_name, self.physical_money)

    def __str__(self):
        return '{}-{}-{}'.format(self.first_name, self.last_name, self.physical_money)

    @classmethod
    def create_by_string(cls, string):
        first_name, last_name, physical_money = string.split('-')
        return cls(first_name, last_name, float(physical_money))

    @property
    def first_name(self):
        return self.__first_name

    @property
    def last_name(self):
        return self.__last_name

    @property
    def full_name(self):
        return '{}, {}'.format(self.__last_name, self.__first_name)

    @property
    def physical_money(self):
        return self.__physical_money

    @full_name.setter
    def full_name(self, full_name):
        first_name, last_name = full_name.split(' ')
        self.__first_name = first_name
        self.__last_name = last_name

    @full_name.deleter
    def full_name(self):
        print('Delete fullname!')
        self.__first_name = None
        self.__last_name = None

    def deposit_money(self, money):
        if float(money) > self.physical_money:
            raise Exception('You can not deposit more money than you own')
        self.__physical_money -= money
        set_client_info(self)
        save(self)

    def extract_money(self, money_to_extract):
        self.__physical_money += money_to_extract
        set_client_info(self)
        save(self)
