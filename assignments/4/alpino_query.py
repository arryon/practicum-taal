#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import socket
from  lxml import etree

class AlpinoQuery:
    host = "vingolf.let.rug.nl"
    port = 42424

    sentence = ""
    xml = ""
    
    def __init__(self, sentence = None):
        self.sentence = sentence

    def query(self):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((self.host,self.port))
        self.sentence += "\n\n"
        s.sendall(self.sentence)

        total_xml= ""
        while True:
            xml = s.recv(8192)
            if not xml:
                break
            total_xml += str(xml)
        print total_xml
        xml = etree.fromstring("".join(total_xml))
        print xml
        print total_xml
        
        self.etree = xml
        self.xml = total_xml

    def named_entities(self, xml, string = None):
        if string:
            named_entities = xml.xpath(string)
        else:
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

#-----------------------------------------
# AUXILIARY FUNCTIONS, GETTERS AND SETTERS
#-----------------------------------------

    def getEtree(self):
        return self.etree

    def getXML(self):
        return self.xml

    def setSentence(self, sentence):
        self.sentence = sentence

