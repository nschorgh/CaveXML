#! /usr/bin/env python3

# This script outputs lon/lat coordinates from CaveXML entries in KML format'

import xml.etree.ElementTree
import cavexml

# Enter name of XML database here
tree = xml.etree.ElementTree.parse('../allcaves-database.xml')

root = tree.getroot()

excludelist = ['Moon','Mars','Mercury','Venus','Io','Titan']


# open file for writing
f = open('tmp.kml', 'w')


# print header lines
f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
f.write('<kml xmlns="http://www.opengis.net/kml/2.2" xmlns:gx="http://www.google.com/kml/ext/2.2">\n')
f.write('<Document>\n')


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
    if longitude is not None: # Tag present (but could be empty)
        if longitude.text is not None:
            lon_float = longitude.text

            
    # Write KML entry
    if lat_float != -999:
        f.write('  <Placemark>\n')
        f.write('    <name>'+cavename+'</name>\n')
        f.write('    <Point>\n')
        f.write('      <coordinates>'+lon_float+','+lat_float+',0.0</coordinates>\n')
        f.write('    </Point>\n')
        f.write('  </Placemark>\n')



# close KML file
f.write('</Document>\n')
f.write('</kml>\n')

f.close()
print('Wrote file tmp.kml')
