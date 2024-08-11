perguntas = [
    {
        'Pergunta': 'Quanto é 1 + 1?',
        'Opções': ['2','3','4','5'],
        'Resposta': '2',
    },
    {
        'Pergunta': 'Quanto é 5 * 5?',
        'Opções': ['10','55','25','51'],
        'Resposta': '25'
    },
    {
        'Pergunta': 'Quanto é 10 / 2?',
        'Opções': ['4','5','2','1'],
        'Resposta': '5'
    }
]

acertos = 0

for x in perguntas:
    print(f"Pergunta: ", x.get('Pergunta'))
    print('Opções: \n')

    for i, y in enumerate(x['Opções']):
        print(f'{i})', y)
    resposta = input()

    if resposta.isdigit() == False:
        print('Errou :(')
    else:
        resposta = int(resposta)
        if x['Opções'][resposta] == x['Resposta']:
            print('Acertou! \n')
            acertos += 1
        else:
            print('Errou :(')

print(f"Você acertou {acertos} de 3 perguntas.")
    