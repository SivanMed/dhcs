# -*- coding: utf-8 -*-
# coding=utf8
import sys
import codecs
import glob
import math

class Doc_Vector:

	word_vector = dict()

	def check_t_hebrew (self,term):
		if len(term) > 1:
			return all("\u05D0" <= c <= "\u05EA" for c in term)
		return False

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
					if self.check_t_hebrew(term):
						self.update_word_vector(term)
		self.size = self.get_size()


docs_num = 0
docs_vector = dict()
word_dictionary = dict()

def get_docs_list (folder_path):			# also updates the docs_num
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



'''
def update_doc_lib (term):
	if term in docs_lib:
		docs_lib[term] += 1
	else:
		docs_lib[term] = 1

def build_word_vector (docs_list):
	for file in docs_list:		
	#for i in range(3):
		#file = docs_list[i]
		#print ("\t\t",docs_list[i][::-1])
		temp_list = list()
		with codecs.open (file, 'r',encoding="utf8" ) as doc:
			for line in doc:
				line_words = line.split()
				if line_words:
					term = line_words[2]
					if check_t_hebrew (term):
						if not term in temp_list:
							temp_list.append(term)
							update_doc_lib(term)							

'''
def print_docs (docs):
	print ("[")
	for doc in docs:
		print (doc[::-1], " : ", docs[doc], "\t")
	print ("] \n")


build_vectors("source_files")
idf_dict = bulid_idf_table()
print ("total different Docs: ", docs_num)
#build_word_vector(listd)
#print_docs (docs_lib)
#update_to_idf()
print ("total different words: ",len(idf_dict))
#print_docs (docs_lib)