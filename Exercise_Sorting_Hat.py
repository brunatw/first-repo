# Exercício Chapéu Seletor / Sorting Hat Exercise
# Aula Python Iniciante Codédex - 04/02/2026

# Inicialização dos pontos usando um dicionário
# House points initialization using a dictionary
houses = {
  "Gryffindor": 0,
  "Ravenclaw": 0,
  "Hufflepuff": 0,
  "Slytherin": 0
}

print("Welcome to Hogwarts! Please answer the Sorting Hat's questions and discover to which of the four Houses you'll go to!\n")

# --- Pergunta 1 / Question 1 ---
q1 = int(input("Q1) Do you prefer Dawn or Dusk?\n 1) Dawn\n 2) Dusk\n"))

if q1 == 1:
  houses["Gryffindor"] += 1
  houses["Ravenclaw"] += 1
elif q1 == 2:
  houses["Hufflepuff"] += 1
  houses["Slytherin"] += 1
else:
  print("Wrong Input.\n")

# --- Pergunta 2 / Question 2 ---
q2 = int(input("\n Q2) When you're dead, you want people to remember you as:\n 1) The Good\n 2) The Great\n 3) The Wise\n 4) The Bold\n"))

if q2 == 1:
  houses["Hufflepuff"] += 2
elif q2 == 2:
  houses["Slytherin"] += 2
elif q2 == 3:
  houses["Ravenclaw"] += 2
elif q2 == 4:
  houses["Gryffindor"] += 2
else:
  print("Wrong Input.\n")

# --- Pergunta 3 / Question 3 ---
q3 = int(input("\n Q3) Which kind of instrument most pleases your ear?\n 1) The violin\n 2) The trumpet\n 3) The piano\n 4) The drum\n"))

if q3 == 1:
  houses["Slytherin"] += 4
elif q3 == 2:
  houses["Hufflepuff"] += 4
elif q3 == 3:
  houses["Ravenclaw"] += 4
elif q3 == 4:
  houses["Gryffindor"] += 4
else:
  print("Wrong Input.\n")

# Exibição das pontuações finais
# Displaying the final scores
print("Now... The houses' score are:\n")
print("Gryffindor:", houses["Gryffindor"])
print("Ravenclaw:", houses["Ravenclaw"])
print("Hufflepuff:", houses["Hufflepuff"])
print("Slytherin:", houses["Slytherin"])
print("")

# Determina a casa com a maior pontuação
# Determines the house with the highest score
winner = max(houses, key=houses.get)

print("So... You will go to:")
print(f"✨ {winner} ✨")