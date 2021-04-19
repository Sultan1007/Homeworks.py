class BankAccount:
    NAME = 10

    def __init__(self, number, balance):
        self._number = number
        self._balance = balance


    @property
    def number(self):
        return f"Number: {self._number}"

    @number.setter
    def number(self, number):
        self._number = number

    @property
    def balance(self):
        return f"Account balance: {self._balance}"

    # (Функция) Name невозможно изменить
    def __setattr__(self, key, value):
        if key == "NAME":
            raise AttributeError
        else:
            self.__dict__[key] = value

    @balance.setter
    def balance(self, balance):
        if balance < 0:
            raise ValueError("Error")
        self._balance = balance


account = BankAccount(1, 90)
# account._balance = -10000
account._number = 10
account._balance = 1000
print(account.number)
print(account.balance)
# Если раскоментить снизу, то произойдет ошибка
# account.NAME = 10