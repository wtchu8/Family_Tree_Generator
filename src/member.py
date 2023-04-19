""" persons relationship with others """

from person import Person

class Member(Person):
    """ a person's relationship to others """
    def __init__(self,fname,lname):
        super.__init__(fname,lname)
        self.father=None
        self.mother=None
        self.child_list=[]

    def set_father(self,fname,lname):
        self.father=Person(fname,lname)

    def set_mother(self,fname,lname):
        self.mother=Person(fname,lname)

    def add_child(self,fname,lname):
        self.child_list.append(Person(fname,lname))