lista1=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,20,30,"de"]
lista2=["zero","um","dois","tres","quatro","cinco","seis","sete","oito","nove","dez","onze","doze","treze","quatorze","quinze","vinte","trinta","de"]
meses=["","janeiro","fevereiro","marco","abril","maio","junho","julho","agosto","setembro","outrubro","novembro","dezembro"]
x=input("digite um numero: ")
x=x.replace(" "," de ")
print(x)
listaX=x.split()
print(listaX)

# mes
mes=int(listaX[2])#transforma o mes em inteiro
print(type(mes))
if (mes<=12):
    listaX[2]=(meses[mes])

print(listaX)

#dia
dia=int(listaX[0])#transforma o dia em inteiro
if dia not in lista1:
    d=dia
    dezena=dia//10
    unidade=dia%10
    if dezena == 1:
        if unidade == 8:
            dezena=lista2[10]
            unidade=lista2[unidade]
            dia =(dezena+unidade)
            listaX[0]=dia
        elif (unidade == 6) or (unidade == 7):
            dezena=("dezes")
            unidade=lista2[unidade]
            dia =(dezena+unidade)
            listaX[0]=dia    
        else:
            print("ta aqui")
            dezena=("dezes")
            unidade=lista2[unidade]
            dia =(dezena+unidade)
            listaX[0]=dia
        
print(listaX)
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