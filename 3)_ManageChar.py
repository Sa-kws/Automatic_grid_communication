import os

propre = []

encodage = {
	'ã¢': 'â',
	'Ã¢': 'é',
	'Ãª': 'ê',
	'Ã¹': 'ù',
	'Ã»': 'û',
	'Ã§': 'ç',
	'ã§': 'ç',
	'ã¨': 'è',
	'Ã¨': 'è',
	'Ã': 'à',
}
with open('Vocab_ESLO.txt', 'r', encoding='utf-8') as infile:
	for ligne in infile:
		for k,v in encodage.items():
			if k in ligne:
				ligne = ligne.replace(k, v)
		if ligne == '\n':
			pass
		else:
			propre.append(ligne)
for j in open('Vocab_ESLO.txt', 'r', encoding='utf-8'):
	pass

with open('Decoded_ESLO_vocab.txt', 'w', encoding='utf-8') as newfile:
	for ligne in propre:
		newfile.write(ligne+'\n')
os.remove('Vocab_ESLO.txt')
