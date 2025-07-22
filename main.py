#mensagem de saudação a turma do python de 2025
print("Olá turma do Python!")
print("Tudo bem!")

#solicita que o usuário informe seu nome
nome: str = input("Qual é o seu nome? ")
print(f"Olá, {nome}!")

#solicita que o usuário informe qual a sua idade informando se é maior ou menor de idade
try:
 idade = int(input("Quantos anos voçê tem? "))
 print(f"Sua idade é {idade}!")
 
 if idade >= 18:
    print(f"Voçê é maior de idade")
 else:
    print(f"Voçê é menor de idade")

except ValueError:
    print(f"Por favor insira um número válido! ")

#solicita que o usuário informe sua cidade
cidade: str = input("Qual a sua cidade? ")
print(f"Sua cidade é {cidade}")
