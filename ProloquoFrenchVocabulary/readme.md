SCRIPT 1 : 1_gcv.py
	OCR avec l'API de Google (cloud.vision)

SCRIPT 2 : 2_associateWords.py

	Fichier d'entrée : 'IMG_0022.json' [pour le développement, sinon : Folder 'Proloquo_text_Screens']
	Fichier de sortie  :  'Vocabulaire_Français.txt'
	
		ligne 41 : 	Recherche de proximité : Certains mots contenu dans un seul bouton sur proloquo ont été séparé
					Exemple : <c'est fini>, deux annotations différentes dans le fichier json.
					Voir le l'image 'illustration_proximite.jpg'
					
					La condition va vérifier la distance entre le point B de <c'est> et le point A de <fini>, sur l'axe x (abscisse) et sur l'axe y (ordonnée).
					Si l'écart sur les abscisses est inférieur à 20 ET que l'écart sur les ordonnées est compris entre -20 et 20, alors on considère qu'il s'agit de deux mots sur le même bouton. 
		
		Pour faire cette recherche de proximité, on récupère à chaque tour de boucle les coordonnées du point B du mot dans une variable, et on les compare aux coordonnées du point A du mot suivant (dans le tour suivant)
		Une gestion de l'erreur est implémentée pour le premier tour de boucle, dans lequel la variable 'word_one_B_point_x' n'existera pas encore
		
		ligne 62 : 	Une fois le mot1 et le mot2 concaténé, on doit supprimer le mot1 qui a d'abord été ajouté seul à la liste Page_words.
		⚠ Erreur sur cette ligne --> En cours de rectification
		
	
	Ensuite : Supprimer les mots indésirables des pictogrammes
		Exemple : 	Dossier Petits mots, le pictogramme contient les mots [et, ça, la, mots, en haut] (reconnu comme ['el', 'a la', 'en haut'] dans Vocabulaire_Français.txt)
					Ces mots ne font pas partie du vocab et doivent être supprimés
		Idée 1 : 	Checker l'espace entre deux lignes de vocabulaire
		Idée 2 : 	Checker l'écart entre les ordonnées du mots 1 et du mots 2 en miroir
		Difficulté : Quand on change de ligne, on sera forcément sur une ordonné différentes du mot précédent, sans pour autant être sur un mot indésirable
		Cf. Schéma_lignes.pdf

SCRIPTS SUIVANTS : Reprise des comparaison à ESLO
