README
======

CaveXML is a data interchange format for the purpose of facilitating scientific research on caves. This repository provides: CaveXML element and data type definitions, an example database, and a few tools to work with CaveXML-formatted data.  


   [`cavexml.md`](./cavexml.md)	  (explains the CaveXML standard)  
   `cavexml.xsd`		  (XML Schema Definition of CaveXML)  
   `Utilities/cavexml-validate2.py`   (Python program that validates requirements not implemented in cavexml.xsd)   
   `allcaves-database.xml`  (Master version of the database in native format)  
   `allcaves-database.json` (JSON version of the database generated from the XML version)  
   `allcaves-database.csv`  (csv version of the database generated from the XML version)  
   [`https://tinyurl.com/cavedatabase`](https://tinyurl.com/cavedatabase)   (link to GoogleDocs Sheet with simple query functionality)     
   `cavexml-db-table.css`	  (minimalist Style Sheet so the XML database can be viewed in a webbrowser)  
   `Utilities/cavexml2csv.py`         (converts database to comma-separated-values using Python)  
   `Utilities/cavexml-numeric.py`	    (parses quasi-numerical entries; auxiliary utility)   
       

This is a pilot project to explore the capabilities of CaveXML end-to-end. The actual database is for demonstration, and mainly contains ice caves and lava tubes.


## Technical Notes

`cavexml.md` describes the meaning of the XML elements used to organize the data, and restrictions for the entries.

The master copy of the database is in XML format (`allcaves-database.xml`). With the help of `cavexml-db-table.css` the database content can be viewed in a web browser, but this provides a rather poor viewing experience.
An easy way to view and query the database is through GoogleSheets, where a version of the database has been uploaded. The query abilities are still limited, but include numerical searches on quasi-numerical entries.

The Python programs serve as examples for how a CaveXML database can be loaded and analyzed within Python. Parsing functions for quasi-numerical entries are included in `cavexml-numeric.py`.

`cavexml.xsd` incorporates nearly all CaveXML syntax requirements. The following validates a database against the Schema:  

    xmllint --schema cavexml.xsd allcaves-database.xml --noout  

Alternatively, various online tools can be used to validate an XML database against an XSD document. The few requirements that are not validated through `cavexml.xsd` are verified by `cavexml-validate2.py`.

