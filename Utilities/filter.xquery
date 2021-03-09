(: Run with:
saxonb-xquery -q:filter.xquery
:)

let $sourceURL := "https://github.com/nschorgh/CaveXML/raw/master/allcaves-database.xml"
let $doc := doc( $sourceURL ) 
let $doc := doc("CaveXML/allcaves-database.xml")
let $NL := "&#10;"

for $rec in $doc/CaveDataBase/record
    where $rec/contents = 'permanent ice'
    (: where $rec/cave-type = 'lava tunnel' :)
    return fn:concat($rec/country-name/text(), ' ', $rec/principal-cave-name/text() , $NL)

