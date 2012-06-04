#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import socket
import sentence
from sentence import SentStruct, Sentence
from  lxml import etree


class AlpinoQuery:
    host = "vingolf.let.rug.nl"
    port = 42424

    sentence = ""
    xml = ""

    
    
    def __init__(self, sentence = None):
        self.sentence = Sentence(sentence)

    def query(self):
        sentence = self.sentence.getOriginal()

        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((self.host,self.port))
        sentence += "\n\n"
        s.sendall(sentence)

        total_xml= ""
        while True:
            xml = s.recv(8192)
            if not xml:
                break
            total_xml += str(xml)
        xml = etree.fromstring("".join(total_xml))
        
        self.etree = xml
        self.xml = total_xml

    def named_entities(self, string = None, xml = None):
        if not xml:
            xml = self.etree


        if string:
            named_entities = xml.xpath(string)
        else:
                #return the proper nouns
            named_entities = xml.xpath("//node[@pos='name']")

        ne_list = []
        for ne in named_entities :
            ne_list.append(self.tree_yield(ne))
        return ne_list

        
    def tree_yield(self, xml):
        leaves = xml.xpath('descendant-or-self::node[@word]')
        words = []
        for l in leaves :
            words.append(l.attrib["word"])
        return " ".join(words)

#---------------------------------------------
# FUNCTIONS FOR DETERMINING SENTENCE STRUCTURE
#---------------------------------------------

    def getSentenceType(self):
        #question sentence
        if len(self.named_entities('//node[@cat="whq"]')) > 0:
            self.sentence.addType(SentStruct.QUESTION)
        #quantity sentence
        if len(self.named_entities('//node[contains(@frame, "wh_adjective") and @root="hoeveel"]')) > 0:
            self.sentence.addType(SentStruct.QUANTITY)
        #what
        if len(self.named_entities('//node[contains(@frame, "pronoun") and @wh="ywh" and @root="wat"]')) > 0:
            self.sentence.addType(SentStruct.WHAT)
        #who
        if len(self.named_entities('//node[contains(@frame, "pronoun") and @wh="ywh" and @root="wie"]')) > 0:
            self.sentence.addType(SentStruct.WHO)
        #date
        if len(self.named_entities('//node[@frame="wh_tmp_adverb" and @root="wanneer"]')) > 0:
            self.sentence.addType(SentStruct.DATE)
        #place
        if len(self.named_entities('//node[@frame="er_wh_loc_adverb" and @root="waar"]')) > 0:
            self.sentence.addType(SentStruct.LOC)

        return self.sentence.getTypes()
        
        


#-----------------------------------------
# AUXILIARY FUNCTIONS, GETTERS AND SETTERS
#-----------------------------------------

    def getEtree(self):
        return self.etree

    def getXML(self):
        return self.xml

    def setSentence(self, sentence):
        self.sentence.setOriginal(sentence)
        self.sentence.setType(SentStruct.UNKNOWN)


