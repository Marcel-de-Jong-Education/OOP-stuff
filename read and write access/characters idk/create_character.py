class CreateCharacter:
    def __init__(self, name, classtype, level):
        self.name = name
        self.classtype = classtype
        self.level = level

    def get_name(self):
        return self.name
    
    def get_classtype(self):
        return self.classtype
    
    def get_level(self):
        return self.level
    

    def set_name(self, name):
        self.name = name

    def set_classtype(self, classtype)