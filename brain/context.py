from brain.memory import buscar_recuerdo



def obtener_contexto():

    nombre = buscar_recuerdo("nombre")


    if nombre:

        return {
            "nombre": nombre
        }


    return {}
