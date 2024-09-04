""" 
Ejercicio 1:  Dada  la  siguiente  información,  elija  una  estructura  de  datos  que  permita  guardarla 
adecuadamente. 
Guerra del Peloponeso 431 a.C  
Revolución de Mayo 1810 d.C  
Llegada de los españoles a América 1492 d.C  
Comienzo de la construcción de la gran Muralla China 214 a.C
"""

eventos_historicos = {
    'Guerra del Peloponeso': {'anio':431, 'era':'aC'},
    'Revolución de Mayo': {'anio':1810, 'era':'dC'},
    'Llegada de los españoles a América': {'anio':1492, 'era':'dC'},
    'Comienzo de la construcción de la gran Muralla China': {'anio':214, 'era':'aC'}
}

def mostrar_eventos(d_eventos):
    for evento,detalles in d_eventos.items():
        print(f'{evento} {detalles['anio']} {detalles['era']}')

if __name__=='__main__':
    mostrar_eventos(eventos_historicos)