import re
from SPARQLWrapper import SPARQLWrapper, JSON

class SparqlQuery:

    def __init__(self, query = None):
        self.__query = query
        self.sparql = SPARQLWrapper("http://dbpedia.org/sparql")

        self.__namespaces = \
"""
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
PREFIX Category: <http://dbpedia.org/resource/Category:>
"""

    def query(self, sub = False):

        if (self.__query == None or self.__query == ""):
            raise Exception("Sparql: Er is geen vraag gesteld aan het systeem")
        #print self.__namespaces + self.__query

        if sub:
            self.sparql.setQuery(self.__namespaces + self.__query_subcat)
        else:
            self.sparql.setQuery(self.__namespaces + self.__query)

        self.sparql.setReturnFormat(JSON)

        print "Query uitvoeren, even geduld a.u.b. ...\n\n"
        reply = self.sparql.query().convert()

        answer = []
        for entry in reply["results"]["bindings"]:
            answer.append(entry["string"]["value"] + " ".join(["" for x in range(50 - len(entry["string"]["value"]))]) + entry["uri"]["value"] + "\n")

        return answer

    def setQueryFromCategory(self, category):
        self.__query_subcat = \
"""
SELECT DISTINCT ?uri ?string
WHERE {
{?subcat skos:broader """+category+""" . ?uri dcterms:subject ?subcat .} UNION { ?uri dcterms:subject """ + category + """ . }
OPTIONAL { ?uri rdfs:label ?string . }
FILTER ( lang(?string) = \'nl\' )
}
"""

        self.__query = \
"""
SELECT DISTINCT ?uri ?string
WHERE {
{ ?uri dcterms:subject """ + category + """ . }
OPTIONAL { ?uri rdfs:label ?string . }
FILTER ( lang(?string) = \'nl\' )
}
"""

        #temporary disabling
        self.__query = None

    def getNamespace(self, name):
        reg = re.compile("(?<="+name+":\s<).+(?=>)")
        match = reg.search(self.__namespaces)
        if match:
            return match.group()

