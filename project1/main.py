import textPre.pdftxt as pdft
import textPre.ppttxt as pptt
import textPre.extprocess as prc
import textPre.lrword as lrw
import os
import time
import pickle
import pandas as pd
from konlpy.tag import Mecab
import json
# start = time.time()

def openFile(url):
	if os.path.splitext(url)[1]=='.pdf':
		text = pdft.read_pdf_PDFMINER(url)
		print('filename extension: .pdf')   
	elif os.path.splitext(url)[1]=='.pptx':
		text = pptt.read_ppt(url)
		print('filename extenstion: .pptx')
	else:
		print("error: unknown filename extension")
	return text

def cleanText(text):
	t = prc.clean_txt(text)
	# t = prc.check_spell(text)
	return t

def getStopwords():
	stopfile = '/home/yjlee/Desktop/stopword_ko.csv'
	stopdata = pd.read_csv(stopfile, encoding='utf-8')
	stopset = list(stopdata.stopword)
	#print(list(stopdata.stopword))
	return stopset

def getWords(text, stopset):
	mecab = Mecab()
	pos = mecab.pos(text)
	
	vocab_ko = {}
	noun_nn_pre = []
	noun_nn = []
	noun_fo = []
	
	tag_nn = ['NNG','NNP']
	noun_nn_pre = [w[0] for w in pos if w[1] in tag_nn]
	noun_fo = [w[0] for w in pos if w[1]=='SL']
	noun_nn = [word for word in noun_nn_pre if word not in stopset]
	for w in noun_nn:
		if w not in vocab_ko:
			vocab_ko[w] = 0
		vocab_ko[w] += 1
	vocab = sorted(vocab_ko.items(), key =lambda x: x[1], reverse=True)

	vocab_hr = [k for k, v in vocab if v>4]
	vocab_lr = [k for k, v in vocab if v<=4]
	
	pos = [w[0] for w in pos]
	return vocab_ko, vocab, vocab_hr, vocab_lr, noun_fo, noun_nn, pos

def writeResult(vocab_fin, noun_nn, M, pos):
	loc = "/home/yjlee/Desktop/"
	# noun_nn
	f = open(loc + "noun_nn.txt", 'w')
	f.write(', '.join(noun_nn))
	f.close()
	# Vocab_Fin
	f = open(loc + "vocab_fin.txt", 'w')
	f.write("\n".join(vocab_fin))
	f.close()
	# stt전송형식- no weight
	f = open(loc + "w_request.txt", 'w')
	f.write(', '.join(M))
	f.close()
	# pos
	f = open(loc +"raw_pos.txt", 'w')
	f.write(', '.join(pos))
	f.close()

if __name__ == '__main__':

	# DIR WHERE FILE EXISTS
	loc = '/home/yjlee/Desktop/lecNote/'
	
	# line86 : will be deleted soon
	url = loc + 'art.pdf'
	
	# NO NEED TO INPUT FILENAME, ONLY DIR NAME REQUIRED
	# filelist = os.listdir(loc)
	# url = loc + filelist[0]	

	text = openFile(url)	
	clean_txt = cleanText(text)
	stopset = getStopwords()
	vocab_ko, vocab, vocab_hr, vocab_lr, noun_fo, noun_nn, pos = getWords(clean_txt, stopset)

	vocab_lr_new = lrw.extractWord(vocab_lr)
	# print(vocab_lr_new)
	vocab_fin = vocab_hr + vocab_lr_new
	# print(type(vocab_ko))
	M = []
	for i in vocab_fin:
		M.append('{ \"'+ i +'\" }')
		# WEIGHT
		# M.append('{ \"phrases\" : \"'+ i +'\", "boost" :' + str(vocab_ko[i]) + ' }')

	#json.dumps(M)
	
	writeResult(vocab_fin, noun_nn, M, pos)
	
	print(vocab_fin)
	
	print("Success")


