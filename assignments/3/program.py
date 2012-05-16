#import other classes
import input_processor
import sparql_query

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
                self.__sparqlQuery.setQuery(self.__processor.query_from_input())
                answer = self.__sparqlQuery.query()
            
                print answer
                
            except Exception as error:
                print "\n-------------------\nEr is een fout opgetreden:"
                print error.args[0]
                print "-------------------\n"

            self.__processor.process_input()



program = Program()
program.run()
