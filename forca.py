def jogar():
    print("###################################")
    print("### Bem vindo ao jogo da Forca ###")
    print("###################################")

    palavra_secreta = 'banana'
    letras_acertadas = ['_', '_', '_', '_', '_', '_']
    print(letras_acertadas)

    enforcou = False
    acertou = False

    while not enforcou and not acertou:
        chute = input('Qual a letra? ')
        chute = chute.strip()


        index = 0 
        for letra in palavra_secreta:
            if chute.lower() == letra.lower():
                letras_acertadas[index] = letra
                print(f"Encontrei a letra {chute} na posição {index}")
            if ' '.join(letras_acertadas) == palavra_secreta:
                print('Palavra correta')
                break
            index += 1
        print(letras_acertadas)
    print('Fim do jogo')
    
if(__name__ == "__main__"):
    jogar()