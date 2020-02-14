import xml.etree.ElementTree as ET

ns = '{http://www.drugbank.ca}'


class api():
    product_list = {}

    def __init__(self):
        self.root = ET.parse('./full database.xml').getroot()

        for tag in self.root.findall(f"{ns}drug"):
            self.product_list[tag.find(f"{ns}name").text] = (
                set([product.find(f"{ns}name").text for product in tag.find(f'{ns}products').findall(f'{ns}product')]))
