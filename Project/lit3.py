# -*- coding: utf-8 -*-

import csv
import collections
import pandas as pd
import plotly.plotly as py
import plotly.graph_objs as go
import numpy as np
import codecs
import io

vector_dic = dict()

def create_vectors

def do_grafh (from_user):
	input_file= pd.read_csv('Knesset-Protocols-Filtered_utf8.csv') 
	counts = input_file[from_user].value_counts().to_dict()
	freq= counts.values()
	value= counts.keys()
	trace = dict(x=value, y=freq)
	data = [trace]
	layout = dict( xaxis=dict(title=from_user),
				  yaxis=dict(title='number of meetings'))
	fig = dict(data=data, layout=layout)
	py.plot(fig, filename='ia_county_populations')
 
def do_grafh2 (from_user):
	f = open('Knesset-Protocols-Filtered_utf8.csv', 'rb')
	reader = csv.reader(f)	
	rows = list(reader)

user_number = input("""choose your qustion\nhow many meeting have been evey ____ 
1.VAADA_CODE 
2.MOSHAV 
3.YESHIVA_DATE_MONTH
4.YESHIVA_DATE_DAY
5.YESHIVA_DATE_YEAR
6.NOSEH
7.SUG_PEILUT_NAME
8.SUG_PEILUT\n""")
if user_number== 1:
	from_user='VAADA_CODE'
	do_grafh2 (from_user)
elif user_number== 2:
	from_user='MOSHAV'
elif user_number== 3:
	from_user='YESHIVA_DATE_MONTH'
elif user_number== 5:
	from_user='YESHIVA_DATE_YEAR'
elif user_number== 6:
	from_user='NOSEH'
elif user_number== 7:
	from_user='SUG_PEILUT_NAME'
else:
	from_user='SUG_PEILUT'
	
	
do_grafh (from_user)

