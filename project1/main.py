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
	stopfile = '/media/sf_Share/stopword_ko.csv'
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
	vocab_ko = sorted(vocab_ko.items(), key =lambda x: x[1], reverse=True)

	vocab_hr = [k for k, v in vocab_ko if v>4]
	vocab_lr = [k for k, v in vocab_ko if v<=4]

	return vocab_ko, vocab_hr, vocab_lr, noun_fo

def writeResult(vocab_fin, noun_fo):
	# English
	f = open("/home/yunjung/capstone_kor/noun_fo.txt", 'w')
	f.write(', '.join(noun_fo))
	f.close()
	# Vocab_Fin
	f = open("/home/yunjung/capstone_kor/vocab_fin.txt", 'w')
	f.write("\n".join(vocab_hr))
	f.close()
	# stt전송형식
	# f = open("/home/yunjung/capstone_kor/word_request.txt", 'w')
	# f.write(',\n'.join(M))
	# f.close()

if __name__ == '__main__':
	url = '/media/sf_Share/예술.pdf'
	text = openFile(url)
	clean_txt = cleanText(text)
	stopset = getStopwords()
	vocab, vocab_hr, vocab_lr, noun_fo = getWords(clean_txt, stopset)
	vocab_lr_new = lrw.extractWord(vocab_lr)
	vocab_fin = vocab_hr + vocab_lr_new
	# M = []
	# for i in vocab:
	# 	 M.append('{ \"value\" : \"'+i[0]+'\", "boost" :'+str(i[1])+' }')
	# json.dumps(M)
	# print(M)
	writeResult(vocab_fin, noun_fo)

	print("Success")


