__author__ = 'cxa70'

import Ch1
import xml.etree.cElementTree as et
import sqlite3 as sql
import XmlNode


def showElements(element, indent, is_root):
    sz = len(element)
    ind = indent
    if is_root:
        ind = 0
    if sz > 0:
        print(" "*ind + "Name: " + element.tag)
        for ele in element:
            showElements(ele, indent*2, False)
    else:
        print(" "*indent + element.tag + ": " + element.text)


def print_sections(section, indent):
    idt = indent
    if section.IsRoot:
        idt = 0

    print(" "*idt + section.Name + "(" + section.Value + ")")

    if section.has_values():
        for val in section.Values:
            print(" "*indent*2 + val.Name + ":    " + val.Value)

    if section.has_sections():
        for sec in section.Sections:
            print_sections(sec, indent*2)





xdoc = et.parse('RRV-CINCToDSHRequestSample1.xml')
root = xdoc.getroot()

doc = XmlNode.Section()
doc.IsRoot = True
doc.build_from_etree(root)

print_sections(doc, 2)
