# -*- coding: utf-8 -*-
# coding=utf8
import sys
import codecs
import glob
import math
from operator import itemgetter


class Doc_Vector:

	word_vector = dict()
	'''
	def check_t_hebrew (self,term):
		if len(term) > 1:
			return all("\u05D0" <= c <= "\u05EA" for c in term)
		return False
	'''
	def word_count(self, w):
		if w in self.word_vector:
			return self.word_vector[w]
		else:
			return 0

	def update_word_vector (self, term):
		if term in self.word_vector:
			self.word_vector[term] += 1
		else:
			self.word_vector[term] = 1

	def get_size(self):
		lenth = 0
		for word in self.word_vector:
			lenth += self.word_vector[word]
		return lenth

	def __init__(self, path):
		self.doc_path = path
		with codecs.open (path, 'r',encoding="utf8" ) as doc:
			for line in doc:
				line_words = line.split()
				if line_words:
					term = line_words[2]
					#if self.check_t_hebrew(term):
					self.update_word_vector(term)
		self.size = self.get_size()


docs_num = 0
docs_vector = dict()
word_dictionary = dict()

def get_docs_list (folder_path):	# also updates the docs_num
	global docs_num
	g_scan_path = folder_path + "/*.txt"
	docs_list = glob.glob(g_scan_path)
	docs_num = len(docs_list)
	return docs_list

def build_vectors(folder_path):
	files = get_docs_list(folder_path)
	for file in files:
		with codecs.open (file, 'r',encoding="utf8" ) as folder:
			docs_vector[file] = Doc_Vector(file)	

def idf (count):
	return math.log((docs_num + 1)/count)

def update_to_idf (dic):
	for term in dic:
		value = dic[term]
		dic[term] = idf(value)


def bulid_idf_table():
	if not bool(docs_vector):
		return {}
	word_idf = dict()
	for file in docs_vector:
		for word in docs_vector[file].word_vector:
			if word in word_idf:
				word_idf[word] += 1
			else:
				word_idf[word] = 1

	update_to_idf(word_idf)
	return word_idf


docs_comp = dict()
idf_dict = dict()
k = 0.75
b = 1.6
avgbl = 0

def get_avglb():
	global avgbl
	if avgbl != 0:
		return avgbl
	else:
		total = 0
		for doc in docs_vector:
			total += docs_vector[doc].size
		avgbl = total / docs_num
		return avgbl

def tf (w, D):
	c = D.word_count(w)
	return (c * (k + 1))/(c + k * ( 1 + b + b * (D.size/get_avglb())))

def get_idf(w):
	if w in idf_dict:
		return idf_dict[w]
	else:
		return 0

def bm25(vec, doc):
	sim = 0
	for word in vec.word_vector:
		sim += tf(word, vec) * tf(word, doc) * get_idf(word)
	return sim

def compr (file):
	print ("Comparing, Please wait...")
	vec = Doc_Vector(file)
	for doc in docs_vector:
		docs_comp[doc] = bm25(vec, docs_vector[doc])
	print ("Finished Comparing!")


def print_first(num):
	if docs_comp == {}:
		print ("Please compare a document first")
	else:
		for key in sorted(docs_comp, key= itemgetter(1), reverse = True)[:num]:
			print ("{} : {}".format(key, docs_comp[key]))
			#print (key)


def open_menu():
	menu = """
What would you like to do?
	1. Compare a document to the Data Base.
	2. Get first 10 similar documents.
	3. Get first 100 similar documents.
	4. Print all documents results.
	5. Exit
"""
	print(menu)
	try:
		inpt = input("What option would you like to choose? Num. ")
		if (inpt == '1'):
			file = input ("Enter file (include path):")
			compr(file)
		elif (inpt == '2'):
			print_first(10)
		elif (inpt == '3'):
			print_first(100)
		elif (inpt == '4'):
			print_first(len(docs_comp))
	finally:
		if (inpt == '5'):
			return
		open_menu()


def print_docs (docs):
	print ("[")
	for doc in docs:
		print (doc[::-1], " : ", docs[doc], "\t")
	print ("] \n")

# ====================== main ======================

print("Please Wait a few seconds while we build the Data Base in folder 'source_files'...\n")
build_vectors("source_files")
idf_dict = bulid_idf_table()
print("Completed building the Data Base in folder 'source_files';")
print ("total different Docs in the Data Base: ", docs_num)
print ("total different words in the Data Base: ",len(idf_dict))
open_menu()

