#! /usr/bin/env python3

# This script outputs lon/lat coordinates from CaveXML entries in KML format'

import xml.etree.ElementTree
import cavexml

# Enter name of XML database here
tree = xml.etree.ElementTree.parse('../allcaves-database.xml')

root = tree.getroot()

excludelist = ['Moon','Mars']

# print header lines
print('<?xml version="1.0" encoding="UTF-8"?>')
print('<kml xmlns="http://www.opengis.net/kml/2.2" xmlns:gx="http://www.google.com/kml/ext/2.2">')
print('<Document> ')

    
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
    if latitude is not None:
        if latitude.text is not None:
            lat_float = float(latitude.text)
            
    # Get longitude, if present
    lon_float = -999
    longitude = item.find('longitude')
    if longitude is not None: # Tag present (but could be empty)
        if longitude.text is not None:
            lon_float = float(longitude.text)

            
    # Write KML entry
    if lat_float != -999:
        print('  <Placemark>')
        print('    <name>',cavename,'</name>',sep='')
        print('    <Point>')
        print('      <coordinates>',lon_float,',',lat_float,',0.0</coordinates>',sep='')
        print('    </Point>')
        print('  </Placemark>')



# close KML file
print('</Document>')
print('</kml>')
