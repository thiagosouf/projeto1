#ano
def anoX(ano):
    milhar=ano//1000
    a=ano%1000
    centena=a//100
    a=ano%100
    dezena=a//10
    unidade=ano%10
    dia=ano%100
    if milhar == 1:
        if (centena==0) and (dezena==0) and (unidade==0):
            m=lista2[26] #mil
            ano=(m)
            return(ano) 
        if (centena==9) and (dezena==0) and (unidade==0):
            m=lista2[26] #mil
            u=lista2[9] #nove
            c=lista2[25] #centos
            ano=(m+" e "+u+c)
            return(ano) #mil/nove/centos
        else:
            if (centena==9):
                m=lista2[26] #mil
                u=lista2[9] #nove
                c=lista2[25] #centos
                d=diaX(dia)
                ano=(m+" "+u+c+" e "+d)
                return(ano)

    if milhar == 2:
        if (centena==0) and (dezena==0) and (unidade==0):
            u=lista2[2] #dois
            m=lista2[26] #mil
            ano=(u+" "+m)
            return(ano) 
        if (centena==1) and (dezena==0) and (unidade==0):
            u=lista2[2] #dois
            m=lista2[26] #mil
            c=lista2[24] #cem
            ano=(u+" "+m+" e "+c)
            return(ano) 
        else:
            if (centena==0):
                u=lista2[2] #dois
                m=lista2[26] #mil
                d=diaX(dia)
                ano=(u+" "+m+" e "+d)
                return(ano) 


#dia
def diaX(dia):
    dezena=dia//10
    unidade=dia%10

    if dezena == 0:
        return(lista2[dia])

    if dezena == 1:
        if (unidade == 8) or (unidade == 0):
            dezena=lista2[10]
            unidade=lista2[unidade]
            dia =(dezena+unidade)
            return(dia)
        elif (unidade == 6) or (unidade == 7):
            dezena=("dezes")
            unidade=lista2[unidade]
            dia =(dezena+unidade)
            return(dia)
        elif (unidade == 9):
            dezena=("deze")
            unidade=lista2[unidade]
            dia =(dezena+unidade)
            return(dia)
        else:            
            return(lista2[dia])
           
    if dezena == 2:
        if (unidade == 0):
            dezena=lista2[16]
            unidade=lista2[unidade]
            dia =(dezena+unidade)
            return(dia)        
        else:
            dezena=("vinte e ")
            unidade=lista2[unidade]
            dia =(dezena+unidade)
            return(dia)

    if dezena == 3:
        if (unidade == 0):
            return(lista2[17])        
        else:
            dezena=("trinta e ")
            unidade=lista2[unidade]
            dia =(dezena+unidade)
            return(dia)

    if dezena == 4:
        if (unidade == 0):
            return(lista2[18])        
        else:
            dezena=(lista2[18]+" e ")
            unidade=lista2[unidade]
            dia =(dezena+unidade)
            return(dia)
        
    if dezena == 5:
        if (unidade == 0):
            return(lista2[19])        
        else:
            dezena=(lista2[19]+" e ")
            unidade=lista2[unidade]
            dia =(dezena+unidade)
            return(dia)
        
    if dezena == 6:
        if (unidade == 0):
            return(lista2[20])        
        else:
            dezena=(lista2[20]+" e ")
            unidade=lista2[unidade]
            dia =(dezena+unidade)
            return(dia)
        
    if dezena == 7:
        if (unidade == 0):
            return(lista2[21])        
        else:
            dezena=(lista2[21]+" e ")
            unidade=lista2[unidade]
            dia =(dezena+unidade)
            return(dia)

    if dezena == 8:
        if (unidade == 0):
            return(lista2[22])        
        else:
            dezena=(lista2[22]+" e ")
            unidade=lista2[unidade]
            dia =(dezena+unidade)
            return(dia)
        
    if dezena == 9:
        if (unidade == 0):
            return(lista2[23])        
        else:
            dezena=(lista2[23]+" e ")
            unidade=lista2[unidade]
            dia =(dezena+unidade)
            return(dia)
    
#mes
def mesX(mes):
    return (meses[mes])
    
lista2=["","um","dois","tres","quatro","cinco","seis","sete","oito","nove","dez","onze","doze","treze","quatorze","quinze","vinte","trinta",
        "quarenta","cinquenta", "sessenta", "setenta", "oitenta", "noventa","cem","centos","mil","cento"]
meses=["","janeiro","fevereiro","marco","abril","maio","junho","julho","agosto","setembro","outrubro","novembro","dezembro"]
x=input("digite um numero: ")
x=x.replace(" "," de ")
listaX=x.split()
dia=int(listaX[0]) #transforma o dia em inteiro
mes=int(listaX[2]) #transforma o mes em inteiro
ano=int(listaX[4]) #transforma o ano em inteiro
if (dia<=31) and (mes<=12) and (ano>=1900) and (ano<2100):
    listaX[0]=diaX(dia)
    listaX[2]=mesX(mes)
    listaX[4]=anoX(ano)

    datatr=str(listaX).strip("[]")#retira os conchetes
    datatr=datatr.replace("'","")#retira as aspas
    datatr=datatr.replace(",","")#retira as virgulas
    print(datatr)
else:
    print("ERRO")



