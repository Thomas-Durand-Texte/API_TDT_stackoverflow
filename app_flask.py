from flask import Flask

app = Flask(__name__)


test = 123


@app.route('/')
def message_initial():
    return 'Bonjour. Pour prédire des tags, veuillez aller sur' \
           '/predict/votre_phrase'


@app.route('/predict/<string:phrase>')
def predict(phrase):
    return f"{phrase} : {test}"


if __name__ == '__main__':
    app.run(host="0.0.0.0")
