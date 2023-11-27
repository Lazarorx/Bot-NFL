import os


def processar_resposta(resposta, nome):
    if resposta == '7':
        return

    if resposta == '1':
        print(f'\n{nome}, CO Pittsburgh Steelers e o New England Patriots estão empatados no topo da tabela com seis Super Bowls cada.\n')
    elif resposta == '2':
        print(f'\n{nome}, Tom Brady é o jogador mais vitorioso da NFL, com sete títulos. Brady venceu seis títulos com o New England Patriots e um com o Tampa Bay Buccaneers.\n')
    elif resposta == '3':
        print(f'\n{nome}, Tom Brady é o jogador com mais touchdowns na NFL, com 845. Brady é seguido por Peyton Manning (714), Brett Favre (508) e Dan Marino (420).\n')
    elif resposta == '4':
        print(f'\n{nome}, Peyton Manning é o jogador com mais jardas de passe na NFL, com 84.520. Manning é seguido por Tom Brady (84.520), Drew Brees (80.358) e Brett Favre (71.838).\n')
    elif resposta == '5':
        print(f'\n{nome}, Jerry Rice é o jogador com mais recepções na NFL, com 22.895. Rice é seguido por Tony Gonzalez (15.127), Marvin Harrison (14.580) e Larry Fitzgerald (17.492).\n')
    elif resposta == '6':
        print(f'\n{nome}, Bruce Smith é o jogador com mais sacks na NFL, com 200. Smith é seguido por Reggie White (198), John Randle (133.5) e DeMarcus Ware (138.5).\n')


def start():
    # Apresentar o chatbot
    print('Olá bem-vindo ao chatbot sobre a NFL!')
    # pedir o nome
    nome = input('Digite seu nome: ')

    resposta = ''
    while resposta != '7':
        resposta = input(
            f'O que gostaria de saber hoje sobre a NFL?\n'
            f'[1] - Qual time da NFL tem mais Super Bowls conquistados?\n'
            f'[2] - Qual é o jogador mais vitorioso da NFL?\n'
            f'[3] - Qual é o jogador com mais touchdowns na NFL?\n'
            f'[4] - Qual é o jogador com mais jardas de passe na NFL?\n'
            f'[5] - Qual é o jogador com mais recepções na NFL?\n'
            f'[6] - Qual é o jogador com mais sacks na NFL?\n')

        processar_resposta(resposta, nome)


if __name__ == '__main__':
    start()

