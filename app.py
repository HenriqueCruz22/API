from flask import Flask, request, jsonify

app = Flask(__name__)

translations = {
    "hello": {
        "en": "Hello",
        "pt": "Olá",
        "es": "Hola"
    },
    "cat": {
        "en": "cat",
        "pt": "gato",
        "es": "gato"
    },
    # Adicione mais palavras e traduções aqui
}

@app.route('/translate', methods=['GET', 'POST'])
def translate():
    if request.method == 'POST':
        data = request.get_json()
        word = data.get('word')
        lang = data.get('lang')

        if word is None or lang is None:
            return jsonify({'error': 'Palavra e idioma são campos obrigatórios.'}), 400

        translation = translations.get(word.lower())

        if translation is None:
            return jsonify({'error': f'Tradução não encontrada para a palavra "{word}".'}), 404

        translated_word = translation.get(lang.lower())

        if translated_word is None:
            return jsonify({'error': f'Idioma "{lang}" não encontrado.'}), 404

        return jsonify({'word': translated_word})
    
    elif request.method == 'GET':
        return jsonify({'message': 'Para traduzir, envie uma requisição POST para esta rota com a palavra e o idioma desejado.'})

@app.route('/')
def home():
    return jsonify({'message': 'Bem-vindo à API de tradução. Acesse /translate para usar o serviço.'})

if __name__ == '__main__':
    app.run(debug=True)
