import time
begin = time.time()

import spacy

frequence = {}

with open('name.txt', 'r', encoding='utf-8') as f:
    for i in f:
        doc = nlp(i.replace('\n',''))
        for token in doc:
            if token.lemma_ in frequence:
                frequence[token.lemma_] += 1
            else:
                frequence[token.lemma_] = 1
frequence = sorted(frequence.items(), key=operator.itemgetter(1))
frequence.reverse()
with open('Vocab_ESLO.txt', 'w', encoding='utf-8') as out:
    for key, value in frequence:
        out.write(str(key) + '\t' + str(value) + '\n')
