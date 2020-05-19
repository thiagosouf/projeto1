def computador_escolhe_jogada(n,m):
    if n<=m:
        print("O computador tirou",n," peças.")
        print ("Fim do jogo! O computador ganhou!")
        return n
        
    else:
        ctirou=0
        while ctirou<m:
            ctirou=ctirou+1
            sobrou=n-ctirou
            if ((sobrou)%(m+1))==0:
                print("O computador tirou",ctirou," peças.")
                n=sobrou
                print("Agora restam",n,"peças no tabuleiro.")
                usuario_escolhe_jogada(n,m)

    
def usuario_escolhe_jogada(n,m):
    utirou=int(input("Quantas peças você vai tirar? "))
    while utirou>m:
        print("Oops! Jogada inválida! Tente de novo.")
        utirou=int(input("Quantas peças você vai tirar? "))
    if utirou<=m:
        print("voce tirou",utirou,"peças")
        n=n-utirou
        print("Agora restam",n,"peças no tabuleiro.")
        computador_escolhe_jogada(n,m)
        return utirou #ta gravando a primeira tentativa
    

def partida():
    peças=int(input("Quantas peças? ")) 
    limite=int(input("Limite de peças por jogada? ")) 
    if (peças%(limite+1))==0:
        print("Você começa!")
        return usuario_escolhe_jogada(peças,limite)
        
    else:
        print("Computador começa!")
        return computador_escolhe_jogada(peças,limite)
    
    
def main():
    print ("Bem-vindo ao jogo do NIM! ")
    print()
    print("1 - para jogar uma partida isolada")
    print("2 - para jogar um campeonato")
    p=int(input("Escolha: "))
    if p==1:
        print("Voce escolheu partida isolada")
        print()
        print("**** Partida Isolada ****")
        return partida()
        
    if p==2:
        print("Voce escolheu um campeonato!")
        print()
        print("**** Rodada 1 ****")
        print()
        partida()
        print("Fim do jogo! O computador ganhou!")
        print()    
        print("**** Rodada 2 ****")
        print()
        partida()
        print("Fim do jogo! O computador ganhou!")
        print()
        print("**** Rodada 3 ****")
        print()
        partida()
        print("Fim do jogo! O computador ganhou!")
        print()
        print("**** Final do campeonato! ****")
        print()
        return("Placar: Você 0 X 3 Computador")
        
    if p!=1 and p!=2:
        print("Comando Invalido")
        print()
        return main()
    
    
print(main())