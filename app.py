from flask import Flask, request, jsonify

app = Flask(__name__)

translations = {
    'hello': {
        'en': 'Hello',
        'es': 'Hola',
        'fr': 'Bonjour'
    },
    'goodbye': {
        'en': 'Goodbye',
        'es': 'Adiós',
        'fr': 'Au revoir'
    }
}

@app.route('/translate', methods=['POST'])
def translate():
    data = request.get_json()
    word = data['word']
    language = data['language']
    
    if word in translations and language in translations[word]:
        translated_word = translations[word][language]
        return jsonify({'translated_word': translated_word})
    else:
        return jsonify({'error': 'Translation not available for the given word and language.'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
