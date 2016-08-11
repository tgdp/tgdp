# -*- coding: utf-8 -*-


import scipy
import pandas
import codecs
import numpy as np
from collections import defaultdict


#/home/ps/tgdp/summer16/mapping/shortishortue_merged.csv
def outlierremover(spreadsheet, variable, column_name, no_of_stdevs):
	#keep NAs in there
	print "Removing outliers {} stdevs from the mean".format(no_of_stdevs)
	column_mean=np.mean(spreadsheet[spreadsheet['variable']==variable][column_name])
	column_stdev=np.std(spreadsheet[spreadsheet['variable']==variable][column_name])
	#from docs
	# df1.loc[:, df1.loc['a'] > 0]
	print spreadsheet.loc[spreadsheet['variable']==variable]
	print "The mean is {}, the standard deviation is {} for column {}".format(column_mean, column_stdev, column_name)
	#x=t.loc[(t['oF1'] > 700) & (t['variable'] == 'ʏ')]
	outputspread=spreadsheet.loc[((spreadsheet[column_name] > column_mean-(no_of_stdevs*column_stdev))&(spreadsheet[column_name] < column_mean+(no_of_stdevs*column_stdev)))|(spreadsheet['variable'] != variable)]
	print outputspread.describe()
	print outputspread['oF1']
	print "\n\n DIFFERENCE\n before:", spreadsheet.shape, "after", outputspread.shape
	outputspread.to_csv("CSVSCSV.csv")
	return outputspread

#df.loc[(df["B"] > 50) & (df["C"] == 900), "A"]	
	
	
def distancecomputer(input_file, variable_1, variable_2, remove_outliers=True):
	speakerdict=defaultdict()
	with codecs.open(input_file, "r", "utf-8") as inputfile:
		inputspread=pandas.read_csv(inputfile)
	if remove_outliers:
		inputspread=outlierremover(inputspread, variable_1, 'oF1', 1)
		inputspread=outlierremover(inputspread, variable_1, 'oF2', 2)
		inputspread=outlierremover(inputspread, variable_2, 'oF1', 2)
		inputspread=outlierremover(inputspread, variable_2, 'oF2', 2)
	#this makes a groupby object
	#below equals inputspread.groupby(inputspread['speaker_number'])
	t=inputspread.groupby('speaker_number')
	#we convert the k[1] dataframe into a dictionary
	speakerdict={k[0]:k[1].to_dict(orient='list') for k in t}
	for entry in speakerdict:
		for f in ['oF1', 'oF2', 'oF3']:
			speakerdict[entry][f]=[np.float64(i) for i in  speakerdict[entry][f]]
			speakerdict[entry][f+"_mean"]=np.mean([i for i in speakerdict[entry][f] if not np.isnan(i)])
		print speakerdict[entry]['oF1_mean']#speakerdict[entry]['oF2']=[np.float64(i) for i in  speakerdict[entry]['oF2']]
			#speakerdict[entry]['oF1_mean']=np.mean([i for i in speakerdict[entry]['oF1'] if not np.isnan(i)])
			#speakerdict[entry]['oF2']=[np.float64(i) for i in  speakerdict[entry]['oF2']]
			#speakerdict[entry]['oF2_mean']=np.mean([i for i in speakerdict[entry]['oF2'] if not np.isnan(i)])
			#speakerdict[entry]['oF3_mean']=np.mean([i for i in speakerdict[entry]['oF3'] if not np.isnan(i)])
			#print entry, speakerdict[entry]['oF2'], [type(i) for i in speakerdict[entry]['oF2']] , np.mean([i for i in speakerdict[entry]['oF2'] if not np.isnan(i)]),  [np.isnan(i) for i in speakerdict[entry]['oF2']]
	#print inputspread.iloc[0]
	#for i in t:
	
		#print i[1]['dob'].data()
		#i[0] contains the speaker number, the i[1] is the data associated with it
		# speakerdict[i[0]]={
		# 'raw_f1':i[1]['oF1'],
		# 'raw_f2':i[1]['oF1'],
		# 'raw_f3':i[1]['oF1'],
		# 'mean_f1':i[1]['oF1'].mean(),
		# #'mean_f2':i[1]['oF2'].mean(),
		# #'mean_f3':i[1]['oF3'].mean(),
		# #'count_f1':i[1]['oF1'].count(),
		# #'count_f2':i[1]['oF2'].count(),
		# #'count_f3':i[1]['oF3'].count(),
		# #'location':i[1]['location'],
		# 'dob':i[1]['dob']
		# }
	#print speakerdict
	
	outi=pandas.DataFrame.from_dict(speakerdict, orient='index')	
	#speaker_nr, mean_x, mean_y
	#
	
	#print outi
	outi.to_csv("test.csv")	
		
	#print t.sum()
	#
	#t.to_csv("test.csv")
	#this sseems terribly inelegant
	#for speaker in inputspread['speaker_number']:
	#	print speaker
	#	speakerdict[speaker]['f1']=inputspread[inputspread['speaker_number']==speaker]['oF1']
	#	speakerdict[speaker]['f2']=inputspread[inputspread['speaker_number']==speaker]['oF2']
	#print speakerdict
	
	#inputspread.groupby(
	# for speaker in inputspread.groupby(speaker):
		# print speaker
		#make mean F1, F2 of i, make mean F1, F2 of y
		#compute distance
		#also for f1 , f3 




distancecomputer('/home/ps/tgdp/summer16/mapping/shorti_final_FIXED.csvshortue_final_FIXED.csv_merged.csv', 'ʏ', 'ɪ', remove_outliers=False)