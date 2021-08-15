#! /usr/bin/env python3

# Generates HTML document with full data records
# references are turned into hyperlinks

import xml.etree.ElementTree
from cavexml import *

# Enter name of XML database here
#tree = xml.etree.ElementTree.parse('test.xml')
tree = xml.etree.ElementTree.parse('../allcaves-database.xml')

root = tree.getroot()


MDLB = '  \n'  # Markdown line break


# load data for cross-linking of branches and systems
pcnlist, conlist, uidlist, syslist, list_of_lists = cross_load_data(root)


count = 0

# open file for writing
ff = open("tmp-full.md","w")


ff.write('All entries in allcaves-database.xml  \n')
ff.write('------------------------------------  \n')
ff.write('All text and links are automatically generated from the CaveXML database.  \n')
ff.write('\n')
ff.write('\n---  \n')
    
for item in root.findall('record'):
    
    # link cave-system entry
    sys_link = cross_link_cavsys(count, conlist, pcnlist, syslist[count], list_of_lists, uidlist)
    
    # link branch-name entries
    bra_link = cross_link_branch(count, conlist, pcnlist, syslist, list_of_lists[count], uidlist)

    # output one record in Markdown format

    buffer = ''

    uid = generate_unique_id(item)
    ff.write('<a name="' + uid + '"></a>\n')
    
    con = item.find('country-name')
    if con is not None:
        if con.text is not None: # empty tag
            buffer += con.text

    province = item.findall('state-or-province')
    prostr = merge_elements(province)
    if prostr:
        buffer += ' - ' + prostr

    area = item.findall('phys-area-name')
    outstr = merge_elements(area)
    if outstr:
        buffer += ' - ' + outstr

    ff.write(buffer + MDLB)
    buffer = ''

    uniid = generate_unique_id(item)
    
    ff.write('*Cave Name(s):* ')
    try:
        pcn = item.find('principal-cave-name').text
        if pcn:
            buffer += '**' + pcn.strip() + '**'
    except:
        pass

    ocn = item.findall('other-cave-name')
    str = merge_elements(ocn)
    if str:
        buffer += ' ' + str.strip()
            
    cid = item.find('cave-id')
    if cid is not None:
        if cid.text:
            buffer += ' *Id:* ' + cid.text

    ff.write(buffer + MDLB)
    buffer = ''
            
    latitude = item.find('latitude')
    longitude = item.find('longitude')
    if latitude is not None and longitude is not None:
        if latitude.text and longitude.text:
            lon = float(longitude.text)
            if lon>0:
                lonstr = '+' + longitude.text
            else:
                lonstr = longitude.text
            #buffer = '*Coordinates:* ' + latitude.text + ', ' + lonstr + ' '
            if con is not None:
                googlemaplink = generate_maplink(latitude.text, longitude.text, con.text)
            else:
                googlemaplink = generate_maplink(latitude.text, longitude.text, None)
            buffer = '*Coordinates:* [' + latitude.text + ', ' + lonstr + '](' + googlemaplink + ') '
            
    alt = item.findall('altitude')
    altstr = merge_elements(alt)
    if altstr:
        buffer += '*altitude:* ' + altstr 

    if buffer:
        ff.write(buffer + MDLB)
    buffer = ''
        
    leng = item.find('length')
    if leng is not None:
        if leng.text is not None:
            buffer = '*Length:* ' + leng.text + 'm '

    vex = item.find('vertical-extent')
    if vex is not None:
        if vex.text is not None:
            buffer +=  '*Vertical extent:* ' + vex.text + 'm '
            
    noe = item.find('number-of-entrances')
    if noe is not None:
        if noe.text is not None: 
            buffer += '*Number of entrances:* ' + noe.text

    if buffer:
        ff.write(buffer + MDLB)
    buffer = ''

    mali = item.findall('map-link')
    if mali:
        for j in range(0,len(mali)):
            uri = mali[j].text
            if uri:
                ff.write("[map](" + uri + ") ")
        ff.write(MDLB)

            
    roty = item.findall('rock-type')
    rostr = merge_elements(roty)
    if rostr:
        buffer = '*Rock type:* ' + rostr + ' '
        
    cavty = item.findall('cave-type')
    cavstr = merge_elements(cavty)
    if cavstr:
        buffer += '*Cave type:* ' + cavstr 

    if buffer:
        ff.write(buffer + MDLB)
    buffer = ''
        
    cont = item.findall('contents')
    contstr = merge_elements(cont)
    if contstr:
        ff.write('*Contents:* ' + contstr + MDLB)

    comm = item.findall('comments')
    comm = merge_elements(comm)
    if comm:
        ff.write('*Comments:* ' + comm.strip() + MDLB)

    cavsys = item.find('cave-system')
    try:
        if sys_link:
            ff.write(' *Part of* [' + cavsys.text.strip() + '](#' + sys_link + ')' + MDLB)
        else:
            ff.write(' *Part of* ' + cavsys.text.strip() + MDLB)
    except:
        pass

    
    branch = item.findall('branch-name')
    if len(branch)>0:
        buffer = '*Branches:* '
    for j in range(0,len(branch)):
        brastr = branch[j].text
        if brastr:
            if bra_link[j]:
                buffer += '[' + brastr + '](#' + bra_link[j] + '); '
            else:
                buffer += brastr + '; '
    if buffer:
        ff.write(buffer + MDLB)
            
    
    ref = item.findall('reference')
    if ref:
        #if len(ref)>0:
        #    ff.write('  *References:*')

        for j in range(0,len(ref)):
            rawstr = ref[j].text
            if rawstr is None:
                continue
            refstr = rawstr
            refstr = refstr.replace("doi:", "https://doi.org/")
            refstr = refstr.replace("DOI:", "https://doi.org/")
            if "https://www" not in refstr and "http://www." not in refstr:
                refstr = refstr.replace("www", "http://www") # could be http or https

            hytxt = extract_hyperlink_from_string(refstr)
            
            if not hytxt:
                ff.write(refstr + MDLB)
            else:
                htmllink = "[" + rawstr + "](" + hytxt + ") "
                ff.write(htmllink + MDLB)



    caveuse = item.findall('cave-use')
    str = merge_elements(caveuse)
    if str:
        ff.write('*Cave use:* ' + str + MDLB)

    cur = item.findall('curation')
    str = merge_elements(cur)
    if str:
        ff.write('  *Data curation:* ' + str + MDLB)
        

    ff.write('\n---  \n')

    
    count = count + 1  # count number of records

    

print('Wrote file tmp-full.md')
print('Number of records:', count)


ff.close()
