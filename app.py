from flask import Flask, render_template, request, jsonify
from translate import Translator

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    text = request.form['text']

    s = Translator(from_lang="pt-br", to_lang="english")
    res = s.translate(text)

    return jsonify(translation=res)

if __name__ == '__main__':
    app.run()
