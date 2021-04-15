#! /usr/bin/env python3

# This Python script converts a CaveXML database into a RDF/XML database that
# uses the KarstLink ontology.

import lxml.etree as ET
#import CaveXML.Utilities.cavexml as cavexml
import cavexml

tree = ET.parse('../allcaves-database.xml')
#tree = ET.parse('test.xml')

rdf_file = 'tmp.rdf'

xmlns={  # Namespaces used in RDF output
    'karstlink' : "https://ontology.uis-speleo.org/ontology/#",
    'schema': "https://schema.org/",
    'rdf': "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
    'gn' : "http://www.geonames.org/ontology#", 
    'w3geo' : "http://www.w3.org/2003/01/geo/wgs84_pos#",
    'dct': "http://purl.org/dc/terms/",
    'rdfs': 'http://www.w3.org/2000/01/rdf-schema#',
    'cavexml': "https://github.com/nschorgh/CaveXML/raw/master/cavexml.owl.ttl#",
    'xml': "http://www.w3.org/XML/1998/namespace"
}

base="https://github.com/nschorgh/CaveXML/raw/master/Derivatives/allcaves-database.rdf#"


def processRecord(xmltag, namespace, rdftag):
    b1 = None
    buf = item.find(xmltag) # maxOccurs=1
    if buf is not None:
        if buf.text is not None:
            b1 = ET.SubElement(mm, ('{%s}'+rdftag) % xmlns[namespace] )
            b1.text = buf.text

    return b1


def processRecords(xmltag, namespace, rdftag):
    bb = None
    buf = item.findall(xmltag) # maxOccurs=unbounded
    for i in range(0,len(buf)):
        if buf[i].text is not None:
            bb = ET.SubElement(mm, ("{%s}"+rdftag) % xmlns[namespace] )
            bb.text = buf[i].text

    return bb


root = tree.getroot()
rootout = ET.Element("{%s}RDF" % xmlns['rdf'], nsmap=xmlns)
rootout.set('{%s}base' % xmlns['xml'], base) # add baseURL as attribute


for item in root.findall('record'):

    uniid = cavexml.generate_unique_id(item)
    
    mm = ET.Element("{%s}UnderGroundCavity" % xmlns['karstlink'] )
    mm.set('{%s}ID' % xmlns['rdf'], uniid) # add attribute
    rootout.append (mm)

    processRecords('country-name', 'schema', 'addressCountry')
    # country-name -> gn:countryCode
    con = item.find('country-name') 
    if con is not None:
        if con.text is not None:
            b1 = ET.SubElement(mm, ('{%s}countryCode') % xmlns['gn'] )
            iso2 = cavexml.country2alpha2(con.text)
            b1.text = iso2
    
    processRecords('state-or-province', 'schema', 'addressLocality')
    processRecords('phys-area-name', 'schema', 'addressLocality')

    processRecord('principal-cave-name','rdfs','label')
    processRecords('other-cave-name', 'gn', 'alternateName')
    
    processRecord('latitude','w3geo','latitude')
    processRecord('longitude','w3geo','longitude')
    processRecord('altitude','w3geo','altitude')  # cavexml != w3geo

    # discard non-numerical characters (cavexml -> karstlink)
    length = item.find('length')
    if length is not None:
        number, approx, qual = cavexml.parse_ExtendedUnsignedInteger(length.text)
        if number is not None:
            b1 = ET.SubElement(mm, "{%s}length" % xmlns['karstlink'])
            b1.text = str(number)

    # discard non-numerical characters (cavexml -> karstlink)
    vex = item.find('vertical-extent') 
    if vex is not None:
        number, approx, qual = cavexml.parse_ExtendedUnsignedInteger(vex.text)
        if number is not None:
            b1 = ET.SubElement(mm, "{%s}vertical-extent" % xmlns['karstlink'])
            b1.text = str(number)

    processRecord('number-of-entrances', 'cavexml', 'number-of-entrances')
    processRecords('map-link', 'schema', 'hasMap')
    
    processRecords('rock-type', 'cavexml', 'rock-type')
    processRecords('cave-type', 'cavexml', 'cave-type')
    processRecords('contents', 'cavexml', 'contents')
    
    processRecords('comments', 'rdfs', 'comment')
    processRecord('cave-system','schema','containedInPlace')
    processRecords('branch-name', 'karstlink', 'relatedToUndergroundCavity')
        
    ref = item.findall('reference')
    for i in range(0,len(ref)):
        refentry = ref[i].text
        if refentry is not None:
            bo = ET.SubElement(mm, "{%s}references" % xmlns['dct'])
            refurl = cavexml.extract_hyperlink_from_string(refentry)
            if len(refurl)==0: # no hyperlink
                bo.text = refentry
            else: # set attribute and only use hyperlink as value
                bo.set('{%s}resource' % xmlns['rdf'], refurl)

    processRecords('cave-use', 'cavexml', 'cave-use')
    processRecords('curation', 'cavexml', 'curation')
        
    # write XML output
    treeout = ET.ElementTree(rootout)
    treeout.write(rdf_file, pretty_print=True, encoding='UTF-8', xml_declaration=True)


print('Wrote file', rdf_file)

