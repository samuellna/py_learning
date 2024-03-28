a, b = 10, 20
a, b = b, a # Inverting values

# print(a, b)

student = {
    'full_name': 'Samuel Nunes de Andrade',
    'age': 20,
    'parents': ['Antonio', 'Ione'],    
}

(key_1, value_1), *_ = student.items()

# print(key_1, value_1)

student_data = {
    'subjacts' : [
        'Logic', 'Infracom', 'English'
    ],
    'grades': [
        [10, 10, 10],
        [6.3, 8.2, 10],
        [10, 10, 10]
    ]
}

all_data_student = {
    **student,
    'address': ['Rua da Claraval', '68'],
    'course': 'Computer engineering',
    **student_data
}

print(all_data_student)

def mostro_argumentos_nomeados(*args, **kwargs):
    print('NÃO NOMEADOS:', args)

    for chave, valor in kwargs.items():
        print(chave, valor)


# mostro_argumentos_nomeados(nome='Joana', qlq=123)
# mostro_argumentos_nomeados(**pessoas_completa)

configuracoes = {
    'arg1': 1,
    'arg2': 2,
    'arg3': 3,
    'arg4': 4,
}
mostro_argumentos_nomeados(**configuracoes)