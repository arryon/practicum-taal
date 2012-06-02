from SPARQLWrapper import SPARQLWrapper, JSON

sparql = SPARQLWrapper("http://dbpedia.org/sparql")

namespaces = """
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX dbpedia-owl: <http://dbpedia.org/ontology/>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
PREFIX dc: <http://purl.org/dc/elements/1.1/>
PREFIX : <http://dbpedia.org/resource/>
PREFIX dbpedia2: <http://dbpedia.org/property/>
PREFIX dbpedia: <http://dbpedia.org/>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX dcterms: <http://purl.org/dc/terms/>
PREFIX category: <http://dbpedia.org/page/Category:>
"""



queries = [\
"""
SELECT ?result WHERE {
:Winter_Olympic_Games dbpedia2:data ?result .
} LIMIT 1
""",\
"""
SELECT ?result WHERE {
?result dcterms:subject category:Olympic_bronze_medalists_for_Czechoslovakia.
} LIMIT 10
""",\
"""
SELECT ?result WHERE {
?result skos:broader category:Summer_Olympics_events_by_year.
} LIMIT 10
""",\
"""
SELECT ?result WHERE {
:1992_Winter_Olympics dbpedia2:stadium ?result.
}
""",\
"""
SELECT ?result WHERE {
:1896_Summer_Olympics dbpedia-owl:numberOfParticipatingNations ?result.
}
"""]


entry =  """Voer een van de vijf vragen als query uit:
1. In welk jaar zijn de eerste olympische winterspelen gehouden?
2. Wanneer zijn de olympische zomerspelen gehouden?
3. Wie hebben er allemaal bronzen medailles gewonnen voor Tsjecho-Slowakije?
4. In welk stadion vond de opening plaats van de winterspelen van 1992?
5. Hoeveel landen deden er mee aan de eerste olympische zomerspelen?
(voer 'q' in om te stoppen)"""


print entry
num = raw_input("voer door [1-5] in te toetsen een van de queries uit...\n")

while (num != 'q'):
    num = int(num)
    if (num > 5):
        print "query is hoger dan 5, zet op 5"
        num = 5

    print "\nQuery", num, ": \n"

    print queries[num-1]
    sparql.setQuery(namespaces + queries[num-1])
    sparql.setReturnFormat(JSON)

    results = sparql.query().convert()

    for result in results["results"]["bindings"]:
        if (result["result"]["value"] == ""):
            print "Geen resultaat"
        else:        
            print "Antwoord: ", result["result"]["value"]

    print "\n\n", entry
    num = raw_input("voer door [1-5] in te toetsen een van de queries uit...'\n")
