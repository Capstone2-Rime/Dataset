# 들어오는 텍스트: 하나의string
# 띄어쓰기, 맞춤법은 옳다고 가정하겠음 (강의/회의자료, 사전자료이기 때문)
# 영어 두글자 이하 지우기 /url, email 삭제
from hanspell import spell_checker
import re
#text = '마춤뻡 검사가 시원찬은것 같아요.'
#result = spell_checker.check(text).checked
#print(result)
#text_runs = [re.sub('[-−+=_:;#/?:$/|\@^*[\]{\}(\)<\`\>~0123456789]', ' ', i) for i in text_runs]

def clean_txt(text):
    text = text.strip()
    #한글자모
    text = re.sub('([ㄱ-ㅎㅏ-ㅣ]+)', '', text)
    #Email
    text = re.sub('([a-z0-9_.+-]+@[a-z0-9-]+\.[a-z0-9-.]+)', ' ', text)
    #URL
    text = re.sub('(http|ftp|https|uhttp|$uhttp)://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', ' ', text)
    #html태그
    text = re.sub(r'<[^>]+>', ' ', text)
    #제1, 제2
    text = re.sub(r'[제]+\d+', ' ', text)
    #특수문자 
    text = re.sub('[^\w]', ' ', text)
    text = re.sub('_', ' ', text)
    #숫자정리
    text = re.sub(r'\d+','', text)# remove number
    #lower case
    text = text.lower()
    #짧은영어
    shortword = re.compile(r'[a-zA-Z]*\b[a-zA-Z]{1,2}\b')
    #shortword = re.compile(r'\W*\b\w{1,2}\b')
    text = shortword.sub('', text)
    #space처리
    text = re.sub(r'\s+', ' ', text) 
    text = re.sub(r"^\s+", '', text)#from start
    text = re.sub(r'\s+$', '', text)#from end
    return text

def check_spell(text):
    spelled_sent = spell_checker.check(text)
    text = spelled_sent.checked
    return text

