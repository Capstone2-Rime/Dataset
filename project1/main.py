import textPre.pdftxt as pdft
import textPre.ppttxt as pptt
import os
import time
#from konlpy.tag import Mecab
from konlpy.tag import Okt
#from kiwipiepy import Kiwi, Option
start = time.time()
#mecab = Mecab()
okt = Okt()
#kiwi = Kiwi()

# url은 언젠가 업로드되는 주소로 바뀔 것임!
# url = 'C:/Users/이윤정/Desktop/캡디/참고파일/3조 최종데모 발표 자료.pptx'
# url = 'C:/Users/이윤정/Desktop/캡디/사이보그가 되다.pdf'
url = '/media/sf_Share/testpdf.pdf'

if os.path.splitext(url)[1]=='.pdf':
    text = pdft.read_pdf_PDFMINER(url)
    print('filename extension: .ppf')   
elif os.path.splitext(url)[1]=='.pptx':
    text = pptt.read_ppt(url)
    print('filename extenstion: .pptx')
else:
    print("error: unknown filename extension")

#print(mecab.pos(text))
#print(okt.pos(text))
#위치는 나중에 변경할 것
# mecab
#f = open("/home/yunjung/capstone_kor/new.txt", 'w')
#f.write('\n'.join(mecab.morphs(text)))
#f.write('time :'+str(time.time()-start))
#f.close()
# twt
f = open("/home/yunjung/capstone_kor/new_twt.txt", 'w')
f.write('\n'.join(okt.morphs(text)))
f.write('\ntime :'+str(time.time()-start))
print('time :', time.time()-start)
f.close()
# kiwi
#kiwi.prepare()
#a = kiwi.analyze(text)
#print(a)
#f = open("/home/yunjung/capstone_kor/new_kiwi.txt", 'w')
#f.write('time :'+str(time.time()-start))
#print('time:', time.time()-start)
#f.close()
