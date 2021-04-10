import textPre.pdftxt as pdft
import textPre.ppttxt as pptt
import textPre.extprocess as prc
import os
import time
import pickle
from konlpy.tag import Mecab
# start = time.time()
mecab = Mecab()

# url은 언젠가 업로드되는 주소로 바뀔 것임!
# url = 'C:/Users/이윤정/Desktop/캡디/참고파일/3조 최종데모 발표 자료.pptx'
# url = 'C:/Users/이윤정/Desktop/캡디/사이보그가 되다.pdf'
url = '/media/sf_Share/경영.pdf'

if os.path.splitext(url)[1]=='.pdf':
    text = pdft.read_pdf_PDFMINER(url)
    print('filename extension: .pdf')   
elif os.path.splitext(url)[1]=='.pptx':
    text = pptt.read_ppt(url)
    print('filename extenstion: .pptx')
else:
    print("error: unknown filename extension")

text = prc.clean_txt(text)
#text = prc.check_spell(text)

# TEXT 저장
#f = open("C:/Users/이윤정/Desktop/new.txt", 'w', encoding='UTF-8')
#f.write(text)
#f.close()

pos = mecab.pos(text)
noun_nn = []
noun_foB = []
tag_nn = ['NNG','NNP', 'SH']
for i in pos:
	if i[1] in tag_nn:
		noun_nn.append(i[0])
	elif i[1]=='SL':
		noun_foB.append(i[0])
# 2글자 이하의 영어 제거
noun_fo = []
for i in noun_foB:
	if len(i)>2:
		noun_fo.append(i)
#print(noun_nn)
#print('\n')
#print(noun_fo)

# mecab
#print(mecab.nouns('한국은 예로부터 tradition을 重視해왔다. 利花가 아름답다. AK 플라자에 가고 싶다. 그녀는 그 일에 대해서 이루 말할 수 없이 슬펐다. 그들은 무엇도, 단 한 개도 제공하지 않았다. 첫째로, 애나는 미국행 비행기 티켓을 끊었다.'))
f = open("/home/yunjung/capstone_kor/mecab_nn.txt", 'w')
f.write(", ".join(noun_nn))
f.close()
f = open("/home/yunjung/capstone_kor/mecab_fo.txt", 'w')
f.write(', '.join(noun_fo))
f.close()
# nouns 시간 계산해서 알아보기
#f = open("/home/yunjung/capstone_kor/mecabnoun.txt", 'w')
#f.write('\n'.join(mecab.nouns(text)))
#f.close()


