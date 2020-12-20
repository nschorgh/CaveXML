#! /usr/bin/env python3

# Module for CaveXML
# defines functions helpful for working with CaveXML data


import re  # Regular Expressions


def merge_elements(stuff):
    # merges repeat XML elements, useful for flattenig database
    if stuff:  #if stuff is not None and len(stuff)>0:
        outstr = stuff[0].text
        for i in range(1,len(stuff)):  # merge multiple entries
            if stuff[i].text is not None:
                outstr = outstr + "; " + stuff[i].text
    else:
        outstr = ""
    return outstr



def parse_ExtendedUnsignedInteger(eui):
    if eui is None:
        return None, None, None

    # test whether input is ExtendedUnsignedInteger
    matched = re.fullmatch("[~>]?[0-9]+[+]?", eui.strip())
    if matched is None:
        print('Warning:',eui,'is not an ExtendedUnsignedInteger')
        return None, None, None

    # extract number
    number = [int(s) for s in re.findall(r'\b\d+\b',eui)]
    number = number[0]

    # set defaults
    qualifier = None
    approx = False

    # determine meaning of characters, if present
    if len(eui)>0:
        first_char = eui[0]
        if first_char=="~":
            approx = True
        if first_char==">":
            qualifier = '>'

        last_char = eui[len(eui)-1]
        if last_char == '+':
            qualifier = '+'
            
    #print('EUI:',eui,number,approx,qualifier)
    return number, approx, qualifier



def parse_AltitudeEntry(alt):
    # this function always returns two numbers
    lownumber = +99999; highnumber = -99999

    for i in range(0,len(alt)):
        outstr = alt[i].text
        if outstr is not None:
            if "-" in outstr or "–" in outstr: # altitude range
                if "-" in outstr:
                    hyphen = '-'
                if "–" in outstr:
                    hyphen = '–'
                minalt = int(outstr.split(hyphen)[0])
                maxalt = int(outstr.split(hyphen)[1])
                if minalt<lownumber:
                    lownumber = minalt
                if maxalt>highnumber:
                    highnumber = maxalt
            else:  # ExtendedUnsignedInteger optionally followed by comment
                outstr = outstr.strip()
                if len(outstr.split(' '))>1:  
                    outstr = outstr.split(' ')[0]  # strip comment
                number, approx, qual = parse_ExtendedUnsignedInteger(outstr)
                if number<lownumber:
                    lownumber = number
                if number>highnumber:
                    highnumber = number
                #if qual=='>' or qual=='+':
                #    highnumber = +99999
                
    if lownumber>highnumber and lownumber!=+99999:
        swap = highnumber
        highnumber = lownumber
        lownumber = swap

    return lownumber, highnumber



def parse_cave_id(caveid):

    org = ''
    id = ''
    
    if caveid is None:
        return
    
    outstr = caveid.text
    if outstr is not None:
        try:
            org = outstr.split('-')[0]  # organization code
            re.compile("[A-Z]{3,4}", org)  # fails if it doesn't match
            id  = outstr.split('-')[1]  # (incorrect if 2nd hyphen present)
        except:  # no organization given
            org = ''
            id  = outstr

    return org, id



def is_this_an_ice_cave(record):
    # returns True if 'contents' includes 'permanent ice'
    cont = record.findall('contents')
    if cont:
        for i in range(0,len(cont)):
            if cont[i].text:
                if 'permanent ice' in cont[i].text:
                    return True

    return False



def is_this_a_lava_tube(record):
    # returns True if 'cave-type' includes 'lava tunnel'
    cavetype = record.findall('cave-type')
    if cavetype:
        for i in range(0,len(cavetype)):
            if cavetype[i].text:
                if 'lava tunnel' in cavetype[i].text:
                    return True

    return False



