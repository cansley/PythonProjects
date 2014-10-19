__author__ = 'cxa70'
import re

class Section:
    def __init__(self):
        self.Sections = []
        self.Values = []
        self.Attributes = []
        self.IsRoot = False
        self.Name = ""
        self.Value = ""
        self.Namespace = ""

    def has_sections(self):
        return len(self.Sections) > 0

    def has_values(self):
        return len(self.Values) > 0

    def _build_attribs(self, attribs):
        for attrib in attribs.keys():
            new_attrib = Attribute()
            new_attrib.Name = attrib
            new_attrib.Value = attribs[attrib]
            self.Attributes.append(new_attrib)

    def build_from_etree(self, etree):
        regex = re.compile("{(.*)}(.*)")
        r = regex.search(etree.tag)
        if len(r.groups()) > 0:
            self.Name = r.groups()[1]
            self.Namespace = r.groups()[0]
        else:
            self.Name = etree.tag.strip()

        self.Value = etree.text.strip()
        if len(etree.attrib) > 0:
            self._build_attribs(etree.attrib)

        if len(etree) > 0:
            for ele in etree:
                child = Section()
                child.build_from_etree(ele)
                if child.has_values():
                    self.Sections.append(child)
                else:
                    self.Values.append(child)



class Value:
    def __init__(self):
        self.Name = ""
        self.Value = ""


class Attribute:
    def __init__(self):
        self.Name = ""
        self.Value = ""