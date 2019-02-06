from abc import ABC, abstractmethod


class Bank(ABC):

    def __init__(self, commision, amount_of_pay):
        self._commision = commision
        self._amount_of_pay = amount_of_pay

    @abstractmethod
    def abs_method(self):
        pass
