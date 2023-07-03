from flask import Flask, request, jsonify

app = Flask(__name__)

translations = {
    'hello': {
        'pt': 'olá',
        'es': 'hola',
        'fr': 'bonjour'
    },
    'cat': {
        'pt': 'gato',
        'es': 'gato',
        'fr': 'chat'
    },
    'dog': {
        'pt': 'cachorro',
        'es': 'perro',
        'fr': 'chien'
    }
}

@app.route('/translate', methods=['POST'])
def translate():
    data = request.get_json()

    word = data.get('word')
    language = data.get('language')

    if not word or not language:
        return jsonify({'error': 'Por favor, forneça uma palavra e um idioma para tradução.'}), 400

    translation = translations.get(word.lower())

    if not translation:
        return jsonify({'error': 'Tradução não encontrada para a palavra fornecida.'}), 404

    translation_text = translation.get(language.lower())

    if not translation_text:
        return jsonify({'error': 'Tradução não encontrada para o idioma fornecido.'}), 404

    return jsonify({'word': word, 'translation': translation_text})

if __name__ == '__main__':
    app.run(debug=True)
