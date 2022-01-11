"""testing for exam"""
import xml.etree.ElementTree as ET
import json

class C:

    @staticmethod
    def m(n1, n2):
        """Parse XML data and return families which pass the obj"""
        doc = ET.parse('mockdata.xml')
        families = doc.getroot()
        count = 0
        for family in families:
            if int(family[2][1].text) >= n1 and len(family[3]) >= n2:
                count += 1
        return count

    @staticmethod
    def m1(n1,n2):
        with open('mockdata.json') as file:
            families = json.load(file)
        count = 0
        for i in families:
            if i['wife']['age'] >= n1 and len(i['children']) >= n2:
                count += 1
        return count

    @staticmethod
    def m2(n1):
        with open('mockdata.json') as file:
            families = json.load(file)
        new = []
        for family in families:
            if len(family['children']) >= n1:
                new.append(family)
        with open('mockdata1.json','w') as f:
            json.dump(new, f, indent=3)

print(C.m(40, 2))
print(C.m1(40, 2))
C.m2(2)