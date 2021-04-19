class BankAccount:

    def init(self, name, balance):
        self._name = name
        self._balance = balance

    @property
    def name(self):
        return f"My account's number {self._name}"

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def balance(self):
        return f"user account: {self._balance} Euro"

    # @name.setter
    # def name(self, name):
    #     if name == "name":
    #         raise ValueError("System error!")
    #     self._name = name

    @balance.setter
    def balance(self, balance):
        if balance < 0:
            raise ValueError("System error!")
        self._balance = balance


account = BankAccount()
account.name = 12859315
print(account.name)
account.balance = 1000000000
print(account.balance)