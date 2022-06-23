import yaml
import sys
import xml.etree.ElementTree as ET

def xmlout(dictionary, root, fout=sys.stdout, node_type=None, list_dict={}):

    if isinstance(dictionary, dict):
        for key, value in dictionary.items():
            # Fix items..
            if value is None:
                value = ""
            elif isinstance(value, (float, int)):
                value = str(value)
            elif isinstance(value, bool):
                value = str(value).lower()

            if isinstance(value, list):
                xmlout(value, root, fout=sys.stdout, node_type=key[:-1])
            elif isinstance(value, dict):
                root = ET.SubElement(root, key)
                xmlout(value, root, fout=sys.stdout)
            elif isinstance(value, str):
                if list_dict is not None:
                    list_dict[key] = value
                root.attrib[key] = value.format(**list_dict)
            else:
                raise TypeError(type(value))
    elif isinstance(dictionary, list):
        for value in dictionary:
            if isinstance(value, dict):
                subroot = ET.SubElement(root, node_type)
                xmlout(value, subroot, fout=sys.stdout, list_dict=list_dict)
            else:
                raise TypeError(type(value))

data = yaml.load(open("main.yml", "r"), Loader=yaml.SafeLoader)

root = ET.Element("xdxf")
xmlout(data["xdxf"], root)

from xml.dom import minidom

xmlstr = minidom.parseString(ET.tostring(root)).toprettyxml(indent="  ")
tree = ET.ElementTree(root)
with open("main2.xdxf", "w") as f:
    f.write(xmlstr)
