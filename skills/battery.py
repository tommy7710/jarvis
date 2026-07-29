from android.sensors import obtener_sensores



def bateria():

    datos = obtener_sensores()


    bat = datos.get(
        "bateria",
        {}
    )


    if not bat.get("disponible"):

        return (
            "Señor, el sensor de batería "
            "no está disponible."
        )


    return (
        "Informe de batería:\n"
        f"Nivel: {bat.get('porcentaje')}%\n"
        f"Estado: {bat.get('estado')}\n"
        f"Temperatura: {bat.get('temperatura')}°C"
    )
