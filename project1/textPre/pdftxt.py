from io import StringIO
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser
import re

def read_pdf_PDFMINER(pdf_file_path):
    """
    pdf_file_path: 'dir/aaa.pdf'로 구성된 path로부터 
    내부의 text 파일을 모두 읽어서 스트링을 리턴함.
    https://pdfminersix.readthedocs.io/en/latest/tutorials/composable.html
    """
    output_string = StringIO()
    with open(pdf_file_path, 'rb') as f:
        parser = PDFParser(f)
        codec = 'utf-8'
        doc = PDFDocument(parser)
        rsrcmgr = PDFResourceManager()
        device = TextConverter(rsrcmgr, output_string, codec=codec, laparams=LAParams())
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        for page in PDFPage.create_pages(doc):
            interpreter.process_page(page)
    v = str(output_string.getvalue())
    return ' '.join(v.split())

# pdf_file_path = 'C:/Users/이윤정/Desktop/캡디/사이보그가 되다.pdf'

# f = open("C:/Users/이윤정/Desktop/new.txt", 'w', encoding='UTF-8')
# f.write(read_pdf_PDFMINER(pdf_file_path))
# f.close()