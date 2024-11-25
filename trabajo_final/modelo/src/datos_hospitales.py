# src/datos_hospitales.py

def obtener_datos_hospitales():
    hospitales = [
        "Hospital Elizalde",
        "Hospital Fernandez",
        "Hospital Pirovano",
        "Hospital Rivadavia",
        "Hospital Durand",
        "Hospital Argerich",
        "Hospital Ramos Mejia",
        "Hospital Tornu",
        "Hospital Zubizarreta",
        "Hospital Santojanni"
    ]

    conexiones = [
        ("Hospital Elizalde", "Hospital Fernandez", 4),
        ("Hospital Elizalde", "Hospital Pirovano", 7),
        ("Hospital Fernandez", "Hospital Rivadavia", 2),
        ("Hospital Pirovano", "Hospital Rivadavia", 3),
        ("Hospital Rivadavia", "Hospital Durand", 5),
        ("Hospital Fernandez", "Hospital Durand", 6),
        ("Hospital Argerich", "Hospital Ramos Mejia", 8),
        ("Hospital Ramos Mejia", "Hospital Tornu", 4),
        ("Hospital Tornu", "Hospital Zubizarreta", 6),
        ("Hospital Zubizarreta", "Hospital Santojanni", 5),
        ("Hospital Santojanni", "Hospital Argerich", 7)
    ]

    return hospitales, conexiones

def cargar_datos_hospitales(grafo):
    hospitales, conexiones = obtener_datos_hospitales()
    for hospital in hospitales:
        grafo.agregar_vertice(hospital)
    for desde, hacia, peso in conexiones:
        grafo.agregar_arista(desde, hacia, peso)