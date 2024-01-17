# JOGO DA FORCA
import os

secret_word = input("Type a word: ")
secret_word = secret_word.lower()

size_word = len(secret_word)
fails = 0
word = ''

for i in range(0, size_word):
    word += '_'

win = False

while(fails < 3 and not win): # The player can fail 3 times
    letter = input("Type a letter: ")
    is_letter = len(letter) == 1
    if(is_letter):
        letter = letter.lower()
        if(letter in secret_word and letter not in word):
            start = 0
            index = secret_word.find(letter, start)
            word_aux = ''
            for j in range(0, size_word):
                if(j == index):
                    word_aux += letter
                    start = index + 1
                    index = secret_word.find(letter, start)
                else:
                    word_aux += word[j]
            word = word_aux
            print(word_aux)
        elif letter in secret_word:
            print("You already sent this letter.")
        else:
            if(fails < 2):
                print(f"Wrong answer, now you failed {fails + 1} times")
            else:
                print("You lose this game!")
            fails += 1
        if word == secret_word:
            os.system("cls")    
            print("You're amazing! Congrats for win this game!")
            win = True
    else:
        print("You lose the game because of cheating.")
        fails += 3