from alpino_query import AlpinoQuery

sentence = ""

aq = AlpinoQuery()


while sentence != 'q':
    sentence = raw_input("Geef een zin op voor Alpino om te parsen: \n")
    aq.setSentence(sentence)
    aq.query()

    xml = aq.getEtree()
    print xml

    print aq.named_entities(xml, "//node[@pos='name']")
    print aq.tree_yield(xml)

    
