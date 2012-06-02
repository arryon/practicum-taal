#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import socket
from  lxml import etree

# parse input sent and return alpino output as an xml element tree
def alpino_parse(sent, host='vingolf.let.rug.nl', port=42424):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((host,port))
    sent = sent + "\n\n"
    s.sendall(sent)
    total_xml= ""
    while True:
        xml = s.recv(8192)
        if not xml:
            break
        total_xml += str(xml)
    print total_xml
    xml = etree.fromstring("".join(total_xml))
    return xml

# extract named entities from xml and return as list of strings
def named_entities(xml, xpath = None):

    named_entities = xml.xpath('.//node[(@cat="mwu" and node[@pos="name"]) or (@pos="name" and not(@rel="mwp"))]')

    ne_list = []
    for ne in named_entities :
        ne_list.append(tree_yield(ne))
    return ne_list

    
def tree_yield(xml):
    leaves = xml.xpath('descendant-or-self::node[@word]')
    words = []
    for l in leaves :
        words.append(l.attrib["word"])
    return " ".join(words)
    
def main():
    sentence=raw_input("Geef de zin die Alpino moet analyseren: ")
    #print("zin gelezen: {}".format(sentence))
    xml =alpino_parse(sentence)
    names = named_entities(xml)
    print names
    for name in names :
        print(name)
    
if __name__ == '__main__':
    main()
