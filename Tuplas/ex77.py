palavras = ("python", "programacao", "tupla", "vogais", "consoantes")

for palavra in palavras:
    vogais = []
    for letra in palavra:
        if letra in "aeiou":
            vogais.append(letra)
    print(f"As vogais da palavra {palavra} são: {vogais}")
