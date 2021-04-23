class Catel:

    def __init__(self, nume, varsta=2, greutate=15, culoare="negru"):
        self.nume = nume
        self.varsta = varsta
        self.greutate = greutate
        self._culoare = culoare

    def spune_woof(self):
        if self.varsta < 5:
            print("Woof")
        elif self.varsta >= 5:
            print("Woof..lene")


c1 = Catel("Pablo")
c2 = Catel("Scooby", 5, 30, "maro")
c1.spune_woof()
c2.spune_woof()

