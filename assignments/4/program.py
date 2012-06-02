# coding: utf-8
#import other classes
import input_processor
import sparql_query
import sys

from input_processor import InputProcessor
from sparql_query import SparqlQuery        

class Program:

    def __init__(self):
        self.__processor = InputProcessor()
        self.__sparqlQuery = SparqlQuery()

    def run(self):
        print "Welkom bij de DBPedia Olympische Spelen vragensteller.\nToets 'q' en druk op enter om te stoppen.\n"

        self.__processor.process_input()

        while (self.__processor.get_input("raw") != 'q'):
 
            try:
                category = self.__processor.category_from_input()
                #print the category and it's link
                output = category + " ".join(["" for x in range(50 - len(category))]) + "http://dbpedia.org/resources/" + category
                dashes = len(output) * '-'
                print "\n\n" + dashes + "\n" + output + "\n" + dashes + "\n\n"
                
                self.__sparqlQuery.setQueryFromCategory(category)
                answer = self.__sparqlQuery.query()
            
                if answer:
                    self.print_answer(answer)
                else:
                    print "Geen antwoord gevonden, opnieuw zoeken met subcategorieën..."
                    answer = self.__sparqlQuery.query(True)
                    if answer:
                        self.print_answer(answer)
                    else:
                        print "Helaas, er kon geen antwoord op de vraag gevonden worden. Probeer het nog eens."
                
            except Exception as error:
                print "\n-------------------\nEr is een fout opgetreden:"
                print error.args[0]
                print "-------------------\n"

            self.__processor.process_input()

    def print_answer(self, answer, recurse = False):
        cont = "y"
        if len(answer) // 50 == 0:
            print "".join(answer)
        else:
            if not recurse:
                print "Meer dan 50 antwoorden. Print eerste 50:\n"
            print "".join(answer[:50])
            cont = raw_input("Druk op een toets om door te gaan. Toets 'n' en druk op enter om af te breken. Druk 'q' om te stoppen.\n")
            if cont == 'n':
                return
            if cont == 'q':
                sys.exit()
            self.print_answer(answer[51:], True)


program = Program()
program.run()
