import random

numero_minimo = 1
numero_maximo = 100

PC = random.randint(numero_minimo, numero_maximo)

print("=" * 59)
print("{:^56}".format("JOGO DO IMPRENSADINHO"))
print("=" * 59)
print("Vamos jogar?! Você terá que descobrir qual número eu pensei.")
print("Ele está entre", numero_minimo, "e", numero_maximo)

acertou = False
tentativas = 0

while not acertou:
  
  Usuario = int(input('Que número eu pensei?: '))

  if Usuario == 0:
    print(f"Você desistiu. O número correto era {PC}.")
    break
  elif Usuario < numero_minimo or Usuario > numero_maximo:
    print(f"Por favor, digite um número entre {numero_minimo} e {numero_maximo}.")
    print("Caso queira desistir digite 0")
    continue

  tentativas += 1

  if Usuario < PC:
    numero_minimo = Usuario
    print("Ele está entre", numero_minimo, "e", numero_maximo)
  elif Usuario > PC:
    numero_maximo = Usuario
    print("Ele está entre", numero_minimo, "e", numero_maximo)
  else:
    acertou = True

if acertou:
    print(f"Você GANHOU!!! Você acertou o número {PC} em {tentativas} tentativa(s).")

