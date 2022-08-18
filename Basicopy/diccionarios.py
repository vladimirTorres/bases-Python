def run():
    mi_diccionario = {
        "llave1": 1,
        "llave2": 2,
        "llave3": 3,
    }

    print(mi_diccionario["llave1"])
    print(mi_diccionario["llave2"])
    print(mi_diccionario["llave3"])

    poblacion_paises = {
        "Argentina": 45632112,
        "Brasil": 215658125,
        "Colombia": 56423655
    }

    for pais in poblacion_paises.keys(): # muestra la llaves de un diccionario
        print(pais)

    for pobla in poblacion_paises.values(): # muestra la valor del diccionario
        print(pobla)

    for pai, poblaci in poblacion_paises.items():
        print(pai, "tiene", str(pobla), "habitantes")

if __name__ == "__main__":
    run()