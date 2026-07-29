import datetime


def comando_sistema(texto):

    texto = texto.lower()


    # HORA
    if "hora" in texto:

        ahora = datetime.datetime.now()

        return (
            f"Señor Tomy, son las "
            f"{ahora.strftime('%H:%M:%S')}."
        )


    # FECHA
    if "fecha" in texto or "día" in texto:

        ahora = datetime.datetime.now()

        return (
            f"Señor Tomy, hoy es "
            f"{ahora.strftime('%d/%m/%Y')}."
        )


    return None
