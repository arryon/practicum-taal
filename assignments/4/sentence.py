class SentStruct:
    QUESTION = "question"
    QUANTITY = "qty"
    WHO = "who"
    WHAT = "what"
    DATE = "when"
    LOC = "where"
    UNKNOWN = "?"

class Sentence(object):
    original = ""
    modified = ""

    _type = [SentStruct.UNKNOWN]

    def __init__(self, sentence = None):
        self.original = sentence

    def getOriginal(self):
        return self.original

    def setOriginal(self, sentence):
        self.original = sentence

    def getModified(self):
        return self.modified

    def setModified(self, sentence):
        self.modified = sentence

    def setType(self, newtype):
        self._type = [newtype]

    def addType(self, _type):
        self._type.append(_type)
        if self._type[0] == SentStruct.UNKNOWN:
            self._type.pop(0)

    def getTypes(self):
        return self._type

    def addToModified(self, append):
        self.modified += append
