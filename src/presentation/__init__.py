#from sys import exit
from src.domain.CaixaBank import CaixaBank
#from src.Client import Client

if __name__ == '__main__':

    str_bank = 'Caixa Bank-0.2-100000'
    obj_bank = CaixaBank.create_by_string(str_bank)

    print(obj_bank)
    while True:
        try:
            """First we are gonna ask to the client which operation wants to make"""

            str_operation = input('Choose the operation you wanna make (write deposit or extract): ')

            '''Now we are gonna ask to the client how many money'''
            try:
                money = float(input('Choose the quantity of money you want to make the {}: '
                                              .format(str_operation)))
            except ValueError:
                print('\nYou have to introduce a number to specify the amount of money\n')

            obj_bank.operation(str_operation, money)
            print(obj_bank)

        except Exception as e:
            print(e)
