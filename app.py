# %% import packages
from flask import Flask, request, render_template

import pickle
from funcs import clean_body, TagPredictor
###

# %% initialization
app = Flask(__name__)

with open('data/final.pickle', 'rb') as file:
    predictor = TagPredictor(pickle.load(file))
prediction_tags = predictor.get_prediction_tags()


# @app.route('/')
# def message_initial():
#     return 'Welcome. To predict some tags, please go to: ' \
#            '/predict/your sentence'

@app.route('/')
def my_form():
    return render_template('my-form.html')


# @app.route('/predict/<string:sentence>')
@app.route('/', methods=['POST'])
def predict():
    sentence = request.form['text']
    cleaned_sentence, prediction = predictor.predict(sentence)
    tags = prediction_tags[prediction > 0]
    # print('tags:', tags)
    if len(tags) == 0:
        return 'no appropriate tag detected'
    # tags = [f'<{tag}>' for tag in tags]
    out = "".join([f'<{tag}>' for tag in tags])
    # print("out:", out)
    # print('cleaned sentence:', cleaned_sentence)
    return render_template('view_suggested_tags.html',
                           cleaned_entence=cleaned_sentence,
                           suggested_tags=out)
    # return [f"{out}"][0]
    # return 'test affichage'


# test_sentence = "I Can't load my python module"
# test_sentence = "How can I load c++ library within python ?"

# print('tags:', prediction_tags)
# print('prediction:', prediction)
# print('suggested tags:', prediction_tags[prediction > 0])
# print(predict(test_sentence))


if __name__ == '__main__':
    app.run(host="0.0.0.0")

# %%
