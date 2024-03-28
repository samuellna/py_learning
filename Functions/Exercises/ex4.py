# Resolving the quest of 'the huxley' site. Quest: https://thehuxley.com/problem/4067?quizId=7899

class Pokemon:
    def __init__(self, name = 'Undefined', element = 'Undefined', atk = 0, defense = 0):
        self.name = name
        self.element = element
        self.atk = atk
        self.defense = defense


enemy = []
strings = ['Name: ', 'Element: ', 'ATK: ', 'DEF: ']
i = 0

while i < 4:
    enemy.append(input(f'{strings[i]}'))
    if(enemy[i].isdigit()):
        if(i == 2 or i == 3):
            i += 1
        else:
            del enemy[i]
            print("Please, don't type a number.")
    else:
        if(i == 2 or i == 3):
            del enemy[i]
            print("Please, type a number.")
        else:
            i += 1
    print(i)

enemy_poke = Pokemon(enemy[0], enemy[1], int(enemy[2]), int(enemy[3]))
print(enemy_poke)