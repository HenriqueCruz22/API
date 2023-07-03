from flask import Flask, request, jsonify

app = Flask(__name__)

translations = {
    "hello": {
        "pt": "olá",
        "es": "hola",
        "fr": "bonjour"
    },
    "cat": {
        "pt": "gato",
        "es": "gato",
        "fr": "chat"
    },
    "dog": {
        "pt": "cão",
        "es": "perro",
        "fr": "chien"
    }
}

@app.route('/translate', methods=['POST'])
def translate():
    data = request.get_json()
    word = data.get('word')
    lang = data.get('lang')

    if word in translations and lang in translations[word]:
        translated_word = translations[word][lang]
        return jsonify({"translated_word": translated_word})
    else:
        return jsonify({"error": "Tradução não encontrada para a palavra fornecida."})

if __name__ == '__main__':
    app.run(debug=True)
