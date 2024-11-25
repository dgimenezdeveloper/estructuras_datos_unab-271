def obtener_datos_diagnosticos():
    vertices = [
        "fiebre",
        "tos",
        "dolor de cabeza",
        "prueba de sangre",
        "prueba de radiografia",
        "prueba de pcr",
        "gripe",
        "neumonia",
        "covid-19"
    ]

    aristas = [
        ("fiebre", "prueba de sangre"),
        ("tos", "prueba de radiografia"),
        ("dolor de cabeza", "prueba de pcr"),
        ("prueba de sangre", "gripe"),
        ("prueba de radiografia", "neumonia"),
        ("prueba de pcr", "covid-19")
    ]

    return vertices, aristas