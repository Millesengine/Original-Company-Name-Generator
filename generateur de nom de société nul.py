import random

print("Put the word or name of your choice and it will create a company name that suits you !")
x = input()
mots = ["Tarti","Super", "Magistiquement", "Déchire","Flex", "Fume", "Famous", "Trop BG"]
mot_qui_déchire = random.choice(mots)
print(mot_qui_déchire + x)

x = input()