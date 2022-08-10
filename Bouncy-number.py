#Creamos la clase bouncy
class Bouncy1:
    def __init__(self, porcentaje):
        self.porcentaje=porcentaje
    #Función para determinar si un número es Bouncy o no.
    def Es_bouncy(self,num):
        #se pasa el numero a string
        n=str(num)
        #este comando convierte el string en una lista organizada en forma ascendente
        a=sorted(n)
        #invierte la lista anterior para tenerla el número en una lista descedente
        d=a[::-1]
        #convertimos el numero original a una lista
        nu=list(n)
        #si el numero original no es igual a su forma ascende o descente entonces es buncy
        '''Por ejemplo:1234 es ascendete, cuando lo organizamos en forma "asecendete" 
        por logica sigue igual, por tanto si los comparamos van a ser los mismo. '''
        if(nu!=a and nu!=d):
            return(True)
        else:
            return(False)
    #Función que calcula el ultimo numero Bouncy dado un porcentaje
    def Numero(self):
        #variables iniciales
        i=0 
        b=0 
        bol=True
        while bol:
            i=i+1#contador
            if(self.Es_bouncy(i)): #si es Bouncy va contado
                b=b+1#contador
            #Calcula el porcentaje en cada ciclo por regla de tres
            porcen=(b*100)/i
            #verifica si el porcentaje aun no es el indicado, esto permite que se repita 
            #el ciclo
            if(porcen!=self.porcentaje):
                bol=True
            else:
                bol=False
        print(i)  
b=Bouncy(99)
b.Numero()
