class Mundo:
    def __init__(self, pais, oceano, idioma, gentilicio):
        self.pais = pais
        self.oceano = oceano
        self.idioma = idioma
        self.gentilicio = gentilicio

m1 = Mundo("Colombia", "Oceano Pacifico", "español", "colombianos")

print(m1.pais)
print(m1.oceano)
print(m1.idioma)
print(m1.gentilicio)
