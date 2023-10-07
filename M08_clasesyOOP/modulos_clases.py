class modulo8:
    
    #### metodo contructor
    def __init__ (self): 
        pass
    
    ### metodo para verificar que cada numero es o no primo
    def es_primo(self,numero):
        primo=True
        if numero == 0 or numero == 1 or numero == 2:
            pass
        else:
            for i in range(2,numero):
                if numero%i==0:
                    primo=False
                    break
            if primo:
                primo=True       
        return primo
    # metodo para ir recorriendo la lista y llamando a 
    # es_primo para hacer la comprobacion numero a numero
    
    def verificar_primo(self,lista):
        self.lista = lista
        resul=[]
        for i in lista:
            if self.es_primo(i):            
                resul.append(i)
        print(f"La lista resultante de los num primos de num_lista es: \n{resul}\n")

    ## metodo para ubicar el numero que se repite mas en una lista, viendo cuantas veces 
    ## se repite y mostrando ambos datos
    def valor_modal(self,lista):
        self.lista = lista
        a=0
        b=0
        for i in lista:
            for j in lista:
                if i==j:
                    a+=1
            if a>b:
                numero_mas_repe=i
                numero_de_repe=a
                b=a
            a=0
        print(f'El numero que mas se repite es: {numero_mas_repe}, {numero_de_repe} veces\n')

    ## metodo calculadora convertidor entre grados, kel, cel, far
    def convertidor_temp(self,temp, medida_origen, medida_destino):
        self.temp=temp
        self.medida_origen =medida_origen
        self.medida_destino = medida_destino
        
        cel_to_far = lambda cel: (cel*9/5)+32
        cel_to_kel = lambda cel: cel+273.15
        far_to_cel = lambda far: (far-32)*5/9
        far_to_kel = lambda far: (far-32)*5/9 + 273.15
        kel_to_cel = lambda kel: kel-273.15
        kel_to_far = lambda kel: ((kel-273.15)*9/5) + 32
        
        if self.medida_origen=="cel" and self.medida_destino=="far":
            print(f'{temp} {self.medida_origen} son {cel_to_far(temp)} {self.medida_destino}\n') 
        if self.medida_origen=="cel" and self.medida_destino=="kel":
            print(f'{temp} {self.medida_origen} son {cel_to_kel(temp)} {self.medida_destino}\n') 
        if self.medida_origen=="far" and self.medida_destino=="cel":
            print(f'{temp} {self.medida_origen} son {far_to_cel(temp)} {self.medida_destino}\n') 
        if self.medida_origen=="far" and self.medida_destino=="kel":
            print(f'{temp} {self.medida_origen} son {far_to_kel(temp)} {self.medida_destino}\n') 
        if self.medida_origen=="kel" and self.medida_destino=="cel":
            print(f'{temp} {self.medida_origen} son {kel_to_cel(temp)} {self.medida_destino}\n') 
        if self.medida_origen=="kel" and self.medida_destino=="far":
            print(f'{temp} {self.medida_origen} son {kel_to_far(temp)} {self.medida_destino}\n') 
    
    def factorial(self,numero):
        self.numero = numero
        if type(self.numero)==float or self.numero<0:
            return print("el numero ingresado debe entero y positivo")
        elif self.numero==0:
            return 1
        else:
            self.numero = self.numero * self.factorial(self.numero - 1)
            return self.numero
        


