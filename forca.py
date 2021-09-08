def jogar():
    print("###################################")
    print("### Bem vindo ao jogo da Forca ###")
    print("###################################")

    palavra_secreta = 'banana'

    enforcou = False
    acertou = False

    while not enforcou and not acertou:
        print('jogando....')
        palavra = input()
        if palavra == palavra_secreta:
            acertou = True
            print('Parabéns! palavra correta')
        else:
            print('Palavra incorreta, tente novamente')

    print('Fim do jogo')
    
if(__name__ == "__main__"):
    jogar()