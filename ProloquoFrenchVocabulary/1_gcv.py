import time
begin = time.time()

import os, io
from google.cloud import vision
import json
from google.protobuf.json_format import MessageToJson


OUT_FOLDER = 'Proloquo_text_screens'

try:
    os.mkdir(OUT_FOLDER)
except FileExistsError:
    print('Folder already exists')


DOSSIER = 'Proloquo_Screens'
compteur = 0


client = vision.ImageAnnotatorClient()


for fichier in os.listdir(DOSSIER):

    compteur += 1

    INFILE_NAME = fichier
    OUTFILE_NAME = OUT_FOLDER + '/' + (fichier).replace('.PNG', '.json').replace('.jpg', '.json')


    with io.open(os.path.join(DOSSIER, INFILE_NAME), 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)
    response = client.text_detection(image=image)

    full_image_words_annotation = []

    for text in response.text_annotations:
        # x = ordonné
        # y = abscisse
        ocr_annotation = {'DESCRIPTION': text.description,'VERTICES': ['{x : %s, y: %s}' % (v.x, v.y) for v in text.bounding_poly.vertices]}
        full_image_words_annotation.append(ocr_annotation)

    with open(OUTFILE_NAME, 'w', encoding='utf-8') as outfile:
        json.dump(full_image_words_annotation, outfile, indent=4, ensure_ascii=False)

    print(compteur, '--', fichier, '\t Done')


end = time.time()
temps = end-begin
minutes = round((temps / 60),2)
print('Temps d\'execution : '+str(minutes)+' minute.s.')
