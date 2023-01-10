# AUTOGENERATED! DO NOT EDIT! File to edit: app.ipynb.

# %% auto 0
__all__ = ['learn', 'categories', 'image', 'label', 'examples', 'intf', 'is_healthy', 'classify_image']

# %% app.ipynb 1
from fastai.vision.all import *
import gradio as gr

def is_healthy(x): return x[0].isupper()

# %% app.ipynb 3
learn = load_learner('model.pkl')

# %% app.ipynb 5
categories = ('Aphids', 'Army worm', 'Bacterial Blight', 'Healthy', 'Powdey Mildew', 'Target spot')

def classify_image(img):
    pred,idx,probs = learn.predict(img)
    return dict(zip(categories, map(float,probs)))

# %% app.ipynb 7
image = gr.inputs.Image(shape=(192,192))
label = gr.outputs.Label()
examples = ['Exemples/Aphids.jpg', 'Exemples/Army worm.jpg', 'Exemples/Bacterial Blight.jpg', 'Exemples/Healthy.jpg', 'Exemples/Powdey Mildew.jpg', 'Exemples/Target spot.jpg']

title = "Leaf disease recognition"
description = "<p style='text-align: center'>Identifier sur une photo de feuille d'arbre si elle saine sinon de quoi elle est atteinte.</br>Catégories : Aphids, Army worm, Bacterial Blight, Healthy, Powdey Mildew, Target spot</p>"

intf = gr.Interface(fn=classify_image, inputs=image, outputs=label, examples=examples)
intf.launch(inline=False)
