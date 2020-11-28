CaveXML Definitions
===================

CaveXML facilitates exchange of data about caves through the definition and implementation of a data interchange format. The CaveXML standard defines a set of XML elements and their meaning, as described below. Its syntax is implemented in an XML Schema Definition (`cavexml.xsd`). As a pilot project, basic data for a few thousand caves has been organized in CaveXML format.

> "The systematic documentation, mapping and publication of data about caves (excepting entrance locations) is a responsibility of all users of the cave environment, and should be encouraged by management authorities."  
> *Guidelines for Cave and Karst Protection*, Working Group on Cave and Karst Protection (1997)

The Informatics Commission of the Internationl Union of Speleology (UISIC) has drafted guidelines for a data exchange standard with over 700 fields. CaveXML builds on these recommendations for the much smaller number of elements it uses.  

A CaveXML database has the following structure, where each record corresponds to a cave or cave system:

        <CaveDataBase> 
          <record>
            ...
          </record>
        
          <record>
            ...
          </record>
            .
            .
            .
        </CaveDataBase>

Elements within a record are defined as follows:

**\<country-name\>**  *controlled vocabulary*  
Country name where the cave entrance is located. This should be the name of the country spelled out and according to the ISO 3166 standard, although a few country names have been simplified. (The precise list is found in the CaveXML Schema Definition `cavexml.xsd`.)  
Similar to UISIC field [SY285](http://www.uisic.uis-speleo.org/exchange/atendefn.html#285)  
For extraterrestrial caves, this element specifies the planetary body where the cave is located. Allowed terms are "Moon", which refers to Earth's moon, and "Mars". An empty or missing entry implies the cave is located on planet Earth. In fact, "Earth" is not an allowed term, because it is implicit.

**\<state-or-province\>**  *string*  
State or province where the cave entrance is located. This can also be a county or district. [state-or-province] is intended for politically or organizationally defined areas below country level. For physically/geologically defined units, use [phys-area-name] instead.      
Generalization of UISIC field [SY287](http://www.uisic.uis-speleo.org/exchange/atendefn.html#287)

**\<phys-area-name\>**  *string*  
Name of mountain, volcano, mountain range, island, geologic unit, or another physically-defined unit. Example: Pyrenees. For politically-defined regions use [state-or-province] instead.

**\<principal-cave-name\>** *string, maxOccurs=1*    
The current formal agreed name for a cave or karst feature, expressed in the local language. Where a new name is awaiting ratification, enclose it in round brackets. The character set is UTF-8, so characters from many languages can be used.    
UISIC field [CA70](http://www.uisic.uis-speleo.org/exchange/atendefn.html#70)

**\<other-cave-name\>**  *string*  
Further names which a cave or karst feature has or has had beyond its current name as given in [principal-cave-name].    
Similar to UISIC field [CA69](http://www.uisic.uis-speleo.org/exchange/atendefn.html#69)

**\<cave-id\>** *(special string)*  
International cave identification number: 2-letter ISO country code + optional 3-letter organization code + cave registry number, separated by dashes, e.g. US-HSS-234/7. For small countries, this might just be the 2-letter ISO country code + national cave number, e.g. AT-1234/5.  
Similar to UISIC field [CA227](http://www.uisic.uis-speleo.org/exchange/atendefn.html#227). 
Very similar to the "international cave number". A record is allowed to have more than one [cave-id], but different caves must have different [cave-id]s.  

**\<latitude\>**  *-90 ≤ decimal ≤ +90, maxOccurs=1*  
The N-S latitude of the cave entrance or karst feature, expressed as +/- degrees and decimal degrees. Positive if north of the equator, negative if south of the equator. Expressed as a real number, rather than as degrees, minutes, and seconds. If both [latitude] and [longitude] have only one significant digit after the decimal point, they have been rounded in order not to reveal the exact location.  
UISIC fields [CA245](http://www.uisic.uis-speleo.org/exchange/atendefn.html#245) (exact) or [CA21](http://www.uisic.uis-speleo.org/exchange/atendefn.html#21) (coarse)

**\<longitude\>**  *-180 ≤ decimal ≤ +180, maxOccurs=1*  
The E-W longitude of the cave entrance or karst feature, expressed as +/- degrees and decimal degrees. Positive if east of Greenwich, or negative if west of Greenwich. Expressed as a real number, rather than as degrees, minutes, and seconds. If both [latitude] and [longitude] have only one significant digit after the decimal point, they have been rounded in order not to reveal the exact location. (It is statistically improbable that latitude and longitude would each end in several trailing zeros, and it is therefore apparent from the numbers whether the coordinates have been intentionally rounded. The rounding precision is 0.1 degree.)  
UISIC fields [CA246](http://www.uisic.uis-speleo.org/exchange/atendefn.html#246) (exact) or [CA22](http://www.uisic.uis-speleo.org/exchange/atendefn.html#22) (coarse)

**\<altitude\>** *(special string)*  
Altitude or range of altitudes of cave entrance(s) in meters above sea level, followed by an optional comment that can be used to clarify the nature of the entry. Multiple [altitude] entries are allowed in a single record. Examples: \~2500 main entrance, 2227 lower entrance, 2227-2500. If a range of altitudes is provided, it should represent the altitudes of the lowest and highest entrance of a cave, and not an uncertainty in altitude. The latter should be indicated with a "\~" sign in front of the number of by adding "coarse" after the altitude value.  
Similar to UISIC fields [CA442](http://www.uisic.uis-speleo.org/exchange/atendefn.html#442) (altitude) and [CA670](http://www.uisic.uis-speleo.org/exchange/atendefn.html#670) (altitude-comment) combined.

**\<length\>**  *ExtendedUnsignedInteger, maxOccurs=1*  
The aggregate length of the cave passages in meters, usually obtained by summing the lengths of all surveyed distances. Length differs from horizontal extent. The length should be rounded to the nearest integer. The unit must be meters, not km or feet.    
UISIC field [CA56](http://www.uisic.uis-speleo.org/exchange/atendefn.html#56)

**\<vertical-extent\>**  *ExtendedUnsignedInteger, maxOccurs=1*  
The overall vertical distance in meters between the highest and lowest known points of the cave or karst feature, expressed as an unsigned value. (Sometimes vertical extent is defined as the vertical distance between the highest and lowest survey station.)  
UISIC field [CA511](http://www.uisic.uis-speleo.org/exchange/atendefn.html#511)

**\<number-of-entrances\>**  *ExtendedUnsignedInteger, maxOccurs=1*  
The total number of entrances to the cave, whether they are numbered or not. Normally provided only if there is more than one entrance. This is usually a positive integer, but expressions such as \>5 are allowed.  
UISIC field [CA9](http://www.uisic.uis-speleo.org/exchange/atendefn.html#9)

**\<rock-type\>**  *controlled vocabulary*  
Type(s) of rock in which the cave or karst feature is formed from, selected from a pre-defined list of options.
Similar to UISIC field [CA7](http://www.uisic.uis-speleo.org/exchange/atendefn.html#7).  
[List of options:](http://www.uisic.uis-speleo.org/exchange/atencode.html#7) limestone, dune limestone, dolomite, marble, basalt, dolerite, granite, gypsum, ice, lava, magnesite, mudstone, quartzite, sandstone, soil, tuff.  

**\<cave-type\>**  *controlled vocabulary*  
The cave type(s) according to a pre-defined list of terms.
UISIC field [CA8](http://www.uisic.uis-speleo.org/exchange/atendefn.html#8).  
 [List of options:](http://www.uisic.uis-speleo.org/exchange/atencode.html#8) limestone cave, artificial cave, blowhole, boulder cave, fault-movement cave, glacier cave, lava tunnel, lava vent, mine, rock shelter, sea cave, piping cave, weathering cave, misc. type. The term "lava tunnel" is equivalent to "lava tube".

**\<contents\>**  *controlled vocabulary*  
What the cave contains. Similar to UISIC field [CA72](http://www.uisic.uis-speleo.org/exchange/atendefn.html#72).  
List of options: permanent ice, periodic ice, perennially submerged, intermittently submerged, extensive guano, many bats, occasional bats, fish, snakes, trogloxenes, accidental trogloxenes, troglophiles, troglobites, charcoal, paintings, minerals, lake(s), waterfall(s), tree roots. CA72 has [36 allowed options](http://www.uisic.uis-speleo.org/exchange/atencode.html#72), which have been shortened to 17, and the two terms about submersion are borrowed from [CA2](http://www.uisic.uis-speleo.org/exchange/atendefn.html#2). If the desired entry is not available among the list of terms, enter it in [comments] instead.

**\<comments\>**  *string*  
Comments about a cave or karst feature. This field should be used only when a suitable more specific field is not available. Use semicolons (;) between separate comments, or place them in separate [comments] entries.  
UISIC field [CA53](http://www.uisic.uis-speleo.org/exchange/atendefn.html#53).

**\<cave-system\>**  *string, maxOccurs=1*  
On occasion, it is discovered that two named caves are connected with one another, and hence form a single cave. The caves keep their individual names and the whole is referred to as a cave system. Another type of cave system is a lava tube with collapsed portions that divide the conduit into segments. A record in the database can be a cave (with one or more branches or segments) or a cave system (of two or more named caves). Entries can link to the system they are part of using the field [cave-system], which should match the [primary-cave-name] of the cave system. Caves can have a [cave-system] element even if a dedicated record for the cave system does not exist in the database. Vice versa, the entry [branch-name] links the cave system to branches or segments that have their own record (and their own entrances). (Note: A group of caves that are not connected and never were connected do not form a cave system and must be represented by individual entries.)

**\<branch-name\>** *string*    
A [branch-name] is the [principal-cave-name] of named cave branches or cave segments with their own entrances. This field allows a record to be a cave system consisting of named caves that already have their own record in the database. Multiple [branch-name]s should be listed, even if the target records do not exist in the database. The presence of one or more [branch-name] entries identifies a record as a cave system.

**\<reference\>**  *string*  
Bibliographical reference, often abbreviated as "Author et al. (year) doi". Multiple references should be separated by a semicolon or placed in multiple [reference] entries. All references that served as source of the data in the record ought to be entered here. Additional references about the cave can also be entered. A URL can also be a reference.

**\<cave-use\>**  *controlled vocabulary*  
The present use (if any) being made of the cave. Similar to UISIC field [CA41](http://www.uisic.uis-speleo.org/exchange/atendefn.html#41).  
CA41 allows [32 predefined terms](http://www.uisic.uis-speleo.org/exchange/atencode.html#41). This list has been shortened to nine terms: guided tourist cave, self-guided tourist cave, waste disposal, habitation, livestock shelter, water source, mine, shrine, temple.

**\<curation\>**  *string*  
Comments about the curation of database entries. This is a free-form entry, but data curators can choose to use their own standardized terminology or codes.  

Comments
--------

-   All fields are optional *(minOccurs=0)*.
-   Elements without *maxOccurs=1* can be used more than once within a record. (The UISIC refers to this as multi-valued, as opposed to single-valued.)
-   The elements must appear in the order listed above.
-   So far, CaveXML defines only these 21 elements.
-   At this point, the hierarchy is flat. All the elements are at the same level within a record, but this will change in future.

Syntax rules (in support of parsing and querying)
-------------------------------------------------

-   All text is in UTF-8, so characters from many languages can be used.

-   All of the controlled vocabulary, except a few country names, uses only ASCII characters (which is a subset of UTF-8). Hence, there is no need to ever enter non-ASCII characters for those.

-   XML has five **special characters**: ampersand &, single quote ', double quote ", smaller than \<, and larger than \>. That doesn't mean these characters can't be used; it depends on how they are used. For example, \> can be used in front of a number without problem. The special characters can alternatively be expressed by their HTML code, e.g., `&apos;` for an apostrophe.

-   **Almost-numerical entries:** Length entries are usually numbers, but they can also be of the form "\>42000", "\~100", or "2000+". A data type "ExtendedUnsignedInteger" has been created in CaveXML for this purpose. ExtendedUnsignedIntegers are positive integers that can contain a few additional symbols. The symbols "\>" and "\~" are allowed in front of the number. The number should contain no comma or decimal point, and digits after the decimal point are prohibited to avoid ambiguity. The elements [length], [vertical-extent], and [number-of-entrances] are ExtendedUnsignedIntegers and therefore obey the same syntax rules. Length and altitude must be rounded to the nearest whole meter. After the number, a "+" symbol is allowed, which has the meaning "or more" (≥). Only one symbol is allowed in front of the number, but note that "\>\~100" is equivalent to "\~100+". However, "10+" (for the number of cave entrances) is equivalent "\>9".

-   **Altitude** is usually a positive decimal number, but it can also have the following forms: "2227 lower entrance", "2500 coarse", "\~700", "500-700", "\>3500", or "4000 upper entrance, coarse". The term "coarse" refers to an approximate value, and is commonly used because the altitude is either not known more accurately or should not be known more accurately. An [altitude] entry starts either with an ExtendedUnsignedInteger, followed by an optional comment, or it is a range of the form "lownumber-highnumber". There can by more than one altitude in a record, e.g., for different cave entrances. Multiple altitudes must be entered in separate pairs of altitude tags, so each pair of tags contains only one altitude entry.

-   A Digital Object Identifier **(doi)** in [reference] can be automatically converted to a hyperlink by replacing "doi:" with "https://doi.org:" followed by the doi number. The character sequence the parser will look for is "doi:", in lower or upper case.

CaveXML data types
------------------

The use of well-defined data types facilitates storage and querying of the data. Among the built-in XML data types, CaveXML uses or builds on the following three: String, token, and decimal. The character set for a string is UTF-8, which encodes over a million characters, so a string can include characters from many languages. A "token" in XML is a string with insignificant whitespaces ignored. Specifically, a token ignores leading and trailing spaces, internal sequences of consecutive spaces, carriage return, line feed, and tab characters. For example, for the entry \<length\> \~20\</length\>, the leading space will be ignored, because the token representation of the string " \~20" is "\~20". The data type "token" is very helpful when comparing with pre-defined strings or when applying RegEx patterns. The XML data type "decimal" is a floating-point number without exponent notation, and is ideal for representing latitude and longitude.

XML allows the writers of Schema to add restrictions to a built-in data type. One type of restriction for a string or token is a pre-defined list of strings, for example the list of all countries in the world. The use of pre-defined terms (a controlled vocabulary) is obviously helpful for queries. Entries that are not on the list of pre-defined strings are not valid within CaveXML (i.e., an error will occur when the XML database entries are validated against the XML Schema) and will therefore already be identified during the data compilation stage.

For quantities such as length or vertical extent, it is desirable to allow entries such as \>5000, \~100, and 7+. The cave is at least 5000 meters long; it is approximately 100 meter deep, and has 7 or more entrances. A purely numerical data type would be too restrictive. For this purpose, CaveXML defines the user-derived data type ExtendedUnsignedInteger, which can represent such patterns. The ExtendedUnsignedInteger allows one of two symbols in front of the number: \~ (approximate) or \> (larger than). The number is an integer of any length, without commas or periods. This choice was made because commas and periods can lead to ambiguities, such as "2,007". In some countries the decimal point is a period, in others it is a comma. Lengths and depths can rarely be defined more accurately than one meter, e.g., one can ponder to what extent the diameter of the cave should be part of its length. Hence, integers suffice to represent length, vertical extent, and, in any case, the number of cave entrances. In accordance with the UISIC recommendation, CaveXML defines the vertical extent as positive, so an unsigned representation is perfect. Technically, an ExtendedUnsignedInteger is defined within the CaveXML Schema as token restricted by a RegEx pattern, namely `[~>]?[0-9]+[+]?`. Those familiar with RegEx understand that this pattern is consistent with expressions such as \>5000, \~100, 7+, and with all integers. Examples of non-matching patterns are: 123.4, \>\~2000, 100-200, and anything that contains a letter. Note that \>\~2000 is equivalent to \~2000+, and the latter is a valid ExtendedUnsignedInteger.

Entries for altitude (elevation) can be even more varied, e.g., "1220-1570" to indicate the range of altitudes from the lowest to the highest entrance. The UISIC recommends an element [altitude-comment] so the meaning of the numerical value for the altitude could be clarified, e.g. "1220 lower entrance", or "2500 coarse" to indicate the altitude is approximate. For caves with more than one entrance, multiple altitude entries might be needed. The goal is of course that the altitude must be queryable numerically, e.g., the user would search for caves with altitudes above 4000 m a.s.l. It can be decided later whether \~4000 and \>3000 should be compatible with this condition or not. After considering various options, the implementation chosen for CaveXML was to have a single "altitude" element which can hold specific patterns of numbers and strings. An unsigned integer or an ExtendedUnsignedInteger can be followed by a comment. These comments may be be ignored during a query, so few restrictions are placed on their form. Alternatively, a range of integers can be stated, such as 100-200, and not followed by a comment. A query function can convert "100-200" into two altitude entries of the form "100 lowermost entrance" and "200 uppermost entrance". Allowing ranges to be entered is convenient for the person who compiles the data. Technically, the data type for the altitude element is implemented as a token (string) restricted by a RegEx pattern. The comments allowed as part of an altitude entry are those consistent with the RegEx pattern `"[ ,()\w^-^;]\*"`, that is, they can contain spaces, commas, parentheses, and alphanumerical characters. Dashes are not allowed in a comment following an altitude value, because a parsing function might use the dash to distinguish between a range and an entry with a single number. A semicolon is not allowed because it is the designated field separator for the flattened database, when repeat elements are merged into a single element.

This concludes the description of all the data types that have, so far, been defined in the CaveXML Schema. Table 1 shows the data types associated with each CaveXML element. None of the elements is required to appear in a record, and some elements can occur no more than once.

| Element               | XML_data_type | Restrictions | Example |  
|:----------------------|:-------------:|:------------:|:--------|  
|\<country-name\> | token with restriction | pre-defined list of strings | Austria |  
|\<state-or-province\> | string | - | Salzburg |  
|\<phys-area-name\> | string | - | Pyrenees |
|\<principal-cave-name\>| string | maxOccurs=1 | Kolowrathöhle |  
|\<other-cave-name\> | string | - | M-340 |
|\<cave-id\> | token with restriction | RegEx pattern | AT-1547/9 |
|\<latitude\> | decimal with restriction | range -90...+90, maxOccurs=1 | 47.72792 |
|\<longitude\> | decimal with restriction | range -180...+180, maxOccurs=1 | 13.00858 |
|\<altitude\> | token with restriction | RegEx pattern | \~1500 main entrance |
|\<length\> | ExtendedUnsignedInteger | maxOccurs=1 | \>5000 |
|\<vertical-extent\> | ExtendedUnsignedInteger | maxOccurs=1 | 240 |
|\<number-of-entrances\>| ExtendedUnsignedInteger | maxOccurs=1 | 7+ |
|\<rock-type\> | token with restriction | pre-defined list of strings | limestone |
|\<cave-type\> | token with restriction | pre-defined list of strings | glacier cave |
|\<contents\> | token with restriction | pre-defined list of strings | waterfall(s) |
|\<comments\> | string | - | Mauna Loa flow of 1855 |
|\<cave-system\> | string | maxOccurs=1 | Labyrinth Cave System | 
|\<branch-name\> | string | -| Arnold Ice Cave |
|\<reference\> | string | - | Yonge et al. (2018) doi:10.1016/B978-0-12-811739-2.00015-2 |
|\<cave-use\> | token with restriction | pre-defined list of strings | guided tourist cave |
|\<curation\> | string | - | updated length Nov 20, 2020 -NS |


Table 1: Data types for each CaveXML element. Default attributes are minOccurs=0 and maxOccurs=unbounded. The third column shows restrictions on the element or on its value. The last column shows examples of valid entries.
