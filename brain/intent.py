def detectar_intencion(texto):

    texto = texto.lower().strip()


    if (
        texto == "hora"
        or "que hora es" in texto
        or "qué hora es" in texto
    ):
        return "hora"


    if (
        "fecha" in texto
        or "que dia es hoy" in texto
        or "qué día es hoy" in texto
    ):
        return "fecha"


    if (
        "bateria" in texto
        or "batería" in texto
    ):
        return "bateria"


    if (
        "clima" in texto
        or "tiempo" in texto
        or "temperatura" in texto
        or "pronostico" in texto
        or "pronóstico" in texto
    ):
        return "clima"


    if (
        "quien soy" in texto
        or "quién soy" in texto
    ):
        return "identidad"


    if texto.startswith("abre "):
        return "abrir_app"


    if (
        "+" in texto
        or "-" in texto
        or "*" in texto
        or "/" in texto
    ):
        return "calculo"


    return "conversacion"
