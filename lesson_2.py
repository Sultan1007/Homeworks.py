class Human:

    def __init__(self, skin_color, name, language):
        self.skin_color = skin_color
        self.name = name
        self.language = language

    def eat(self):
        return f"{self.name}, I'm eating"


class Kyrgyz(Human):

    def __init__(self, skin_color, name, language, revolutions):
        super(Kyrgyz, self).__init__(skin_color, name, language)
        self.revolutions = revolutions

    def function(self):
        return self.name, self.language, self.revolutions


a = Kyrgyz("asd", "nanm", "dslkc", "dsfknlw")
print(a.function())
