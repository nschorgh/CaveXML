#! /usr/bin/env python3

# This script outputs lon/lat coordinates from CaveXML entries in KML format'

#import xml.etree.ElementTree
import lxml.etree as etree
import cavexml

# Enter name of XML database here
tree = etree.parse('../allcaves-database.xml')

kml_file = "tmp.kml"

excludelist = ['Moon','Mars','Mercury','Venus','Io','Titan']


root = tree.getroot()
rootout = etree.Element("kml")
rootout.set("xmlns", "http://www.opengis.net/kml/2.2")

dd = etree.Element("Document")
rootout.append (dd)

for item in root.findall('record'):
        
    # Find a cave name
    cavename = cavexml.get_one_cave_name(item)

    # Skip extraterrestrial bodies
    coname = item.find('country-name')
    if coname is not None:
        coname = coname.text
        if coname in excludelist:
            continue


    # Get latitude, if present
    lat_float = -999
    latitude = item.find('latitude')
    if latitude is not None: # Tag present (but could be empty)
        if latitude.text is not None:  # Tag not empty
            lat_float = latitude.text
            
    # Get longitude, if present
    lon_float = -999
    longitude = item.find('longitude')
    if longitude is not None: # Tag present
        if longitude.text is not None:  # Tag not empty
            lon_float = longitude.text

            
    # Write KML entry
    if lat_float != -999:

        pm = etree.SubElement(dd, "Placemark")
        if cavename is not None:
            etree.SubElement(pm, "name").text = cavename

        point = etree.SubElement(pm, "Point")

        mergestr = lon_float+','+lat_float+',0.0'
        etree.SubElement(point, "coordinates").text = mergestr
            
        treeout = etree.ElementTree(rootout)
        treeout.write(kml_file, pretty_print=True, encoding='UTF-8', xml_declaration=True)

            

print('Wrote file',kml_file)
