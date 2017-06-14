# -*- coding: utf-8 -*-
import sys
import codecs
import glob
import math

docs_num = 0
docs_lib = dict()

def get_docs_list (folder_path):			# also updates the docs_num
	global docs_num
	g_scan_path = folder_path + "/*.txt"
	docs_list = glob.glob(g_scan_path)
	docs_num = len(docs_list)
	return docs_list

def update_doc_lib (term):
	if term in docs_lib:
		docs_lib[term] += 1
	else:
		docs_lib[term] = 1

def build_word_vector (docs_list):
	for file in docs_list:
		temp_list = list()
		with codecs.open (file, 'r',encoding="utf8" ) as doc:
			for line in doc:
				line_words = line.split()
				if line_words:
					term = line_words[1]
					if not term in temp_list:
						temp_list.append(term)
						update_doc_lib(term)

def print_docs (docs):
	print ("[")
	for doc in docs:
		print (doc, " : ", docs[doc], "\t")
	print ("] \n")	

def idf (count):
	return math.log((docs_num + 1)/count)

def update_to_idf ():
	for term in docs_lib:
		value = docs_lib[term]
		docs_lib[term] = idf(value)


listd = get_docs_list("source_files")
print ("total different words: ", docs_num)
build_word_vector(listd)
#print_docs (docs_lib)
update_to_idf()
print_docs (docs_lib)

