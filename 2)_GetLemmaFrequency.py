import time
begin = time.time()

import spacy
import glob
import operator

nlp = spacy.load('fr_core_news_lg')
dossier = glob.glob('ESLO_modified//*')

encodage = {
	'ã¢': 'â',
	'Ã¢': 'é',
	'Ãª': 'ê',
	'Ã¹': 'ù',
	'Ã»': 'û',
	'Ã§': 'ç',
	'ã¨': 'è',
	'Ã¨': 'è',
	'Ã': 'à',
}

lemme = []
frequence = {}

for fichier in dossier:
    with open(fichier, 'r', encoding='utf-8') as f:
        for i in f:
            doc = nlp(i)
            for token in doc:
                lemme.append(str(token.lemma_))

        for lem in lemme:
            print(lemme)
            if lem in frequence:
                frequence[lem] += 1
            else:
                frequence[lem] = 1
frequence = sorted(frequence.items(), key=operator.itemgetter(1))
frequence.reverse()

with open('Vocab_ESLO.txt', 'w', encoding='utf-8') as out:
    for tup in frequence:
        out.write(str(tup)+'\n')

end = time.time()
temps = end-begin
minutes = round((temps / 60),2)
print('Temps d\'execution : '+str(minutes)+' minute.s.')