def get_one_cave_name(item):
    # Get a cave name for a record by searching, in the following order:
    # 1. principal-cave-name
    # 2. cave-id(s)
    # 3. other-cave-name(s)

    pcn = item.findall('principal-cave-name')
    if len(pcn)>0: # tag present
        pcn = pcn[0].text
        if pcn is not None: # not empty
            outstr = pcn.strip() # strips leading and trailing whitespace
            if len(outstr)>0:
                return outstr

    cid = item.findall('cave-id')
    for i in range(0,len(cid)):
        outstr = cid[i].text
        if outstr is not None: 
            outstr = outstr.strip()
            if len(outstr)>0:
                return outstr
                
    ocn = item.findall('other-cave-name')
    for i in range(0,len(ocn)):
        outstr = ocn[i].text
        if outstr is not None:
            outstr = outstr.strip()
            if len(outstr)>0:
                return outstr

    return ''  # if no name found, return empty string



def extract_hyperlink_from_string(refstr):
    k = refstr.find("https://")
    if k<0:
        k = refstr.find("http://")
        
    if k>=0: 
        t = refstr[k:] 
        kend = t.find(" ") 
        if kend>0:
            t = t[:kend]
            t = '"' + t + '"'
        return t

    return ''  # if no hyperlink found



def country2alpha2(countryname):
    # Return 2-letter ISO 3166-1 abbreviations for country name.
    # The country names are exactly as in cavexml.xsd,
    # where a few country names deviate from the official names.

    dict = {
        'Afghanistan': 'AF',
        'Åland Islands': 'AX',
        'Albania': 'AL',
        'Algeria': 'DZ',
        'American Samoa': 'AS',
        'Andorra': 'AD',
        'Angola': 'AO',
        'Anguilla': 'AI',
        'Antarctica': 'AQ',
        'Antigua and Barbuda': 'AG',
        'Argentina': 'AR',
        'Armenia': 'AM',
        'Aruba': 'AW',
        'Australia': 'AU',
        'Austria': 'AT',
        'Azerbaijan': 'AZ',
        'Bahamas': 'BS',
        'Bahrain': 'BH',
        'Bangladesh': 'BD',
        'Barbados': 'BB',
        'Belarus': 'BY',
        'Belgium': 'BE',
        'Belize': 'BZ',
        'Benin': 'BJ',
        'Bermuda': 'BM',
        'Bhutan': 'BT',
        'Bolivia': 'BO',  # 'Bolivia, Plurinational State of': 'BO', 
        'Bonaire, Sint Eustatius and Saba': 'BQ',
        'Bosnia and Herzegovina': 'BA',
        'Botswana': 'BW',
        'Bouvet Island': 'BV',
        'Brazil': 'BR',
        'British Indian Ocean Territory': 'IO',
        'Brunei Darussalam': 'BN',
        'Bulgaria': 'BG',
        'Burkina Faso': 'BF',
        'Burundi': 'BI',
        'Cambodia': 'KH',
        'Cameroon': 'CM',
        'Canada': 'CA',
        'Cape Verde': 'CV',
        'Cayman Islands': 'KY',
        'Central African Republic': 'CF',
        'Chad': 'TD',
        'Chile': 'CL',
        'China': 'CN',
        'Christmas Island': 'CX',
        'Cocos (Keeling) Islands': 'CC',
        'Colombia': 'CO',
        'Comoros': 'KM',
        'Congo': 'CG',
        'Congo, Democratic Republic of the': 'CD',
        'Cook Islands': 'CK',
        'Costa Rica': 'CR',
        'Country name': 'Code',
        'Croatia': 'HR',
        'Cuba': 'CU',
        'Curaçao': 'CW',
        'Cyprus': 'CY',
        'Czech Republic': 'CZ',
        "Côte d'Ivoire": 'CI',
        'Denmark': 'DK',
        'Djibouti': 'DJ',
        'Dominica': 'DM',
        'Dominican Republic': 'DO',
        'Ecuador': 'EC',
        'Egypt': 'EG',
        'El Salvador': 'SV',
        'Equatorial Guinea': 'GQ',
        'Eritrea': 'ER',
        'Estonia': 'EE',
        'Ethiopia': 'ET',
        'Falkland Islands (Malvinas)': 'FK',
        'Faroe Islands': 'FO',
        'Fiji': 'FJ',
        'Finland': 'FI',
        'France': 'FR',
        'French Guiana': 'GF',
        'French Polynesia': 'PF',
        'French Southern Territories': 'TF',
        'Gabon': 'GA',
        'Gambia': 'GM',
        'Georgia': 'GE',
        'Germany': 'DE',
        'Ghana': 'GH',
        'Gibraltar': 'GI',
        'Greece': 'GR',
        'Greenland': 'GL',
        'Grenada': 'GD',
        'Guadeloupe': 'GP',
        'Guam': 'GU',
        'Guatemala': 'GT',
        'Guernsey': 'GG',
        'Guinea': 'GN',
        'Guinea-Bissau': 'GW',
        'Guyana': 'GY',
        'Haiti': 'HT',
        'Heard Island and McDonald Islands': 'HM',
        'Holy See (Vatican City State)': 'VA',
        'Honduras': 'HN',
        'Hong Kong': 'HK',
        'Hungary': 'HU',
        'Iceland': 'IS',
        'India': 'IN',
        'Indonesia': 'ID',
        'Iran': 'IR',  # 'Iran, Islamic Republic of': 'IR',
        'Iraq': 'IQ',
        'Ireland': 'IE',
        'Isle of Man': 'IM',
        'Israel': 'IL',
        'Italy': 'IT',
        'Jamaica': 'JM',
        'Japan': 'JP',
        'Jersey': 'JE',
        'Jordan': 'JO',
        'Kazakhstan': 'KZ',
        'Kenya': 'KE',
        'Kiribati': 'KI',
        "Korea, Democratic People's Republic of": 'KP',
        'Korea, Republic of': 'KR',
        'Kuwait': 'KW',
        'Kyrgyzstan': 'KG',
        'Laos': 'LA',  #  "Lao People's Democratic Republic": 'LA',
        'Latvia': 'LV',
        'Lebanon': 'LB',
        'Lesotho': 'LS',
        'Liberia': 'LR',
        'Libya': 'LY',
        'Liechtenstein': 'LI',
        'Lithuania': 'LT',
        'Luxembourg': 'LU',
        'Macao': 'MO',
        'Madagascar': 'MG',
        'Malawi': 'MW',
        'Malaysia': 'MY',
        'Maldives': 'MV',
        'Mali': 'ML',
        'Malta': 'MT',
        'Marshall Islands': 'MH',
        'Martinique': 'MQ',
        'Mauritania': 'MR',
        'Mauritius': 'MU',
        'Mayotte': 'YT',
        'Mexico': 'MX',
        'Micronesia': 'FM', # 'Micronesia, Federated States of': 'FM',
        'Moldova, Republic of': 'MD',
        'Monaco': 'MC',
        'Mongolia': 'MN',
        'Montenegro': 'ME',
        'Montserrat': 'MS',
        'Morocco': 'MA',
        'Mozambique': 'MZ',
        'Myanmar': 'MM',
        'Namibia': 'NA',
        'Nauru': 'NR',
        'Nepal': 'NP',
        'Netherlands': 'NL',
        'New Caledonia': 'NC',
        'New Zealand': 'NZ',
        'Nicaragua': 'NI',
        'Niger': 'NE',
        'Nigeria': 'NG',
        'Niue': 'NU',
        'Norfolk Island': 'NF',
        'North Macedonia': 'MK',
        'Northern Mariana Islands': 'MP',
        'Norway': 'NO',
        'Oman': 'OM',
        'Pakistan': 'PK',
        'Palau': 'PW',
        'Palestine, State of': 'PS',
        'Panama': 'PA',
        'Papua New Guinea': 'PG',
        'Paraguay': 'PY',
        'Peru': 'PE',
        'Philippines': 'PH',
        'Pitcairn': 'PN',
        'Poland': 'PL',
        'Portugal': 'PT',
        'Puerto Rico': 'PR',
        'Qatar': 'QA',
        'Romania': 'RO',
        'Russia': 'RU', # 'Russian Federation': 'RU',
        'Rwanda': 'RW',
        'Réunion': 'RE',
        'Saint Barthélemy': 'BL',
        'Saint Helena, Ascension and Tristan da Cunha': 'SH',
        'Saint Kitts and Nevis': 'KN',
        'Saint Lucia': 'LC',
        'Saint Martin (French part)': 'MF',
        'Saint Pierre and Miquelon': 'PM',
        'Saint Vincent and the Grenadines': 'VC',
        'Samoa': 'WS',
        'San Marino': 'SM',
        'Sao Tome and Principe': 'ST',
        'Saudi Arabia': 'SA',
        'Senegal': 'SN',
        'Serbia': 'RS',
        'Seychelles': 'SC',
        'Sierra Leone': 'SL',
        'Singapore': 'SG',
        'Sint Maarten (Dutch part)': 'SX',
        'Slovakia': 'SK',
        'Slovenia': 'SI',
        'Solomon Islands': 'SB',
        'Somalia': 'SO',
        'South Africa': 'ZA',
        'South Georgia and the South Sandwich Islands': 'GS',
        'South Sudan': 'SS',
        'Spain': 'ES',
        'Sri Lanka': 'LK',
        'Sudan': 'SD',
        'Suriname': 'SR',
        'Svalbard and Jan Mayen': 'SJ',
        'Swaziland': 'SZ',
        'Sweden': 'SE',
        'Switzerland': 'CH',
        'Syria': 'SY',   # 'Syrian Arab Republic': 'SY',
        'Taiwan': 'TW',  #  'Taiwan, Province of China': 'TW',
        'Tajikistan': 'TJ',
        'Tanzania': 'TZ',  # 'Tanzania, United Republic of': 'TZ',
        'Thailand': 'TH',
        'Timor-Leste': 'TL',
        'Togo': 'TG',
        'Tokelau': 'TK',
        'Tonga': 'TO',
        'Trinidad and Tobago': 'TT',
        'Tunisia': 'TN',
        'Turkey': 'TR',
        'Turkmenistan': 'TM',
        'Turks and Caicos Islands': 'TC',
        'Tuvalu': 'TV',
        'Uganda': 'UG',
        'Ukraine': 'UA',
        'United Arab Emirates': 'AE',
        'United Kingdom': 'GB',
        'United States of America': 'US',
        'United States Minor Outlying Islands': 'UM',
        'Uruguay': 'UY',
        'Uzbekistan': 'UZ',
        'Vanuatu': 'VU',
        'Venezuela': 'VE', # 'Venezuela, Bolivarian Republic of': 'VE',
        'Viet Nam': 'VN',
        'Virgin Islands, British': 'VG',
        'Virgin Islands, U.S.': 'VI',
        'Wallis and Futuna': 'WF',
        'Western Sahara': 'EH',
        'Yemen': 'YE',
        'Zambia': 'ZM',
        'Zimbabwe': 'ZW',

        'Moon': 'XO',
        'Mars': 'XA'
    }


    return dict[countryname]




import hashlib  # only used in generate_unique_id

def generate_unique_id(item):
    # generate identification string, which is unqiue for a record

    try: # assumes the record includes a country name
        con = item.find('country-name')
        iso2 = country2alpha2(con.text)
    except:
        iso2 = 'XX' # no-man's land
    if len(iso2) != 2:
        iso2 = 'XX'

    try: # use cave-id, if available
        cid = item.find('cave-id')
        uniid = iso2 + '-' + cid.text
    except: # create hash code based on several entries
        mashup = get_one_cave_name(item)
        try:
            province = item.findall('state-or-province')
            prostr = merge_elements(province)
            mashup += prostr
        except:
            pass
        try:
            area = item.findall('phys-area-name')
            outstr = merge_elements(area)
            mashup += outstr
        except:
            pass
        hashcode = hashlib.md5(mashup.encode('utf-8')).hexdigest()
        uniid = iso2 + '-' + hashcode
        
    return uniid


