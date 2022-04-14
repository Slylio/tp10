#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Cell(object):
    """ The class Cell represents an element of the list. It contains 2 attributes: a data of type object and a link to the next element
    """ 
    def __init__(self):
        """ Creates an instance of class Cell
        input   -- self : instance of class Cell
        """
        self.data = object
        self.next = None
        
    def __str__(self):
        """ Returns a string representing the self Cell
        input   -- self : instance of class Cell
        output  -- string, representation of the self cell
        """
        result = str(self.data) + ', next:'
        if self.next == None:
            result += 'None'
        else:
            result += str(self.next.data)
        return '{ ' + result + ' }'

class Liste(object):
    """ The class Liste allows to represent a list from chained elements of type Cell. Each element of the 
    list contains a value and a pointer towards the next element. """
    
    def __init__(self):
        """Creates an instance of class Liste
        input   -- self : instance of class Liste
                    set the first element to None, and the size of the list to 0
        """
        self.mfirst = None
        self.size = 0

    def is_empty_list(self):
        """ Returns True if and only if Liste self is empty
        input   -- self : instance of class Liste
        output  -- v : bool
        """
        v = (self.mfirst == None)
        return v
    
    def __str__(self):
        """ Returns a string representing Liste self
        input   -- self : instance of class Liste
        output  -- string
        """     
        if self.is_empty_list():
            return '[]'
        else:
            result = ''
            current = self.head()
            # Parcours des elements de la liste (self)
            while current.next != None: # on s'arrete a l'avant dernier
                result = result + str(current.data) + ','
                current = current.next
            #dernier element
            result = result + str(current.data) 
        return '[' + result + ']'
    
    def length(self):
        """ Returns the lenght of the list
        input   -- self : instance of class Liste
        output  -- n : int
        """
        n = self.size
        return n
    
    def head(self):
        """ Returns the first element of the list (of type Cell)
        input   -- self : instance of class Liste
                pre-cond: self n'est pas vide
        output  -- p : element of type Cell
        """
        if self.mfirst == None:
            print("empty list")
        else:
            p = self.mfirst
            return p
        
    def first_value(self):
        """ Returns the value of the first element of the list of type object
        input   -- self : instance of class Liste
                pre-cond: self is not empty
        output  -- v : value of type object
        """
        if self.mfirst == None:
            print("liste vide")
        else:
            v = self.mfirst.data
            return v
        
    def insert_first(self, v):
        """ Inserts the value v at the head of the list
        input   -- self : instance of class Liste
                -- v : value of type object to insert at the first position
        output  -- self in which the element of value v has been inserted at the head of the list
                    the size of the list is updated
        """
        m = Cell()
        m.data=v
        if self.mfirst == None:
            m.next = None
        else:
            m.next=self.mfirst
        self.mfirst = m
        self.size += 1
        
    def insert_at(self,v,i):
        """ Returns the list in which the element of value v has been inserted at index i
        input   -- self : instance of class Liste
                -- v : value of type object to insert
                -- i : int index at which the element of value v is inserted
                    exception when the index i is too small or too big
        output  -- self in which the element of value v has been inserted at index i of the list
                    the size of the list is updated
        """
        if i < 0:
            raise ValueError('Error : incorrect index')
        else:
            # Creation d'une cellule de data v
            m = Cell()
            m.data = v
            # Si i == 0, insertion en tete de self
            if i == 0:
                self.insert_first(v)
            else:
                # Pointeur en debut de liste
                current = self.mfirst
                # On se deplace sur la liste pour trouver l'endroit ou inserer
                while i !=1:
                    current= current.next
                    i = i - 1
                temp = current.next
                current.next = m
                m.next = temp
                self.size += 1

    def insert_last(self,v):  
        """ Inserts the value v at the end of the list
        input   -- self : instance of class Liste
                -- v : value of type object to insert at the last position
        output  -- self in which the element of value v has been inserted at the end of the list
                    the size of the list is updated 
        """
        i = self.length()
        if i == 0:
            self.insert_first(v)
        else:
            self.insert_at(v,i)
        
    def delete_value(self,v):
        """ Returns the list in which the element of value v i has been deleted
        input   -- self : instance of class Liste
                -- v : value of type object
        output  -- self in which the element of value v has been deleted
                    the size of the list is updated 
        """
        if self.is_empty_list():
            raise ValueError('La liste est vide')
        else:
            current = self.mfirst
            # Si la liste ne contient qu'un seul element
            if current.data == v:
                self.mfirst = current.next
                self.size -=1
            else:
                while current.data != v and current.next != None:
                    previous = current
                    current= current.next
                if current.data == v:
                    # suppression du dernier element
                    if current.next == None:
                        previous.next=None
                        self.size -= 1
                    #suppression de l'element e dans la liste
                    else:
                        previous.next=current.next
                        self.size -= 1
                            
    def get_at(self,i):
        """ Returns the element of the Liste self at index i
        input   -- self
                -- i : int (index of the searched element) 
        output  -- element of type Cell 
        """
        if i < 0 or i >= self.size:
            return None
        else:
            current = self.head() # start at the first cell
            idx = 0
            while idx  < i:  
                current = current.next
                idx += 1
            return current
                
    def get_value(self,i):
        """ Returns the value of the element of the liste at index i
        input   -- self
                -- i : int (index of the searched element) 
        output  -- v : object 
        """    
        c = self.get_at(i)
        if c == None:
            return None
        else:
            return c.data
    
    def map(self,f):
        """ Applies function f to each value of Liste self
        input   -- self : instance of class Liste
                -- f : function
        output  -- lmap: new Liste in which each value has been modified by function f
                    self is not modified
        """  
        n = self.size
        lmap = Liste()
        for i in range(n):
            v = f(self.get_value(i))
            lmap.insert_last(v)
        return lmap 
    
    def count(self, v):
        """ Counts the number of occurrences of v in Liste self
        input   -- self : instance of class Liste
                -- v : object
        output  -- int : number of times v occurs in Liste self
        """  
        n = self.size
        compt = 0
        for i in range(n):
            if v == self.get_value(i):
                compt += 1
        return compt
        
    def filter(self, f):
        """ Returns the list of the elements x of Liste self that verify f(x) = True
        input   -- self : instance of class Liste
                -- f : function
                pre-cond: verify that f returns True or False
        output  -- lfilter: new Liste of elements whose values verify f(x) = True
        """      
        n = self.size
        lfilter = Liste()
        lfilter.size=0
        for i in range(n):
            v = self.get_value(i)
            if not f(v):
                lfilter.insert_last(v)
        return lfilter   
    
    def reduce(self, f,x):
        """ Returns the value obtained by applying the function f(x,y) to each value y of Liste self
        input   -- self : instance of class Liste
                -- f : function
                -- x : initial value of type object
        output  -- final value of type object
        """         
        n = self.size
        y = self.get_value(0)
        x = f(x,y)
        for i in range(1,n):
            x = f(x,self.get_value(i))
        return x  
        
if __name__ == "__main__":
    print("Hello Liste !!!")