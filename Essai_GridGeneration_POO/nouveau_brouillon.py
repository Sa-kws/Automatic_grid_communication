from word2grid import page_par_liste as ppl

ID = 0
name = 'Page_'+ str(ID)
page = ppl.Page(ID, name)

in_datas = [x.replace(' ', '\t').replace('\n','').lower().split('\t') for x in open('fichier_exemple.txt', encoding='utf-8')]
for i in range(0,len(in_datas)):
    if in_datas[i][1] == 'false':
        in_datas[i][1] = False
    if in_datas[i][1] == 'true':
        in_datas[i][1] = True
    if in_datas[i][2] == 'none':
        in_datas[i][2] = None

'''
used_words = []
grid = ppl.Grid().PAGES

if ppl.Page.isWellSized(ppl.Page, page) == False:
    print(ppl.Page.WARNING_MESSAGE)
    print('Le programme va s\'arrêter.')
else:
    for ligne in in_datas:
        word = ligne[0]
        iscore = ligne[1]
        path = ligne[2]
        #folder_datas = open(word + '.txt', 'r', encoding='utf-8')
        folder_datas = [word]
        grid = ppl.Grid.addFolderPage(path=path, folder_datas=folder_datas, grid=grid, ID=ID)
        grid, page = ppl.Grid.makeGrid(page=page, used_words=used_words, grid=grid, ID=ID, word=word, iscore=iscore)
    grid = ppl.Grid.finishGrid(page=page, grid=grid)
'''
essai = ppl.main(in_datas)
print(essai)