#! /usr/bin/env python3

# Generates HTML document with full data records
# references are turned into hyperlinks

import xml.etree.ElementTree
from cavexml import *

# Enter name of XML database here
#tree = xml.etree.ElementTree.parse('test.xml')
tree = xml.etree.ElementTree.parse('../allcaves-database.xml')


    
root = tree.getroot()

count = 0

# open file for writing
f = open("tmp.html","w")

f.write('<html><body>')


# load data for cross-linking of branches and systems
pcnlist, conlist, uidlist, syslist, list_of_lists = cross_load_data(root)


for item in root.findall('record'):
    
    # link cave-system entry
    sys_link = cross_link_cavsys(count, conlist, pcnlist, syslist[count], list_of_lists, uidlist)
    
    # link branch-name entries
    bra_link = cross_link_branch(count, conlist, pcnlist, list_of_lists[count], uidlist)

    count += 1  # count number of records
    
    f.write('\n<p>')
    
    uid = generate_unique_id(item)
    f.write('<a name="' + uid + '"></a>\n')
    
    con = item.find('country-name')
    if con is not None:
        con = con.text
        f.write(con)

    province = item.findall('state-or-province')
    prostr = merge_elements(province)
    if prostr:
        f.write(' - ' + prostr)

    area = item.findall('phys-area-name')
    outstr = merge_elements(area)
    if outstr:
        f.write(' - ' + outstr)

    f.write('<br><i>Cave Name(s):</i>')
    try:
        pcn = item.find('principal-cave-name').text
        if pcn:
            f.write(' <b>' + pcn + '</b>')
    except:
        pass

    ocn = item.findall('other-cave-name')
    str = merge_elements(ocn)
    if str:
        f.write(' ' + str)
            
    cid = item.find('cave-id')
    if cid is not None:
        if cid.text:
            f.write(' <i>Id:</i> ' + cid.text)
        
    latitude = item.find('latitude')
    longitude = item.find('longitude')
    str1 = ''
    if latitude is not None and longitude is not None:
        if latitude.text and longitude.text:
            lon = float(longitude.text)
            if lon>0:
                lonstr = '+' + longitude.text
            else:
                lonstr = longitude.text
            str1 = '<i>Coordinates:</i> ' + latitude.text + ', ' + lonstr

    alt = item.findall('altitude')
    altstr = merge_elements(alt)
    if str1:
        str2 = '&ensp;'
    else:
        str2 = ''
    if altstr:
        str2 = str2 + '<i>altitude:</i> ' + altstr 

    if str1 or str2:
        f.write('<br>' + str1 + str2)
        
    leng = item.find('length')
    str1 = ''
    if leng is not None:
        if leng.text is not None:
            str1 = '<i>Length:</i> ' + leng.text + 'm'

    vex = item.find('vertical-extent')
    if str1:
        str2 = '&ensp;'
    else:
        str2 = ''
    if vex is not None:
        if vex.text is not None:
            str2 = str2 + ' <i>Vertical extent:</i> ' + vex.text + 'm'
            
    noe = item.find('number-of-entrances')
    if str1 or str2:
        str3 = '&ensp;'
    else:
        str3 = ''
    if noe is not None:
        if noe.text is not None: 
            str3 = str3 + ' <i>Number of entrances:</i> ' + noe.text

    if str1 or str2 or str3:
        f.write('<br>' + str1 + str2 + str3)

    mali = item.findall('map-link')
    if mali:
        f.write('<br>')
        for j in range(0,len(mali)):
            uri = mali[j].text
            if uri:
                f.write('<a href="' + uri + '">map</a> ')
        
    roty = item.findall('rock-type')
    rostr = merge_elements(roty)
    if rostr:
        f.write('<br><i>Rock type:</i> ' + rostr) 
        
    cavty = item.findall('cave-type')
    cavstr = merge_elements(cavty)
    if cavstr:
        f.write('<br><i>Cave type:</i> ' + cavstr) 

    cont = item.findall('contents')
    contstr = merge_elements(cont)
    if contstr:
        f.write('<br><i>Contents:</i> ' + contstr)

    comm = item.findall('comments')
    comm = merge_elements(comm)
    if comm:
        f.write('<br><i>Comments:</i> ' + comm.strip())

    cavsys = item.find('cave-system')
    try:
        if sys_link:
            f.write('<br><i>Part of</i> <a href="#' + sys_link + '">' + cavsys.text.strip() + '</a>')
        else:
            f.write('<br><i>Part of</i> ' + cavsys.text.strip())
    except:
        pass

    branch = item.findall('branch-name')
    if len(branch)>0:
        buffer = '<br><i>Branches:</i> '
        for j in range(0,len(branch)):
            brastr = branch[j].text
            if brastr:
                if bra_link[j]:
                    buffer += '<a href="#' + bra_link[j] + '"</a>' + brastr + '</a>; '
                else:
                    buffer += brastr + '; '

        f.write(buffer + '\n')
            
        
    ref = item.findall('reference')
    if ref:
        #if len(ref)>0:
        #    f.write('<br><i>References:</i>')

        for i in range(0,len(ref)):
            refstr = ref[i].text
            if refstr is None:
                continue
            refstr = refstr.replace("doi:", "https://doi.org/")
            refstr = refstr.replace("DOI:", "https://doi.org/")
            if 'www' in refstr:
                if "https://www" not in refstr and "http://www." not in refstr:
                    refstr = refstr.replace("www", "http://www") # could be http or https

            hytxt = extract_hyperlink_from_string(refstr)
            
            if not hytxt:
                f.write('<br>' + refstr)
            else:
                htmllink = "<a href=" + hytxt + ">" + refstr + "</a>"
                f.write('<br>' + htmllink)

    caveuse = item.findall('cave-use')
    outstr = merge_elements(caveuse)
    if outstr:
        f.write('<br><i>Cave use:</i> ' + outstr)

    cur = item.findall('curation')
    outstr = merge_elements(cur)
    if outstr:
        f.write('<br><i>Data curation:</i> ' + outstr)
        

    f.write('\n<hr>')

    

    
f.write('</body></html>')
f.close()
print('Wrote tmp.html')
print('Number of records:', count)

