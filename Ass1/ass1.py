# coding=UTF-8
import sys
import codecs
import re

#main
OriginalT = 'input.txt'
originalText = codecs.open(OriginalT,'r',encoding='UTF-8')

output = 'output.xml'
ans =codecs.open(output,'w',encoding='UTF-8')
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

tag_list = list()

str = codecs.open('input.txt', 'r',encoding="utf8" ).read()
inner = ""
nl = ""
for line in originalText:
		text = line.split()
		for Origin_word in text:
			with codecs.open('output.txt',encoding="utf8") as source:
				for source_line in source:
					if (Origin_word in source_line) and ("properName" in source_line):
						Origin_word="<properName>"+ Origin_word +"</properName>"+"\n"
						break
					if ("," in Origin_word) and (Origin_word[:-1] in source_line) and ("properName" in source_line):
						Origin_word = "<properName>" + Origin_word + "</properName>" + "\n"
						break

			if (re.findall(r'\d\d\d\d', Origin_word)):
				Origin_word= "<Date>" + Origin_word +"</Date>" +"\n"
			nl = " " + Origin_word + " "
			inner = inner + nl



outputText=meta+"\n"+inner+"\n"+closing

ans.write(outputText)

#def scanForTags (file, tag_list):
#	txt = codecs.open ('output.txt', 'r',encoding="utf8" ).read()
	
