"""
Closure and functions that returns another functions.
"""

def speak(something_to_say):
    def speak_name(name):
        return f'{something_to_say}, {name}!'
    return speak_name


speak_good_m = speak('Good morning') # "speak_good_m" gets the "speak_name" function 

names_list = ["Luffy", "Nami", "Zoro", "Sanji", "Usopp", "Chopper", "Robin", "Franky", "Brook", "Jinbe"]
for name in names_list:
    print(speak_good_m(name))