from alpino_query import AlpinoQuery, SentStruct

print "question: ", SentStruct.POEP

sentence = raw_input("Geef een zin op voor Alpino om te parsen: \n")

aq = AlpinoQuery()

while sentence != 'q':
    
    aq.setSentence(sentence)
    aq.query()

    print aql.getXML()

    match = raw_input("Geef een XPath voor deze in op. Voer 'q' in om te stoppen: \n")

    while match != 'q':
        print aq.named_entities(match)
        match = raw_input("Geef een XPath voor deze in op. Voer 'q' in om te stoppen: \n")

    sentence = raw_input("Geef een zin op voor Alpino om te parsen: \n")

    
