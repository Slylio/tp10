from msilib.schema import tables
import table as ta
import person as per
class Annuaire(ta.Table):
    def __init__(self):
        self.table=ta.Table()
    
    def __str__(self):
        return str(self.table)
    
    """
    Ajoute un object de type personne a l'annuaire
    clef : Prenom+InitialNom
    value : Person
    """    
    def addPerson(self,key,person):
        self.table.put(key,person)