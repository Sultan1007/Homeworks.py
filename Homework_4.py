class BankAccount:
    Name = "Name"
    def __init__(self, number, balance):
        self._number = number
        self._balance = balance

    def __set__(self, num, balance):
        self._num = num
        self._balance = balance

    def __get__(self, num, balance):
        self._num = num
        self._balance = balance

    def __setattr__(self, key, value):
        if key == "Name":
            raise AttributeError
        else:
            self.__dict__[key] = value


account = BankAccount(1, 90)
account._balance = -9999
BankAccount.Name = 1
# Cчет пользователя {self._balance}
print(account._number)
print(account._balance)