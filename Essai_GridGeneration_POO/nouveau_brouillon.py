from word2grid import page_par_liste as ppl



in_datas = [x.replace(' ', '\t').replace('\n','').lower().split('\t') for x in open('fichier_exemple.txt', encoding='utf-8')]
for i in range(0,len(in_datas)):
    if in_datas[i][1] == 'false':
        in_datas[i][1] = False
    if in_datas[i][1] == 'true':
        in_datas[i][1] = True
    if in_datas[i][2] == 'none':
        in_datas[i][2] = None


essai = ppl.main(in_datas)
print(essai)
print(len(essai))