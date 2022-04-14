#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" 
Table d'association
Implementation par une liste chainee
Herite des methodes des listes chainees simples
Une cellule contient une donnee (data) et un lien vers la cellule suivante
Data est une TableCell qui contient une valeur (value) et une cle (key) 
"""


import listes as li

class TableCell():
    def __init__(self, k, v):
        """
        Creates an instance of class TableCell
        input   -- self : instance of class TableCell
                -- k : key of the TableCell
                -- v : value of the TableCell
        """
        self.value = v
        self.key = k
        
    def __str__(self):
        """ Returns a string representing the self TableCell
        input   -- self : instance of class TableCell
        output  -- string, representation of the self TableCell
        """
        return "(" + str(self.key) + " : " + str(self.value) + ")"

class Table(li.Liste):
    """
    The class Table represents an association table ; it is implemented by a list of chained elements
    [(key,value)] associating for each element of the list a value to a key.
    """  
    def __init__(self):
        """ Create an instance of class Table
        output   -- self
           postcond: creates an empty table
        """
        super().__init__()
        
    def __str__(self):
        """
        Returns a string representing Table self
        input   -- self : instance of class Table
        output  -- string
        """
        if self.empty_table():
            return '[]'
        else:
            result = ''
            current = self.head()
            while current.next != None:
                result = result + str(current.data) + ','
                current = current.next
            result = result + str(current.data) 
        return '[' + result + ']'
      
    def empty_table(self):
        """
        Return True if the table self is empty and 
        False otherwise
        input   -- self : instance of class Table
        output  -- b: bool
            postcond: b est True ssi self is empty
        """
        return self.is_empty_list()
    
    def print_values(self):
        """
        Returns a string representing the list of the values of the elements 
        of the table self
        input   -- self : instance of class Table
        output  -- string
        """    
        if self.empty_table():
            return '[]'
        else:
            result = ''
            current = self.head()
            while current.next != None: 
                result = result + str(current.data.value) + ','
                current = current.next
            result = result + str(current.data.value) 
        return '[' + result + ']'
            
    def print_keys(self):
        """
        Returns the list of the keys of the elements 
        of the table self
        input   -- self : instance of class Table
        output  -- string
        """      
        if self.empty_table():
            return '[]'
        else:
            result = ''
            current = self.head()
            while current.next != None:
                result = result + str(current.data.key) + ','
                current = current.next
            result = result + str(current.data.key) 
        return '[' + result + ']'
        
    def put(self,k, v):
        """
        Modifies the element of key k et value v: if the element of key k exists, change its value by v ; 
        if the element does not exist, insert it at the end of the table
        input   -- self : instance of class Table
        output  -- self in which the element (k,v) has been modified or inserted
        """
        elt=self.get_elt(k)
        if elt != None:
            elt.data.value = v
        else :
            new = TableCell(k,v)
            self.insert_last(new)

    def get_value(self,k):
        """
        Searches the element of key k et returns its value
        input   -- self : instance of class Table
        output  -- v: object, valeur of the element of key k
                   of the table self
        """
        elt = self.get_elt(k)
        if elt != None:
            return elt.data.value 
        else: 
            return None

    def remove(self,k):
        """
        Removes the element of key k et returns self in which the element has been removed
        input   -- self : instance of class Table
        output  -- v: object, valeur of the element of key k
                   of the table self
        """
        elt=self.get_elt(k)
        if elt != None:
            self.delete_value(elt)
        return self
        
    def get_elt(self,k):
        """
        Searches the element of key k 
        input   -- self : instance of class Table
        output  -- e: TableCell whose key is k
        """
        elt=self.mfirst
        count=0
        while count<self.length(): #tester <=
            if elt.data.key == k:
                return elt.data
            count+=1
            elt=elt.next
        return None

if __name__ == "__main__":
    print("Hello Table !!!")    
      

