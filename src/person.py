""" person """

class Person():
    """ attributes of a person without relation to others """
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
        self.dob=None
        self.nickname=None
        self.picture=None
        self.birthplace=None