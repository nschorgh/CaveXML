CaveXML Definitions
===================

> "The systematic documentation, mapping and publication of data about caves (excepting entrance locations) is a responsibility of all users of the cave environment, and should be encouraged by management authorities."  
> *Guidelines for Cave and Karst Protection*, Working Group on Cave and Karst Protection (1997)

CaveXML facilitates exchange of data about caves through the definition and implementation of a data interchange format. The CaveXML standard defines a set of XML elements and their meaning, as described below. Its syntax is implemented in an XML Schema Definition (`cavexml.xsd`). As a pilot project, basic data for a few thousand caves has been organized in CaveXML format.  

The Informatics Commission of the International Union of Speleology (UISIC) has drafted guidelines for a data exchange standard with over 700 fields. CaveXML builds on these recommendations for the much smaller number of elements it uses.  

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
Country name where the cave entrance is located. This should be the name of the country spelled out and according to the ISO 3166 standard, although a few country names have been simplified. (The precise list is found in the CaveXML Schema Definition `cavexml.xsd`). Similar to UISIC field [SY285](http://www.uisic.uis-speleo.org/exchange/atendefn.html#285)  
For extraterrestrial caves, this element specifies the planetary body where the cave is located. Allowed terms are "Moon", which refers to Earth's moon, "Mars", and a few more. An empty or missing entry implies the cave is located on planet Earth.  

**\<state-or-province\>**  *string*  
State or province where the cave entrance is located. This can also be a county or district. [state-or-province] is intended for politically or organizationally defined areas below country level. For geologically or physically defined units, use [phys-area-name] instead. If more than one region is entered, it is recommended that they be ordered from large to small, e.g. first 'California' then 'Lassen county', and not the other way round.      
Generalization of UISIC field [SY287](http://www.uisic.uis-speleo.org/exchange/atendefn.html#287)

**\<phys-area-name\>**  *string*  
Name of mountain, volcano, mountain range, island, massif, geologic unit, or another physically-defined unit. Example: Pyrenees. For politically-defined regions use [state-or-province] instead. Parks also belong in this field. If more than one region is entered, it is recommended that they be ordered from large to small, e.g. first 'Canary Islands' then 'Mount Teide'.

**\<principal-cave-name\>**  *string, maxOccurs=1*    
The current formal agreed name for a cave or karst feature, expressed in the local language. The character set is UTF-8, so characters from many languages can be used.    
UISIC field [CA70](http://www.uisic.uis-speleo.org/exchange/atendefn.html#70)

**\<other-cave-name\>**  *string*  
Further names which a cave or karst feature has or has had beyond its current name as given in [principal-cave-name].    
Similar to UISIC field [CA69](http://www.uisic.uis-speleo.org/exchange/atendefn.html#69)

**\<cave-id\>**  *(special string)*  
National cave identification number: optional 3-letter or 4-letter organization code + cave registry number, separated by dashes, e.g. HSS-234/7, where HSS stands for Hawaii Speleological Survey. For small countries, this might just be the national cave identification number or cadastral number, e.g. 1234/5. The [cave-id] is restricted to ASCII characters and must not contain whitespaces. The organization code, if used, must use capital letters.  
Similar to UISIC field [CA227](http://www.uisic.uis-speleo.org/exchange/atendefn.html#227) and to the "international cave number". A record is allowed to have more than one [cave-id]. Different caves within the same country are meant to have different [cave-id]s, but this is not required by the CaveXML standard.  

**\<latitude\>**  *-90 ≤ decimal ≤ +90, maxOccurs=1*  
The N-S latitude of the cave entrance or karst feature, expressed as +/- degrees and decimal degrees. Positive if north of the equator, negative if south of the equator. Expressed as a decimal number, rather than as degrees, minutes, and seconds. If [latitude] is given, [longitude] must also be provided. If both [latitude] and [longitude] have only one or two significant digits after the decimal point, they have been rounded in order not to reveal the exact location. Adding trailing zeros would indicate a coordinate is exact rather than rounded.   
UISIC fields [CA245](http://www.uisic.uis-speleo.org/exchange/atendefn.html#245) (exact) or [CA21](http://www.uisic.uis-speleo.org/exchange/atendefn.html#21) (coarse)

**\<longitude\>**  *-180 ≤ decimal ≤ +180, maxOccurs=1*  
The E-W longitude of the cave entrance or karst feature, expressed as +/- degrees and decimal degrees. Positive if east of Greenwich, or negative if west of Greenwich. Expressed as a decimal number, rather than as degrees, minutes, and seconds. If [longitude] is given, [latitude] must also be provided. If both [latitude] and [longitude] have only one or two significant digits after the decimal point, they have been rounded in order not to reveal the exact location. Adding trailing zeros would indicate a coordinate is exact rather than rounded.     
UISIC fields [CA246](http://www.uisic.uis-speleo.org/exchange/atendefn.html#246) (exact) or [CA22](http://www.uisic.uis-speleo.org/exchange/atendefn.html#22) (coarse)

**\<altitude\>**  *(special string)*  
Altitude or range of altitudes of cave entrance(s) in meters above sea level, followed by an optional comment that can be used to clarify the nature of the entry. Multiple [altitude] entries are allowed in a single record. Examples: \~2500 main entrance, 2227 lower entrance, 2227-2500. And altitude can be preceded by > or ~. If a range of altitudes is provided, it should represent the altitudes of the lowest and highest entrance of a cave, and not an uncertainty in altitude. The latter should be indicated with a "\~" sign in front of the number.  
Similar to UISIC fields [CA442](http://www.uisic.uis-speleo.org/exchange/atendefn.html#442) (altitude) and [CA670](http://www.uisic.uis-speleo.org/exchange/atendefn.html#670) (altitude-comment) combined.

**\<length\>**  *ExtendedUnsignedInteger, maxOccurs=1*  
The aggregate length of the cave passages in meters, usually obtained by summing the lengths of all surveyed distances. Length differs from horizontal extent. The length must be rounded to the nearest integer. The unit must be meters, not kilometers or feet. Symbols ~ and > are allowed in front of the number.   
UISIC field [CA56](http://www.uisic.uis-speleo.org/exchange/atendefn.html#56)

**\<vertical-extent\>**  *ExtendedUnsignedInteger, maxOccurs=1*  
The overall vertical distance in meters between the highest and lowest known points of the cave or karst feature, expressed as an unsigned value. (Sometimes vertical extent is defined as the vertical distance between the highest and lowest survey station.) The vertical extent must be rounded to the nearest meter. Symbols ~ and > are allowed in front of the number.    
UISIC field [CA511](http://www.uisic.uis-speleo.org/exchange/atendefn.html#511)

**\<number-of-entrances\>**  *ExtendedUnsignedInteger, maxOccurs=1*  
The total number of entrances to the cave, whether they are numbered or not. Normally provided only if there is more than one entrance. This is usually a positive integer, but expressions such as \>5, 10+, and ~100 are allowed.  
UISIC field [CA9](http://www.uisic.uis-speleo.org/exchange/atendefn.html#9)

**\<rock-type\>**  *controlled vocabulary*  
Type(s) of rock in which the cave or karst feature is formed from, selected from a pre-defined list of options.
Similar to UISIC field [CA7](http://www.uisic.uis-speleo.org/exchange/atendefn.html#7).
[List of options:](http://www.uisic.uis-speleo.org/exchange/atencode.html#7) *limestone, dune limestone, dolomite, marble, basalt, dolerite, granite, gypsum, ice, lava, magnesite, mudstone, quartzite, sandstone, soil, tuff*.
More than one [rock-type] can be entered, e.g. for a cave in ice with a basalt floor.  

**\<cave-type\>**  *controlled vocabulary*  
The cave type(s) based on formation process and selected from a pre-defined list of terms.
List of options: *solution cave, artificial cave, boulder cave, glacier cave, lava tunnel, lava vent, tectonic cave, eolian cave, piping cave, sea cave, weathering cave, misc. type*.  "Boulder caves" are also known as "talus caves". The term "lava tunnel" is equivalent to "lava tube", and "lava tube" and "lava vent" are subcategories of volcanic caves. Eolian (wind), piping (suffosion), sea (littoral), and frost weathering (frost wedging) caves are types of "erosional caves". UISIC field [CA8](http://www.uisic.uis-speleo.org/exchange/atendefn.html#8) lists [similar options](http://www.uisic.uis-speleo.org/exchange/atencode.html#8).  

**\<contents\>**  *controlled vocabulary*  
What the cave contains. Similar to UISIC field [CA72](http://www.uisic.uis-speleo.org/exchange/atendefn.html#72).  
List of options: *permanent ice, periodic ice, extensive guano, many bats, occasional bats, birds, fish, snakes, trogloxenes, accidental trogloxenes, troglophiles, troglobites, charcoal, paintings, minerals, lake(s), waterfall(s), tree roots, perennially submerged, intermittently submerged, perennially part-submerged, intermittently part-submerged*. CA72 has [36 allowed options](http://www.uisic.uis-speleo.org/exchange/atencode.html#72), which have been shortened to 18, and the four terms about submersion are borrowed from [CA2](http://www.uisic.uis-speleo.org/exchange/atendefn.html#2). If the desired entry is not available among the list of terms, enter it in [comments] instead.

**\<comments\>**  *string*  
Comments about a cave or karst feature. This field should be used only when a suitable more specific field is not available. Use semicolons (;) between separate comments, or place them in separate [comments] entries.  
UISIC field [CA53](http://www.uisic.uis-speleo.org/exchange/atendefn.html#53).

**\<cave-system\>**  *string, maxOccurs=1*  
On occasion, it is discovered that two named caves are connected with one another, and hence form a single cave. The caves keep their individual names and the whole is referred to as a cave system. Another type of cave system is a lava tube with collapsed portions that divide the conduit into segments. A record in the database can be a cave (with one or more branches or segments) or a cave system (of two or more named caves). Entries can link to the system they are part of using the field [cave-system], which should match the [primary-cave-name] of the cave system. Caves can have a [cave-system] element even if a dedicated record for the cave system does not exist in the database. Vice versa, the entry [branch-name] links the cave system to branches or segments that have their own record (and their own entrances).  
(A group of caves that are not connected and never were connected do not form a cave system and must be represented by individual entries. If they are in close vicinity of one another, it can be indicated in the [phys-area-name] or [comments] fields.)

**\<branch-name\>**  *string*    
A [branch-name] is the [principal-cave-name] of named cave branches or cave segments with their own entrances. This field allows a record to be a cave system consisting of named caves that already have their own record in the database. Multiple [branch-name]s should be listed, even if the target records do not exist in the database. The presence of one or more [branch-name] entries identifies a record as a cave system.

**\<reference\>**  *string*  
Bibliographical reference, often abbreviated as "Author et al. (year) doi". Multiple references must be placed in separate [reference] entries. All references that served as source of the data in the record ought to be entered here. Additional references about the cave can also be entered. A URL can also be a reference.

**\<cave-use\>**  *controlled vocabulary*  
The present use (if any) being made of the cave. Similar to UISIC field [CA41](http://www.uisic.uis-speleo.org/exchange/atendefn.html#41).  
CA41 allows [32 predefined terms](http://www.uisic.uis-speleo.org/exchange/atencode.html#41). This list has been shortened to nine terms: *guided tourist cave, self-guided tourist cave, waste disposal, habitation, livestock shelter, water source, mine, shrine, temple*.

**\<curation\>**  *string*  
Comments about the curation of database entries. This is a free-form entry, but data curators can choose to use their own standardized terminology or codes.  


Syntax rules (in support of parsing and querying)
-------------------------------------------------

-   All fields are optional *(minOccurs=0)*.

-   Elements with *maxOccurs=1* can appear at most once within a record, whereas the default is *maxOccurs=unbounded*. (The UISIC refers to this as multi-valued, as opposed to single-valued.)

-   CaveXML defines only these 21 elements, although additional elements may be added in future. No other elements are allowed, but there may be ways of adding a second namespace.

-   The elements must appear in the order listed above.

-   Text uses the UTF-8 character set, so characters from many languages can be used.

-   XML has five **special characters**: ampersand &, single quote ', double quote ", smaller than \<, and larger than \>. That doesn't mean these characters can't be used; it depends on how they are used. For example, \> can be used in front of a number without problem. The special characters can alternatively be expressed by their HTML code, e.g., `&apos;` for an apostrophe.

-   **Almost-numerical entries:** Length entries are usually numbers, but they can also be of the form "\>42000", "\~100", or "2000+". A data type "ExtendedUnsignedInteger" has been created in CaveXML for this purpose. ExtendedUnsignedIntegers are positive integers that can contain a few additional symbols. The symbols "\>" and "\~" are allowed in front of the number. The number should contain no comma or decimal point, and digits after the decimal point are prohibited to avoid ambiguity. The elements [length], [vertical-extent], and [number-of-entrances] are ExtendedUnsignedIntegers and therefore obey the same syntax rules. Length and altitude must be rounded to the nearest whole meter. After the number, a "+" symbol is allowed, which has the meaning "or more" (≥). Only one symbol is allowed in front of the number, but note that "\>\~100" is equivalent to "\~100+". However, "10+" (for the number of cave entrances) is equivalent "\>9".

-   **Altitude** is usually a positive decimal number, but it can also have the following forms: "2227 lower entrance", "2500 coarse", "\~700", "500-700", "\>3500", or "4000 upper entrance, coarse". The term "coarse" refers to an approximate value, and is commonly used because the altitude is either not known more accurately or should not be known more accurately. An [altitude] entry starts either with an ExtendedUnsignedInteger, followed by an optional comment, or it is a range of the form "lownumber-highnumber". There can by more than one altitude in a record, e.g., for different cave entrances. Multiple altitudes must be entered in separate pairs of altitude tags, so each pair of tags contains only one altitude entry.

-   A Digital Object Identifier **(doi)** in [reference] can be automatically converted to a hyperlink by replacing "doi:" with "https://doi.org:" followed by the doi number. The character sequence the parser will look for is "doi:", in all lower or all upper case.


CaveXML data types
------------------

The use of well-defined data types facilitates storage and querying of the data. Among the built-in XML data types, CaveXML uses or builds on the following three: String, token, and decimal. The default character set for a string is UTF-8, which encodes over a million characters, so a string can include characters from many languages. A "token" in XML is a string with insignificant whitespaces ignored. Specifically, a token ignores leading and trailing spaces, internal sequences of consecutive spaces, carriage return, line feed, and tab characters. For example, the token representation of the string " \~20" is "\~20". The data type "token" is obviously helpful when comparing with pre-defined strings or when applying RegEx patterns. The XML data type "decimal" is a floating-point number without exponent notation, and is ideal for representing latitude and longitude.

XML allows the writers of Schema to add restrictions to a built-in data type. One type of restriction for a string or token is a pre-defined list of strings, for example the list of all countries in the world. The use of pre-defined terms (a controlled vocabulary) is obviously helpful for queries. Entries that are not on the list of pre-defined strings are not valid within CaveXML (i.e., an error will occur when the XML database is validated against the XML Schema) and will therefore already be identified during the data compilation stage.

The [cave-id] field can consistent of alphanumeric characters and other common ASCII characters, but does not allow whitespace. Technically this is implemented as a RegEx pattern that allows ASCII codes from 33 to 126, `[!-~]*`. (The ASCII code for a space is 32. Whitespaces are allowed at the beginning and the end, because [cave-id] is a token rather than a string.) The organization code, which can be part of the cave id, must consist of 3 or 4 capital letters, but because it is optional, this does not place any restriction on the syntax allowed in this field.     

For quantities such as length or vertical extent, it is desirable to allow entries such as \>5000, \~100, and 7+. The cave is at least 5000 meters long; it is approximately 100 meter deep, and has 7 or more entrances. A purely numerical data type would be too restrictive. For this purpose, CaveXML defines the user-derived data type ExtendedUnsignedInteger, which can represent such patterns. An ExtendedUnsignedInteger allows one of two symbols in front of the number: \~ (approximate) or \> (larger than). The number is an integer of any length, without commas or periods. This choice was made because commas and periods can lead to ambiguities, such as "2,007", which could be interpreted as approximately 2&nbsp;km or approximately 2&nbsp;m. In some countries the decimal point is a period, in others it is a comma. Lengths and depths can rarely be defined more accurately than one meter anyway. Hence, integers suffice to represent length, vertical extent, and, in any case, the number of cave entrances. In accordance with the UISIC recommendation, CaveXML defines the vertical extent as positive, so an unsigned representation is perfect. Technically, an ExtendedUnsignedInteger is defined within the CaveXML Schema as token restricted by a RegEx pattern, namely `[~>]?[0-9]+[+]?`. Those familiar with RegEx understand that this pattern is consistent with expressions such as \>5000, \~100, 7+, and with all integers. Examples of non-matching patterns are: 123.4, \>\~2000, 100-200, and anything that contains a letter. Note that for a floating-point number \>\~2000 is practically equivalent to \~2000+, and the latter is a valid ExtendedUnsignedInteger.

Entries for altitude (elevation) can be even more varied, e.g., "1220-1570" to indicate the range of altitudes from the lowest to the highest entrance. The UISIC recommends an element [altitude-comment] so the meaning of the numerical value for the altitude could be clarified, e.g. "1220 lower entrance", or "2500 coarse" to indicate the altitude is approximate. For caves with more than one entrance, multiple altitude entries might be needed. The altitude must be queryable numerically, e.g., the user would search for caves with altitudes above 4000 m a.s.l. It can be decided later whether \~4000 and \>3000 should be compatible with this condition or not. After considering various options, the implementation chosen for CaveXML was to have a single [altitude] element which can hold specific patterns of numbers and strings. Two types of entries are allowed:
i) An unsigned integer or an ExtendedUnsignedInteger optionally followed by a comment. These comments are restricted to ASCII characters, or even an subset thereof, and may be ignored during a query.
ii) Alternatively, a range of integers can be stated, such as 100-200, and not followed by a comment. A query function can convert "100-200" into two altitude entries of the form "100 lowermost entrance" and "200 uppermost entrance". Allowing ranges to be entered is convenient for the person who compiles the data.
Technically, the data type for the altitude element is implemented as a token restricted by a RegEx pattern. The comments allowed as part of an altitude entry are those consistent with the RegEx pattern `"[ ,()\w]\*"`, that is, they can contain spaces, commas, parentheses, and alphanumerical characters. Other characters, such as dashes and semicolons, are not allowed in a comment following an altitude value. Dashes can be relied on by a parsing function to distinguish between a range and an entry with a single number, because dashes are not allowed within comments.  

This concludes the description of all the data types that have, so far, been defined in the CaveXML Schema. Table 1 shows the data types associated with each CaveXML element. None of the elements is required to appear in a record, and some elements can occur no more than once.

| Element               | XML_data_type | Restrictions | Example |  
|:----------------------|:-------------:|:------------:|:--------|  
|\<country-name\> | token with restriction | pre-defined list of strings | Austria |  
|\<state-or-province\> | string | - | Salzburg |  
|\<phys-area-name\> | string | - | Pyrenees |
|\<principal-cave-name\>| string | maxOccurs=1 | Kolowrathöhle |  
|\<other-cave-name\> | string | - | M-340 |
|\<cave-id\> | token with restriction | RegEx pattern | HSS-1547/9 |
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
|\<branch-name\> | string | -| Blue Grotto |
|\<reference\> | string | - | Yonge et al. (2018) doi:10.1016/B978-0-12-811739-2.00015-2 |
|\<cave-use\> | token with restriction | pre-defined list of strings | guided tourist cave |
|\<curation\> | string | - | updated length based on Smith et al. (2020) |


Table 1: Data types for each CaveXML element. Default attributes are minOccurs=0 and maxOccurs=unbounded. The third column shows restrictions on the element or on its value. The last column shows examples of valid entries.  


Further Discussion
------------------

**Design Principles**  

CaveXML is designed to provide convenience for data entry, while also being strict and logical enough to allow for a great deal of automated data processing. CaveXML brings the power of automation and algorithms to data organization. Here are a few examples:
- A number can be entered as "~500" to mean "approximately 500" or "10+" to mean "10 or more", but only a few specific symbols are allowed in front and after the number to ensure every entry can be successfully parsed and understood.
- Records for caves that are connected with one another can be linked so they can be automatically treated as a single record (cave), if desired.
- For references to the published literature, a doi (digital object identifier) suffices to automatically generate a hyperlink. Even the bibliographic information can be automatically pulled off the internet based purely on the doi, so there is no need for the user to enter this information.
- CaveXML records do not have a catalog number. Unique record identifiers can be generated automatically, when needed.

There is a profound and mutual relation between the data exchange standard and its implementation. *All of the requirements of the data exchange standard can be implemented with an XML schema definition.* More specifically, the requirements can be verified within version 1.0 of XML schema definitions, and do not require the extended capabilities of version 1.1.
For example, if the [cave-id] was required to be unique among records, this could not be verified with an XML schema, because it would require cross-comparisons between records.
Another example are requirements conditioned on other fields. For example, if the data exchange standard required that either [principal-cave-name] or [other-cave-name] must be present, it is not within the capabilities of XML 1.0 to verify that (although it would be possible with XML 1.1). 
This design choice, that the CaveXML data exchange standard can be fully verified with an XML schema definition, has two practical consequences.
First, verifying that a database is consistent with the CaveXML exchange standard requires nothing but an XML validation. No additional software or validation step are necessary.
Second, *all* of the specifications can be verified during the XML validation. Hence, any software used to process CaveXML data can rely on the specifications being followed completely.
This design choice leads to simplicity and rigor. It also protects the standard from making demands that would be difficult to check.   


**Unique record identifier**

CaveXML does not include a catalog number that would uniquely identify a record. This is intentional. There is no fundamental reason data records would require catalog numbers, something that is not a physical property of the cave. And there can be many CaveXML-formatted databases, rather than a single central database, so there would be multiple catalog numbers for the same cave.  

A unique record identifier can be generated in form of a hash code based on the totality of entries in the record. The hash function is a deterministic procedure that turns an input of arbitrary length into an output of fixed length. For example, the MD5 hash generates a 32-character hexadecimal code, and the probability that the same MD5 hash is produced from different inputs is essentially zero. The same record always results in the same hash. When the record is edited, the hash code changes.
Practically, the hash code could be generated based on a limited number of entries, such as [state-or-province], [phys-area-name], and cave names (principal and other). The strings are merged into a single long string that serves as input for a hash code generator. Two caves in close vicinity of each other should not have the same name, so they ought to differ in one of those fields. And if location information is omitted from the record and the cave name is not unique, the ambiguity is fundamental.
Hence, unique record identifiers can be generated automatically from CaveXML data records. They are not permanent, because they change with even minor edits.   

Another approach to generating unique record identifiers would have been to use the country name (or its ISO letter abbreviation) plus the national cave id, if available. Cave ids, such as cave numbers and cadastral numbers, are meant to be unique for each cave. A record may have more than one cave-id and, in principle, could even have more than one [country-name], but as long as a national cave id is available and unique to the cave, it could be used as unique record identifier. There is one infrequent, but serious flaw to this approach, namely that sometimes a cave system inherits its id number from one of its branches, namely when the system of assigning identification numbers is based on entrances. For example, Eisrohrhöhle and the Eisrohrhöhle-Bammelschacht-System both have the cadastral number 1337/118. This introduces fundamental ambiguities, which should be resolved at a level beyond the CaveXML interchange format definitions. An international cave identification number would identify every cave in the world uniquely, but has not yet been established.  

In other words, for CaveXML data the [cave-id] field is not required to be unique and record identifiers are cryptic codes that occasionally change (so they are not suitable for permalinks, unfortunately).
There is another aspect to this choice of solution. Whereas a data interchange standard can require whatever it deems desirable, an XML-validator considers the content of one record at a time and does not perform cross-comparisons to find out whether a [cave-id] entry is also used in another record. This allows to perfectly align the interchange standard with what can be implemented in an XML schema definition, a technically elegant solution, because nothing else but a single XML validation is necessary to verify that a database follows the standard completely.  


**Automated cross-linking between cave systems and their branches**

When a cave system consists of several branches that have their own record in the database, they can be cross-linked. The elements [cave-system] and [branch-name] point to a [principal-cave-name], but cave names might not be unique, even within the same country, so a more sophisticated approach is needed to unambiguously cross-link a cave system with its branches.  When [cave-system] points to a [principal-cave-name], that record should include a [branch-name] that points back to the [principal-cave-name] of the referring record. This two-way reference guarantees that correct cross links have been established, and this identification can be performed automatically.  

The current version of CaveXML allows [cave-system] and [branch-name] to be present simultaneously in the same record, and hence a hierarchy of levels is possible.   


**Character string normalization in support of search queries**

Cave names are ideally written with the characters of the local language, and use of the UTF-8 character set makes this possible. For searches, however, we may prefer to use a more restricted character set, perhaps only the 26 letters of the English alphabet that are contained in the ASCII character set. For example, Scărişoara Cave in Romania should be found in the database by just typing Scarisoara. In Hawaii there is a cave named Kaʻūpūlehu, which one would want to find by just typing Kaupulehu. For this purpose, a function is needed that reduces words written with the UTF-8 character set to an ASCII character set. (In CaveXML, variations in spelling can be entered in the field [other-cave-name], but entering all conceivable variants would be onerous and unnecessary.)  

The ideal transcription of symbols into ASCII characters depends on the language. For example, the German Umlaut 'ü' is properly transcribed as 'ue', but the same character is also used in Azerbaijani, Basque, and Hungarian, where it is better transcribed simply as 'u'. So far, CaveXML provides no mechanism for specifying the language a cave name is written in; a language attribute for cave names would be a welcome upgrade.  

Within the scope of language-independent transcriptions, the Python function 'unidecode' provides lossy ASCII transliterations of Unicode text, and it can serve as a case study for the reduction of cave names into the ASCII character set. Two such Python modules are available: text-unidecode and unidecode. The unidecode function converts 'Scărişoara' into 'Scarisoara'. It also works with non-Latin alphabets. The Korean cave name '쌍용굴' is translated by unidecode to 'sangyonggul', which is indeed a name that is also used for this cave, although it is more often written with a second 'S' in front as 'Ssangyonggul'.
Unidecode does not remove spaces, dashes, or apostrophes. Certainly, we would want to find Aladdin's Cave with or without typing the apostrophe. Hence additional simplifications should be made after applying the unidecode function, including setting all letters to lower case. One possibility is to omit all characters that are not alphanumerical Latin characters, but obviously only after and not before the unidecode function is applied, otherwise there would be nothing left of '쌍용굴'.  

The same function can also be applied to the user input. In that case the database entry "Kaʻūpūlehu" will turn into "kaupulehu", and when the user types "Ka'upulehu", where incidentally a straight single quotation mark is used instead of a curled single quotation mark (the 'okina symbol used in some Polynesian languages), it will also be converted into kaupulehu and match the database entry.
Of course this is not perfect. 'Hoehle' will not match 'Höhle'. However, the case study demonstrates that names can be normalized reasonably well automatically, without placing any constraints on the characters allowed in the cave name field.  


**Scalability**

How many caves are there? The answer will depend on the definition of what constitutes a cave worth cataloging. The Russian Speleological Atlas lists 5,034 caves. An enthusiast in Thailand has compiled a list of 4,749 caves in that country. The US state of Tennessee has over 10,000 caves, more than any other US state. The lava tube data base at Arizona State University contains about 1,755 entries. From these numbers, one might guess that a worldwide database of natural caves significant enough to be worth cataloging would contain on the order of 100,000 records, and national databases will be much smaller. 
This means that a CaveXML database fits easily in memory, whether it be desktop computer, laptop, or cell phone. CaveXML records consist only of text, not photos, maps, or videos, which can only be linked to.  

From a computational point of view, going through a list of this length is lightning fast, so it can be done on-the-fly and basic linear-time search methods suffice. To link records of cave branches that belong to the same cave, cross-comparisons have to be made. Only a fraction of records potentially have interconnections (i.e., either [cave-system] or [branch-name] is present and not empty), so even these cross-comparisons can be performed quickly. CaveXML data can be pre-processed to generate auxiliary entries. This may be convenient, but from a computational point of view, this is unnecessary.
In conclusion, simple methods of storing and searching data are expected to scale up to the expected size of a global CaveXML database.  

