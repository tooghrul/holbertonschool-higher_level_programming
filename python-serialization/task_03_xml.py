#!/usr/bin/python3


import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    """
    Serializes a Python dictionary into an XML file.
    """
    # Create the root element <data>
    root = ET.Element("data")

    # Iterate through dictionary items and create child elements
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)  # XML only stores text/strings

    # Create the tree and write it to the file
    tree = ET.ElementTree(root)
    try:
        tree.write(filename, encoding='utf-8', xml_declaration=True)
        return True
    except Exception:
        return False

def deserialize_from_xml(filename):
    """
    Reads an XML file and reconstructs it into a Python dictionary.
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        # Reconstruct the dictionary from child elements
        # Note: All values will be returned as strings by default
        return {child.tag: child.text for child in root}
    except FileNotFoundError:
        return None
    except ET.ParseError:
        return None
