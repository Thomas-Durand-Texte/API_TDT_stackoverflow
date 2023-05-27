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


class TagPredictor():
    """Class pour vectoriser les données texte et gérer la modélisation
    """
    def __init__(self, dict_data: dict):
        """initialisation of the class TagPredictor

        Args:
            dict_data (dict): input data of the pre-trained model
        """
        for attribut, value in dict_data.items():
            setattr(self, attribut.replace(' ', '_'), value)
        self.vectorizer = SentenceTransformer('all-MiniLM-L6-v2')

    def transform(self, x):
        out = self.vectorizer.encode([x])
        return out

    def scale(self, x):
        return self.scaler.transform(x)

    def predict(self, text: str):
        text = clean_body(text)
        # print('cleaned text:', text)
        vector = self.transform(text)
        vector = self.scale(vector)
        return text, self.predict_optim_threshold(vector)

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
