import spacy
import re
import operator

nlp = spacy.load('fr_core_news_sm')

name_of_infile = 'name.txt'
name_of_outfile = 'Vocab_ESLO.txt'

lemme = ''
with open(name_of_infile, 'r', encoding='utf-8') as f:
    for ligne in f:
        ligne = re.sub(r'[^\w\s]', '', ligne)
        lemme += ligne.replace('\n', ' ')

frequence = {}
doc = nlp(lemme)
    for token in doc:
        if token.lemma_ in frequence:
            frequence[token.lemma_] += 1
        else:
            frequence[token.lemma_] = 1

frequence = sorted(frequence.items(), key=operator.itemgetter(1))
frequence.reverse()

with open(name_of_outfile, 'w', encoding='utf-8') as out:
    for key, value in frequence:
        out.write(str(key) + '\t' + str(value) + '\n')
