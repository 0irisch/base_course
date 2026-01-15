import random

flower = ['роза', 'тюльпан', 'ирис']
colour = ['черный', 'красный', 'белый', 'синий', 'желтый']
random_colour =[]
for i in range(len(flower)):
    random_colours = random.choice(colour)
    random_colour.append(random_colours)
all = dict(zip(flower, random_colour))
print(all)