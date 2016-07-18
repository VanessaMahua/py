class Fecha():
    def __init__(self,dia,mes,anio):
        self.dia=dia
        self.mes=mes
        self.anio=anio
    def mostrar(self):
        return str(self.dia)+"+"+str(self.mes)+"+"+str(self.anio)
    def modificar_Fecha(self):
        '''aux = tiempo.split(',')
        dia = int(aux[0])
        mes = int(aux[1])
        anio = int(aux[2])'''

        
        if (self.anio % 4 == 0 and self.anio % 100 != 0 or self.anio % 400 == 0):
            print("El año "+str(self.anio)+" Si es bisiesto ")
            if self.mes ==1:
                if self.dia>0 and self.dia<32:#enero
                    d=self.dia+1
                    hoy=Fecha(d,mes,anio)
                    return hoy
                else:
                    d=self.dia+1
                    m=self.mes+1
                    hoy=Fecha(d,m,anio)
                    return hoy  
                
        else:
            print("El año "+str(self.anio)+" No es bisiesto ")
hoy=
'''
# Casos.
if segundos != 60:
    tiempo = (horas, minutos, segundos)
else:
    if minutos == 59 and horas == 23:
        tiempo = (0, 0, 0)
    else:
        if minutos == 59:
            tiempo = (horas + 1, 0, 0)
        else:
            tiempo = (horas, minutos + 1, 0)'''
******************************************************************+
class Fecha():
    def __init__(self,dia,mes,anio):
        self.__dia = 1
    def getDia(self):
        return self.__dia
    def setDia(self, dia):
        if dia > 0 and dia < 31:
            self.__dia = dia
        else:
            print("Error")
mi_fecha = Fecha()
mi_fecha.setDia(33)

#
class Fecha():
    def __init__(self,dia,mes,anio):
        aux = tiempo.split(',')
        dia = int(aux[0])
        mes = int(aux[1])
        anio = int(aux[2])
        # Aumentamos un segundo.
segundos += 1

# Casos.
if segundos != 60:
    tiempo = (horas, minutos, segundos)
else:
    if minutos == 59 and horas == 23:
        tiempo = (0, 0, 0)
    else:
        if minutos == 59:
            tiempo = (horas + 1, 0, 0)
        else:
            tiempo = (horas, minutos + 1, 0)
        
# Pedimos datos.
tiempo = raw_input('Introduce tiempo: ')

# Obtenemos datos.
aux = tiempo.split(',')
horas = int(aux[0])
minutos = int(aux[1])
segundos = int(aux[2])

# Aumentamos un segundo.
segundos += 1

# Casos.
if segundos != 60:
    tiempo = (horas, minutos, segundos)
else:
    if minutos == 59 and horas == 23:
        tiempo = (0, 0, 0)
    else:
        if minutos == 59:
            tiempo = (horas + 1, 0, 0)
        else:
            tiempo = (horas, minutos + 1, 0)

# E imprimimos resultado (una tupla).
print tiempo

