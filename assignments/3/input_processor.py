import re
import csv
import editdist

class InputProcessor:

    question_types = [\
    ("list", re.compile("^(noem|geef)\s(een|de|alle)?\s?(lijst|overzicht|namen|voorbeelden)?\s?(van|met)?")),\
    ("list", re.compile("(lijst|\w+)\svan")),\
    ("question", re.compile("^(waar\sover|hoe\slang|hoe\sveel|wie|wat|waar|wanneer|hoe|waarom)(\s(is|zijn))?"))]

    inflection_types = [\
    ("s", re.compile("s\Z"), ""),\
    ("ese", re.compile("ese\Z"), "ees"),\
    ("enen", re.compile("(?<=[^eoua])[eoua][^eoua]en\Z"), None),\
    ("inen", re.compile("(?<=[^eouai])i[^eouai]en\Z"), None),\
    ("oenen", re.compile("(oe|ou|ui)nen\Z"), {"oenen":"oen", "ounen":"oun", "uinen":"uin"}),\
    ("e", re.compile("(?<=[^eaoui][^eaoui])e\Z"), ""),\
    ("ien", re.compile("ien\Z"), "")]


    def __init__(self):

            #initialize variables in case the get_input function is called before process_input
        self.__input_raw = None
        self.__input_filtered = None
        self.__words = []

            #process the Wikipedia categories file for translation purposes
        self.process_CSV_file('category_page_translation.csv')

    def process_input(self):
        self.__input_raw = raw_input("Stel een vraag over de Olympische Spelen:\n")
        self.__input_filtered = self.__input_raw.lower()
        self.__words = [word.strip() for word in self.__input_filtered.split(' ')]

    def query_from_input(self):
        
        if (self.__input_raw == None or self.__input_raw == ""):
            raise Exception("Processor: Er is geen vraag gesteld aan het systeem (lege input ontvangen)")

        relevant = self.extract_relevant_part().capitalize()
        print relevant
        print self.generate_variations(self.to_array(relevant))

#--------------------------
# PRIVATE FUNCTIONS
#--------------------------
 
    def generate_variations(self, words):
        variations = []

        for word in words:
            variations.append((word ,[word]))
            #match against inflection types
            for _type in self.inflection_types:
                match = _type[1].search(word)
                if match:
                    variations[-1][1].append(self.do_inflection(word, match.group(), _type))


    def do_inflection(self, word, match, _type):
        #return the inflection based on the inflection replacement type

        #if the replacement is a string, return the substring without the
        #matched sequence at the end, plus the defined replacement
        if type(_type[2]).__name__ == "str":
            return word[:-len(match)] + _type[2]

        #if the replacement is a dictionary, we must return the substring without
        #the matched sequence, plus the value of the 'match' key
        elif type(_type[2]).__name__ == "dict":

            return word[:-len(match)] + _type[2][match]

        #if the replacement is None, it is of another kind, and we must do something creative
        elif type(_type[2]).__name__ == "NoneType":
            if _type[0] == "inen":
                return word[:-len(match)] + "ien"
            elif _type[0] == "enen":
                postfix = match[0]+match[0]+match[1]
                return word[:-len(match)] + postfix

    def extract_relevant_part(self):
        # match the lowercase input against each of the regex entries
        for regex in self.question_types:
            match = regex[1].match(self.__input_filtered)
            if match:
                # get the rest of the sentence after the match (probably the category or page name)
                relevant = self.__input_raw[match.end():len(self.__input_raw)].strip()
                # check for interpunction at the end
                if re.compile("\w\Z").match(relevant[-1]) == None:
                    return relevant[:-1]
                else:
                    return relevant

        # no match was found
        raise Exception("Geen vraagzin constructie gevonden in de ingevoerde vraag")


#-----------------------------------------
# AUXILIARY FUNCTIONS, GETTERS AND SETTERS
#-----------------------------------------


    # get_input returns input specified by the modifier
    # return statement works as a case-switch
    def get_input(self, mod):
        return {\
        "raw"       : self.__input_raw,\
        "filtered"  : self.__input_filtered,\
        "words"     : self.__words }[mod]

    def process_CSV_file(self, filename):
        self.__csv = csv.reader(open(filename, 'rb'), delimiter="#")

        # put the entries into a dictionary
        self.__nl2en = {}
        for row in self.__csv:
            self.__nl2en[row[0]] = row[1]

    def to_array(self, string):
        return [word.strip() for word in string.split(' ')]
