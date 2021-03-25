import textPre.pdftxt as pdft
import textPre.ppttxt as pptt
import os

# url은 언젠가 업로드되는 주소로 바뀔 것임!
url = 'C:/Users/이윤정/Desktop/캡디/참고파일/3조 최종데모 발표 자료.pptx'
# url = 'C:/Users/이윤정/Desktop/캡디/사이보그가 되다.pdf'

if os.path.splitext(url)[1]=='.pdf':
    text = pdft.read_pdf_PDFMINER(url)
    print('filename extension: .ppf')   
elif os.path.splitext(url)[1]=='.pptx':
    text = pptt.read_ppt(url)
    print('filename extenstion: .pptx')
else:
    print("error: unknown filename extension")

#위치는 나중에 변경할 것
f = open("C:/Users/이윤정/Desktop/new.txt", 'w')
f.write(text)
f.close()