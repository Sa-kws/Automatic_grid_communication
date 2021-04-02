import time
begin = time.time()

import csv

locuteurs = []

with open('IN_DATAS/metadatas_locuteurs.tsv', encoding='cp1252', newline='') as xlsx_file:
    spamreader = csv.reader(xlsx_file, delimiter='\t')
    for row in spamreader:
        if row[3] == '- de 5 ans' or row[3] == '5/10':
            with open('OUT_DATAS/child_locuteurs.txt', 'a', encoding='utf-8') as outfile:
                outfile.write(row[1] + '\n')

end = time.time()
temps = end-begin
minutes = round((temps / 60),2)
print('Temps d\'execution : '+str(minutes)+' minute.s.')