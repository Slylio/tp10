class Person():
    def __init__(self, nom, prenom,numero):
        """
        Creates an instance of class TableCell
        input   -- self : instance of class TableCell
                -- k : key of the TableCell
                -- v : value of the TableCell
        """
        self.nom = nom
        self.prenom = prenom
        self.numero = numero
    def __str__(self) -> str:
        return self.prenom+" "+self.nom+" : "+str(self.numero)