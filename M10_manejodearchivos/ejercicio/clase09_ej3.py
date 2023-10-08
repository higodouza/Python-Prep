montañas = {'nombre':[  'Everest','K2','Kanchenjunga','Lhotse','Makalu',
                        'Cho Oyu','Dhaulagiri','Manaslu','Nanga Parbat','Annapurna I'],
            'orden':[1,2,3,4,5,6,7,8,9,10],
            'cordillera':['Himalaya','Karakórum','Himalaya','Himalaya','Himalaya'
                        ,'Himalaya','Himalaya','Himalaya','Karakórum','Himalaya'],
            'pais': ['Nepal','Pakistán','Nepal','Nepal','Nepal','Nepal','Nepal','Nepal',
                    'Pakistán','Nepal'],
            'altura':[8849,8611,8586,8516,8485,8188,8167,8163,8125,8091]}


### aca se crea el archivo
import os
archivo = open('clase09_ej3.csv', 'w')


# aca se crea la fila de arriba, y para con un \n cuando en cuentra altura que es el ultimo key
for clave in montañas.keys():
    if (clave == 'altura'):
        archivo.write(clave+'\n')
    else:
        archivo.write(clave+',')
        
ind = 0 ## estas son las filas que se iran llenando como un registro en un DB, 10 veces
while (ind < 10):
    archivo.write(montañas['nombre'][ind]+',')
    archivo.write(str(montañas['orden'][ind])+',')
    archivo.write(montañas['cordillera'][ind]+',')
    archivo.write(montañas['pais'][ind]+',')
    archivo.write(str(montañas['altura'][ind])+'\n')
    ind += 1
    

archivo.close()

## Ver peso del archivo 
print('El archivo tiene un tamaño de', str(round(os.path.getsize('clase09_ej3.csv')/1024,2)),'MB')

# crear un dir nuevo 
os.makedirs('clase09_montañas_altas')

#copiar el archivo en un dir 
os.system('copy clase09_ej3.csv clase09_montañas_altas')

#lista los archivos de ese dir
os.listdir('./clase09_montañas_altas')