#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# %% imports des packages
import re
import contractions
import numpy as np
from sentence_transformers import SentenceTransformer

###


# %% Définition des fonctions utiles

def clean_body(text: str) -> str:
    # lower all strings
    text = text.lower()
    for func in [remove_URL,
                 remove_html,
                 remove_non_ascii,
                 contractions.fix,  # remove text contractions
                 remove_special_characters
                 ]:
        text = func(text)
    return text


# source notebook nlp-preprocessing-feature-extraction-methods-a-z
# LONG NG - Kaggle
def remove_html(text):
    """
        Remove the html in sample text
    """
    html = re.compile(r"<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});")
    return re.sub(html, "", text)


# source notebook nlp-preprocessing-feature-extraction-methods-a-z
# LONG NG - Kaggle
def remove_URL(text):
    """
        Remove URLs from a sample string
    """
    return re.sub(r"https?://\S+|www\.\S+", "", text)


# source notebook nlp-preprocessing-feature-extraction-methods-a-z
# LONG NG - Kaggle
def remove_non_ascii(text):
    """
        Remove non-ASCII characters
    """
    # or ''.join([x for x in text if x in string.printable])
    return re.sub(r'[^\x00-\x7f]', r'', text)


# source notebook nlp-preprocessing-feature-extraction-methods-a-z
# LONG NG - Kaggle
EMOJI_PATTERN = re.compile(
        '['
        u'\U0001F600-\U0001F64F'  # emoticons
        u'\U0001F300-\U0001F5FF'  # symbols & pictographs
        u'\U0001F680-\U0001F6FF'  # transport & map symbols
        u'\U0001F1E0-\U0001F1FF'  # flags (iOS)
        u'\U00002702-\U000027B0'
        u'\U000024C2-\U0001F251'
        ']+',
        flags=re.UNICODE)


def remove_special_characters(text):
    """
        Remove special special characters, including symbols, emojis,
        and other graphic characters
    """
    return EMOJI_PATTERN.sub(r'', text)

###


class Vectorized():
    """Class pour vectoriser les données texte et gérer la modélisation
    """
    def __init__(self):
        self.x = {}
        self.scaler = None
        self.b_scale_x = False
        self.reset_model()
        self.reset_pca()

    def copy_data_from_dict(self, dict):
        """copy data from another vectorized. This method is used to update the
        class without re-train the vectorizer and the classifier.

        Args:
            dict (dict): _description_
        """
        for attribut, value in dict.items():
            setattr(self, attribut.replace(' ', '_'), value)
        self.vectorizer = SentenceTransformer('all-MiniLM-L6-v2')

    def reset_pca(self):
        self.pca = None
        self.use_pca = False

    def reset_model(self):
        self.clf = None
        self.optimized_thresholds = None

    def get_vocabulary(self):
        return self.vectorizer.get_feature_names_out()

    def transform(self, x):
        if self.method == 'word2vec':
            out = np.empty((len(x), 300), dtype=float)
            for out_i, xi in zip(out, x):
                out_i[:] = self.vectorizer.get_mean_vector(xi.split(' '))
            return out
        elif self.method == 'sbert':
            out = self.vectorizer.encode([x])
            # print('out:', out.shape)
            return out
        elif self.method == 'use':
            # return self.vectorizer(x.values)
            # AJOUT DE BOUCLE FOR POUR UN SUIVI
            x = x.values
            v0 = self.vectorizer(x[:1])
            out = np.empty_like(v0, shape=(len(x), len(v0[0])))
            out[0, :] = v0[:]
            print('USE vectorization:')
            for i in range(1, len(x), 10):
                print(f'{i/len(x):.2%}', end='\r')
                out[i:i+10] = self.vectorizer(x[i:i+10])
            print(f'{1:.2%}    ', end='\n'*2)
            # return self.vectorizer.encode(x.values)
            return out
        else:
            return self.vectorizer.transform(x)

    def set(self, which: str, x):
        self.x[which] = self.transform(x)

    def get(self, which: str):
        x = self.x[which]
        if hasattr(x, 'todense'):
            x = x.todense()
        return np.asarray(x)

    def scale(self, x):
        if self.b_scale_x:
            if self.use_pca:
                return self.pca.transform(self.scaler.transform(x))
            return self.scaler.transform(x)
        return x

    def predict(self, text: str):
        text = clean_body(text)
        # print('cleaned text:', text)
        vector = self.transform(text)
        vector = self.scale(vector)
        return self.predict_optim_threshold(vector)

    def predict_proba(self, text):
        return self.clf.predict_proba(self.scale(self.get(which)))

    def predict_optim_threshold(self, scaled_vector):
        y_pred_proba = self.clf.predict_proba(scaled_vector)
        y_pred = np.empty_like(y_pred_proba, dtype=int)
        for y_pred_i, y_pred_proba_i, threshold \
                in zip(y_pred.T,
                       y_pred_proba.T,
                       self.optimized_thresholds):
            y_pred_i[:] = y_pred_proba_i > threshold
        return y_pred.ravel()

    def get_prediction_tags(self):
        return self.prediction_tags


# %% END OF FILE
###
