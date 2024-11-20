# Recebe as 3 notas do aluno
nota1 = float(input("Digite a 1ª nota: "))
nota2 = float(input("Digite a 2ª nota: "))
nota3 = float(input("Digite a 3ª nota: "))

# Calcula a média aritmética
media = (nota1 + nota2 + nota3) / 3

# Exibe a média
print(f"A média do aluno é: {media:.2f}")


def exibir_resultado(media):
    # Exibe o resultado com base na média
    if media > 6:
        print("Aprovado")
    elif 5.0 < media <= 6.0:
        print("Recuperação")
    else:
        print("Reprovado")