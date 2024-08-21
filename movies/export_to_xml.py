# write data to a xml file

import xml.etree.ElementTree as ET


personen: dict = {
				"persoon1":
					{"nummer":1,"voornaam":"bugs","achternaam":"bunny"},
				"peroon2":
					{"nummer":2,"voornaam":"daffy","achternaam":"duck"}
				}

for i in personen:
	print(i)
	print(personen[i])
	

def data_to_xml():

	data = ET.Element("personen");

	editor = ET.Element("editor", role = "admin")
	editor.text = "somebody"

	data.append(editor)

	el_persoon = ET.SubElement(data, "persoon1")

	el_nummer = ET.SubElement(el_persoon, "nummer")
	el_voornaam = ET.SubElement(el_persoon, "voornaam")
	el_achternaam = ET.SubElement(el_persoon, "achternaam")

	el_nummer.text = "1"
	el_voornaam.text = "bugs"
	el_achternaam.text = "bunny"

	byte_xml = ET.tostring(data)


	return byte_xml


def indent(elem, level=0):
   # Add indentation
   indent_size = "    "
   i = "\n" + level * indent_size
   if len(elem):
      if not elem.text or not elem.text.strip():
         elem.text = i + indent_size
      if not elem.tail or not elem.tail.strip():
         elem.tail = i
      for elem in elem:
         indent(elem, level + 1)
      if not elem.tail or not elem.tail.strip():
         elem.tail = i
   else:
      if level and (not elem.tail or not elem.tail.strip()):
         elem.tail = i


def pretty_print_xml_elementtree(xml_string):
   # Parse the XML string
   root = ET.fromstring(xml_string)

   # Indent the XML
   indent(root)

   # Convert the XML element back to a string
   pretty_xml = ET.tostring(root, encoding="unicode")

   # Print the pretty XML
   return pretty_xml


if __name__ == "__main__":  
    
	data = data_to_xml()

	out = pretty_print_xml_elementtree(data)


	with open("xml_export.xml", "w", encoding="UTF8") as xml_file:
	    xml_file.writelines('<?xml version="1.0" encoding="UTF-8"?>\n' + out)