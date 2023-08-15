from flowers import FLOWER, BUYER
import random

plants = []

for i in range(100):
	plant = FLOWER(None,None,None,None,None,"G.Bernard")
	#list starts at 0
	if i % 2 == 1:
		plant.setName("tulip")
	else:
		plant.setName("geranium")
	plant.setPrice(round(random.uniform(10.99,56.01),2))

	plants.append(plant)

print("+-----+-----+-----+-----+-----+-----+")
print(f'Flower Type: {plants[66].getName()}')
print(f"Flower's Price: {plants[66].getPrice()}")
print(f"Flower's Colour: {plants[66].getColour()}")
print(f"Flower's main Season: {plants[66].getSeason()}")
print(f"Flower's Size: {plants[66].getSize()}")
print(f"Flower's Buyer: {plants[66].getBuyer()}")
print("+-----+-----+-----+-----+-----+-----+")

