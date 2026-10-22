import aluno_classe
loop = 0
aux = 0
while True:
    name = input("Nome do aluno: ").strip().upper()
    referencia = aluno_classe.Objeto_media(name, 0)
    while loop < 4:
        nota = input(f"Nota {loop + 1}: ").strip()
        nota = float(nota)
        referencia.nota = nota
        referencia.calcula_nota()
        loop += 1
    nota_arqu = aluno_classe.Salva_nota()
    nota_arqu.nota_arquivada(referencia)
    break