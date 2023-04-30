""" person """

class Person():
    """ attributes of a person without relation to others """
    def __init__(self, fname, lname, **kwargs):
        self.fname=fname
        self.lname=lname
        self.dob=kwargs.get('dob', None)
        self.dod=kwargs.get('dod', None)
        self.nickname=kwargs.get('nickname', None)
        self.pic_file=kwargs.get('pic_file', None)
        self.birthplace=kwargs.get('birthplace', None)