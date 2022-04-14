
import annuaire
import person
annuaireTest=annuaire.Annuaire()
personTest1=person.Person("Raimond", "Emilio", "065656565656")
personTest2=person.Person("Dupont","Nico","123456")
personTest3=person.Person("Oste","Jacques","999999")
annuaireTest.addPerson("EmilioR",personTest1)
annuaireTest.addPerson("NicoD",personTest2)
annuaireTest.addPerson("JacquesO",personTest3)

print("First value : "+str(annuaireTest.table.first_value()))
print("Element (key:EmilioR) : "+str(annuaireTest.table.get_elt("EmilioR")))
print(annuaireTest)