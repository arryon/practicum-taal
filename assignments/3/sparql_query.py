from SPARQLWrapper import SPARQLWrapper, JSON

class SparqlQuery:

    def __init__(self, query = None):
        self.__query = query
        self.__sparql = SPARQLWrapper("http://dbpedia.org/sparql")

        self.__namespaces = """
        PREFIX owl: <http://www.w3.org/2002/07/owl#>
        PREFIX dbpedia-owl: <http://dbpedia.org/ontology/>
        PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX foaf: <http://xmlns.com/foaf/0.1/>
        PREFIX dc: <http://purl.org/dc/elements/1.1/>
        PREFIX : <http://dbpedia.org/resource/>
        PREFIX property: <http://dbpedia.org/property/>
        PREFIX dbpedia: <http://dbpedia.org/>
        PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
        PREFIX dcterms: <http://purl.org/dc/terms/>
        PREFIX category: <http://dbpedia.org/resource/Category:>
        """

    def query(self):

        if (self.__query == None or self.__query == ""):
            raise Exception("Sparql: Er is geen vraag gesteld aan het systeem")

        #temporary handler to assure that up until here, everything works fine
        if (self.__query == "works"):
            raise Exception("Er is nog geen werkende query")

        self.__sparql.setQuery(self.__namespaces + self.__query)
        self.__sparql.setReturnFormat(JSON)

        return self.__sparql.query().convert()

    def setQuery(self, query):
        self.__query = query
