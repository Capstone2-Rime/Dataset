import textPre.pdftxt as pdft
import textPre.ppttxt as pptt
import textPre.extprocess as prc
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
	stopdata = pd.read_csv(stopfile)
	stopset = list(stopdata.stopword)
	# print(list(stopdata.stopword))
	return stopset

def getWords(text):
	mecab = Mecab()
	pos = mecab.pos(text)
	vocab_ko = {}
	noun_nn = []
	noun_fo = []
	tag_nn = ['NNG','NNP']
	for i in pos:
		if i[1] in tag_nn:
			if i[0] in stopset:
				continue
			noun_nn.append(i[0])
			if i[0] not in vocab_ko:
				vocab_ko[i[0]] = 0
			vocab_ko[i[0]] += 1
		elif i[1]=='SL':
			if len(i[0])>2:
				noun_fo.append(i[0])
	vocab_ko = sorted(vocab_ko.items(), key =lambda x: x[1], reverse=True)
	# print(vocab_ko)
	return vocab_ko, noun_nn, noun_fo

def writeResult(vocab_ko, noun_nn, noun_fo):
	# mecab
	f = open("/home/yunjung/capstone_kor/mecab_nn.txt", 'w')
	f.write(", ".join(noun_nn))
	f.close()
	f = open("/home/yunjung/capstone_kor/mecab_fo.txt", 'w')
	f.write(', '.join(noun_fo))
	f.close()
	f = open("/home/yunjung/capstone_kor/vocab_rank.txt", 'w')
	for k, v in vocab_ko:
		f.write(str(k) + ' : ' + str(v)+'\n')
	f.close()

if __name__ == '__main__':
	url = '/media/sf_Share/testpdf.pdf'
	text = openFile(url)
	clean_txt = cleanText(text)
	stopset = getStopwords()
	vocab, noun_nn, noun_fo = getWords(clean_txt)
	writeResult(vocab, noun_nn, noun_fo)
	print("Success")
