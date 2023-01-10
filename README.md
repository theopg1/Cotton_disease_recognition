# Leaf_disease_recognition

Projet d'initiation au deeplearning ayant pour but d'apprendre à comprendre et utiliser un réseau de neurones pour entrainer une intelligence artificielle.

## Problématique :

Créer un programme de reconnaissance de l'état de santé d'une feuille d'arbre. Savoir si cette dernière est saine ou atteinte d'une maladie ou attaqué par un nuisible par exemple. 

Les images sont issues de kaggle grâce à ce dataset :</br>
https://www.kaggle.com/datasets/dhamur/cotton-plant-disease?resource=download

Lien vers le huggingface du projet :</br>
https://huggingface.co/spaces/theopg1/Cotton_disease_recognition

## Contenu :
Le projet contient: 
- le dossier Cotton Plant ayant possédants les images d'entrainement et validation de l'ia dans un dossier par catégorie.
- le dossier Exemples avec un exemple de chaque catégorie afin de tester et afficher ces dernières sur l'interface graphique
- le fichier model.ipynb qui permet de créer et entrainer l'ia pour crée le fichier model.pkl
- le fichier app.ipynb qui nous permet grâce à gradio d'avoir une interface visuel pour utiliser notre ia en local ou sur des sites comme huggingface par ex
- le fichier app.py qui est une version .py de notre jupyter généré automatiquement grâce à ce dernier pour garder l'essentiel
- un fichier requirements.txt pour les librairies

```bash
Leaf_disease_recognition 
├── Cotton plant
│   ├── Aphids
│   ├── Army worm
│   ├── Bacterial Blight
│   ├── Healthy
│   ├── Powdery Mildew
│   └── Target spot
├── Exemples
├── app.ipynb
├── app.py
├── model.ipynb
├── model.pkl
└── requirements.txt
```