#! /usr/bin/env python3

# This script outputs lon/lat coordinates from CaveXML entries in KML format'

import xml.etree.ElementTree

# Enter name of XML database here
tree = xml.etree.ElementTree.parse('../allcaves-database.xml')

root = tree.getroot()

excludelist = ['Moon','Mars']

# print header lines
print('<?xml version="1.0" encoding="UTF-8"?>')
print('<kml xmlns="http://www.opengis.net/kml/2.2" xmlns:gx="http://www.google.com/kml/ext/2.2">')
print('<Document> ')

    
for item in root.findall('record'):
        
    cavename = []
    
    # Find a cave name
    pcn = item.findall('principal-cave-name')
    if len(pcn)>0: # tag present
        pcn = pcn[0].text
        if pcn is not None: # not empty
            cavename = pcn.strip() # strips leading and trailing whitespace

    if len(cavename)==0:
        ocn = item.findall('other-cave-name')
        for i in range(0,len(ocn)):
            str = ocn[i].text
            if str is not None: # not empty
                cavename = str.strip()
                break


    # Skip extraterrestrial bodies
    coname = item.find('country-name')
    if coname is not None:
        coname = item.find('country-name').text
        if coname in excludelist:
            break


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
