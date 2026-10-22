import os
import json

class Objeto_media:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota
        self.aux = 0
    def calcula_nota(self):
        print(f"Aux: {self.aux}")
        self.aux += self.nota
        print(f"Aux depois: {self.aux}")

class Salva_nota:
    def nota_arquivada(self, dados):
        dados.aux /= 4
        if not os.path.exists("boletin.json"):
            lista = []
            with open("boletin.json", "w", encoding="utf-8") as arquivo:
                json.dump(lista, arquivo, indent=4, ensure_ascii=False)
        update = {"nome":dados.nome, "nota_media": dados.aux}
        with open("boletin.json", "r", encoding="utf-8")as arquivo:
            conteudo = json.load(arquivo)
        print(f"Conteudo antes -> {conteudo}")
        conteudo.append(update)
        print(f"Conteudo depois -> {conteudo}")
        with open("boletin.json", "w", encoding="utf-8")as arquivo:
            json.dump(conteudo, arquivo, indent=4, ensure_ascii=False)