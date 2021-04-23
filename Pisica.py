class Pisica:
    rasa = "birmaneza"

    def __init__(self, nume, culoare = "gri"):
        self.nume = nume
        self._culoare = culoare

    def spune_miau(self):
        print(f"MEOW MEOW. Ma numesc {self.nume}.")

    def get_culoare(self):
        return self._culoare

    def set_culoare(self, new_culoare):
        self._culoare = new_culoare

p1 = Pisica("Leia")
print(p1.nume)
p1.spune_miau()
print(Pisica.rasa)
# print(p1._culoare)
p1.set_culoare("rosie")
print(p1.get_culoare())

