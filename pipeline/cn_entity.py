# this is a class to describe an entity data structure which we have as an outcome of the NLP pipeline application

class CNEntity:
    def __init__(self):
        self.text=""
        self.type=""
        self.negation=""
        self.status=""

    def set_attributes(self, text, type, negation, status):
        if text is not None:
            self.text=text
        if type is not None:
            self.type=type
        if text is not None:
            self.negation=negation
        if status is not None:
            self.status=status

    def display_attributes(self):
        print ', '.join("%s: %s" % item for item in vars(self).items())





cne = CNEntity()
cne.set_attributes("a", "b", True, "d")
cne.display_attributes()





