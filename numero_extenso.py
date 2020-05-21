lista1=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,20,30,"de"]
lista2=["","um","dois","tres","quatro","cinco","seis","sete","oito","nove","dez","onze","doze","treze","quatorze","quinze","vinte","trinta","de"]
meses=["","janeiro","fevereiro","marco","abril","maio","junho","julho","agosto","setembro","outrubro","novembro","dezembro"]
x=input("digite um numero: ")
x=x.replace(" "," de ")
listaX=x.split()
print(listaX)

# mes
mes=int(listaX[2])#transforma o mes em inteiro
if (mes<=12):
    listaX[2]=(meses[mes])
else:
    print("ERRO")

#dia
dia=int(listaX[0])#transforma o dia em inteiro
dezena=dia//10
unidade=dia%10

if dia<=31:

    if dezena == 0:
        listaX[0]=lista2[dia]

    if dezena == 1:
        if (unidade == 8) or (unidade == 0):
            dezena=lista2[10]
            unidade=lista2[unidade]
            dia =(dezena+unidade)
            listaX[0]=dia
        elif (unidade == 6) or (unidade == 7):
            dezena=("dezes")
            unidade=lista2[unidade]
            dia =(dezena+unidade)
            listaX[0]=dia
        elif (unidade == 9):
            dezena=("deze")
            unidade=lista2[unidade]
            dia =(dezena+unidade)
            listaX[0]=dia
        else:            
            listaX[0]=lista2[dia]
        
    if dezena == 2:
        if (unidade == 0):
            dezena=lista2[16]
            unidade=lista2[unidade]
            dia =(dezena+unidade)
            listaX[0]=dia        
        else:
            dezena=("vinte e ")
            unidade=lista2[unidade]
            dia =(dezena+unidade)
            listaX[0]=dia

    if dezena == 3:
        if (unidade == 0):
            listaX[0]=lista2[17]        
        else:
            dezena=("trinta e ")
            unidade=lista2[unidade]
            dia =(dezena+unidade)
            listaX[0]=dia
else:
    print("ERROR")

    

datatr=str(listaX).strip("[]")#retira os conchetes
datatr=datatr.replace("'","")#retira as aspas
datatr=datatr.replace(",","")#retira as virgulas
print(datatr)
        
    
#for d in listaX:
#    if d == ("de"):
#        print ("de",end=" ")
#    else:
#        for e in lista1:
#            d=int(d)
#           if e == d:
#                print(lista2[d],end=" ")
