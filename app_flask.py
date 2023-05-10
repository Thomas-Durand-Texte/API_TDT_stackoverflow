# %% import packages
from flask import Flask

import pickle
from funcs import clean_body, Vectorized
###

# % initialization
# app = Flask(__name__)

vectorized = Vectorized()
with open('final.pickle', 'rb') as file:
    vectorized.copy_data_from_dict(pickle.load(file))
prediction_tags = vectorized.get_prediction_tags()

test_sentence = "I Can't load my python module"

prediction = vectorized.predict(test_sentence)

print('tags:', prediction_tags)
print('prediction:', prediction)
print('suggested tags:', prediction_tags[prediction > 0])


# @app.route('/')
# def message_initial():
#     return 'Bonjour. Pour prédire des tags, veuillez aller sur' \
#            '/predict/votre phrase'


# @app.route('/predict/<string:phrase>')
# def predict(phrase):
#     return f"{phrase} : {test}"


# if __name__ == '__main__':
#     app.run(host="0.0.0.0")

# %%
