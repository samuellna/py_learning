questions = [
    {
        'Question': 'Who is the most famous Drag Queen of the world?',
        'Options': ['Ru Paul', 'Gloria Groove', 'Pabllo Vittar', 'Trixie Mattel'],
        'Answer': 'Pabllo Vittar'
    },
    
    {
        'Question': 'What is the best algorithm to find the shortest path in a weighted graph (The graph does not have negative edges):',
        'Options': ['Dijksta', 'Bellman Ford', 'Prim', 'Union Find'],
        'Answer': 'Dijkstra'
    },
    
    {
        'Question': 'What of these skins Lux (League of Legends) have?',
        'Options': ['Coven', 'Blood Moon', 'Project', 'Cosmic'],
        'Answer': "Cosmic"
    },
    
    {
        'Question': 'In the anime "One Piece", who ate the Gomu Gomu no Mi?',
        'Options': ['Luffy', 'Nobody ate the Gomu Gomu no Mi','Sanji', 'Bonney'],
        'Answer': 'Nobody ate the Gomu Gomu no Mi'
    }
]


def print_question(index):
    print(f'Question {index + 1}: \n\t{questions[index].get('Question')}')
    
    for i, op in enumerate(questions[index].get('Options')):
        print(f'\t{i} - {op}')

def verify_answer(answer, index):
    try:
        options_ = questions[index].get('Options')
        correct_answer = questions[index].get('Answer')
        
        if(options_[answer] == correct_answer): 
            return "Correct answer!"
        return "Wrong answer!"
    except:
        return "The answer given is not between 0 and 3"

i = 0
while(i < len(questions)):
    print_question(i)
    answer = input("Answer: ")
    
    if answer.isdigit():
        answer = int(answer)
        if(answer <= 3 and answer >= 0):
            result = verify_answer(answer, i)
            print(result, '\n')
            i += 1
        print("Please, type a number between 0 and 3.")
    else:
        print("Please, type a number.")