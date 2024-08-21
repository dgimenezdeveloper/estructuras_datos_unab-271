""" 
Ejercicio 1:  Dada  la  siguiente  información,  elija  una  estructura  de  datos  que  permita  guardarla 
adecuadamente. 
Guerra del Peloponeso 431 a.C  
Revolución de Mayo 1810 d.C  
Llegada de los españoles a América 1492 d.C  
Comienzo de la construcción de la gran Muralla China 214 a.C
"""

eventos_historicos = {
    'Guerra del Peloponeso': {
        'año': 431,
        'era': 'a.C'
    },
    'Revolución de Mayo': {
        'año': 1810,
        'era': 'd.C'
    },
    'Llegada de los españoles a América': {
        'año': 1492,
        'era': 'd.C'
    },
    'Comienzo de la construcción de la gran Muralla China': {
        'año': 214,
        'era': 'a.C'
    }
}

for evento, datos in eventos_historicos.items():
    print(f'{evento} - {datos["año"]} {datos["era"]}')