# %% import packages
from flask import Flask

import pickle
from funcs import clean_body, TagPredictor
###

# %% initialization
app = Flask(__name__)

with open('final.pickle', 'rb') as file:
    predictor = TagPredictor(pickle.load(file))
prediction_tags = predictor.get_prediction_tags()


@app.route('/')
def message_initial():
    return 'Welcome. To predict some tags, please go to: ' \
           '/predict/your sentence'


@app.route('/predict/<string:phrase>')
def predict(phrase):
    prediction = predictor.predict(test_sentence)
    tags = prediction_tags[prediction > 0]
    tags = ''.join([f'<{tag}>' for tag in tags])
    return tags


# test_sentence = "I Can't load my python module"
# test_sentence = "How can I load c++ library within python ?"

# print('tags:', prediction_tags)
# print('prediction:', prediction)
# print('suggested tags:', prediction_tags[prediction > 0])
# print(predict(test_sentence))


if __name__ == '__main__':
    app.run(host="0.0.0.0")

# %%
