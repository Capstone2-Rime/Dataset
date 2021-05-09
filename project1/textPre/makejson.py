import json
from collections import OrderedDict

def makejson(url, wordlist):
    config = OrderedDict()
    config["languageCode"] = "ko-KR"
    config["speechContexts"] = [{"phrases" : wordlist}]
    with open(url + 'PDFPPT_dataset.json', 'w', encoding='utf-8') as make_file:
        json.dump(config, make_file, ensure_ascii=False, indent='\t')
    print(".json created")
