""" A member of a family """

from person import Person

class Member(Person):
    """ a member of a family """
    def __init__(self, fname, lname, **kwargs):
        super.__init__(fname, lname, **kwargs)
        self.father=None
        self.mother=None
        self.child_list=[]

    def set_father(self, fname, lname, **kwargs):
        self.father=Person(fname, lname, kwargs)

    def set_mother(self, fname, lname, **kwargs):
        self.mother=Person(fname, lname, kwargs)

    def add_child(self, fname, lname, **kwargs):
        self.child_list.append(Person(fname, lname, kwargs))