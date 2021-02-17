import time
begin = time.time()

import spacy
import glob
import operator

nlp = spacy.load('fr_core_news_lg')

dossier = glob.glob('ESLO_modified//*')

lemme = {}
for fichier in dossier:
    with open(fichier, 'r') as f:
        for i in f:
            doc = nlp(i)
            for token in doc:
                if token.lemma_ in lemme:
                    lemme[token.lemma_] += 1
                else:
                    lemme[token.lemma_] = 1
lemme = sorted(lemme.items(), key=operator.itemgetter(1))
lemme.reverse()

with open('Vocab_ESLO.txt', 'w') as out:
    for tup in lemme:
        out.write(str(tup)+'\n')

end = time.time()
temps = end-begin
minutes = round((temps / 60),2)
print('Temps d\'execution : '+str(minutes)+' minute.s.')
