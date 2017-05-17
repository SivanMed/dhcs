# coding=UTF-8
import sys
import codecs
import re

#main
OriginalT = 'input.txt'
originalText = codecs.open(OriginalT,'r',encoding='UTF-8')

output = 'output.xml'
outputT =codecs.open(output,'w',encoding='UTF-8')
meta = """<?xml version="1.0" encoding="UTF-8"?>
<?xml-model href="http://www.tei-c.org/release/xml/tei/custom/schema/relaxng/tei_all.rng" type="application/xml" schematypens="http://relaxng.org/ns/structure/1.0"?>
<?xml-model href="http://www.tei-c.org/release/xml/tei/custom/schema/relaxng/tei_all.rng" type="application/xml"
	schematypens="http://purl.oclc.org/dsdl/schematron"?>
<TEI xmlns="http://www.tei-c.org/ns/1.0">
   <teiHeader>
      <fileDesc>
         <titleStmt>
            <title>
               <surname>פרנקל</surname>, <forename>אלונה</forename> (<surname>גולדמן</surname>,
                  <forename>אילונה</forename>) <date when="1937">(1937) </date>
            </title>
         </titleStmt>
         <publicationStmt>
            <p>Publication Information</p>
         </publicationStmt>
         <sourceDesc>
            <p>Information about the source</p>
         </sourceDesc>
      </fileDesc>
   </teiHeader>
   <text>
      <body>"""

closing="""</body>
</text>
</TEI>"""

str = codecs.open('input.txt', 'r',encoding="utf8" ).read()
inner = ""
nl = ""
for line in originalText:
		text = line.split()
		for wordYael in text:
			with codecs.open('Meni_Output.txt',encoding="utf8") as menny:
				for menyLine in menny:
					if (wordYael in menyLine) and ("properName" in menyLine):
						wordYael="<properName>"+ wordYael +"</properName>"+"\n"
						break
					if ("," in wordYael) and (wordYael[:-1] in menyLine) and ("properName" in menyLine):
						wordYael = "<properName>" + wordYael + "</properName>" + "\n"
						break

			if (re.findall(r'\d\d\d\d', wordYael)):
				wordYael= "<Date>" + wordYael +"</Date>" +"\n"
			nl = " " + wordYael + " "
			inner = inner + nl



outputText=meta+"\n"+inner+"\n"+closing

outputT.write(outputText)