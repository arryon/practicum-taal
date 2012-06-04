from alpino_query import AlpinoQuery, SentStruct

sentence = raw_input("Geef een zin op voor Alpino om te parsen: \n")

aq = AlpinoQuery()

while sentence != 'q':
    
    aq.setSentence(sentence)
    aq.query()

    print aq.getXML()
    print aq.getSentenceType()
    match = raw_input("Geef een XPath voor deze in op. Voer 'q' in om te stoppen: \n")

    while match != 'q':
        ne = aq.named_entities(match)
        print "length: ", len(ne)
        match = raw_input("Geef een XPath voor deze in op. Voer 'q' in om te stoppen: \n")

    sentence = raw_input("Geef een zin op voor Alpino om te parsen: \n")

    
