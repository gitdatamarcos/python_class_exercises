# Solicitar a idade do usuário
idade = int(input("Digite a sua idade: "))

# Verificar o tipo de voto de acordo com a idade
if idade < 16:
  print("NÃO PODE VOTAR")
elif idade in (16, 17) or idade > 65:
  print("VOTO OPCIONAL")
else:
  print("VOTO OBRIGATÓRIO")
