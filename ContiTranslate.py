import json
from deep_translator import GoogleTranslator

ContiList = []
newfile = open('ContiChatTranslate2020.txt', 'w', encoding='utf-8')

with open('ContiChat2020bis.json', encoding='utf-8') as ContiFile:
    for line in ContiFile:
        ContiList.append(json.loads(line))

    for i in range(len(ContiList)):
        try:
            translation = GoogleTranslator(source='auto', target='en').translate(ContiList[i].get('body'))
            ContiList[i]["translation"] = translation
        except Exception as e:
            ContiList[i]["translation"] = e
        print(ContiList[i])
        json.dump(ContiList[i], newfile, ensure_ascii=False)
        newfile.write('\n')

newfile.close()
