quantidade = int(input("Entre com a quantidade de alunos:"))

def avaliar_estudante(nota1, nota2, nota3, nota_recuperacao):
    nota1 = float(input("Entre com a nota 1:"))
    nota2 = float(input("Entre com a nota 2:"))
    nota3 = float(input("Entre com a nota 3:"))
    media = (nota1 + nota2 + nota3)/3
    if media >= 7:
        print(f"Aluno aprovado com média: {media}")
    else:
        nota_recuperacao = float(input("Entre com a nota da recuperação:"))
        if nota_recuperacao >= 5:
            print(f"Aluno aprovado por recuperação com média {nota_recuperacao}")
        else:
            print(f"Aluno reprovado com média: {nota_recuperacao}")

for i in range (0, quantidade):
    nota1 = float
    nota2 = float
    nota3 = float
    nota_recuperacao = float
    resultado = avaliar_estudante(nota1, nota2, nota3, nota_recuperacao)
    print(resultado)