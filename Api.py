from translate import Translator
import translate

s = Translator(from_lang="pt-br", to_lang="english")

res = s.translate(input(str("Digite aqui a frase que queira traduzir: ")))

print(f"A sua tradução e: {res}")