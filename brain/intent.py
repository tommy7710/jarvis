def detectar_intencion(texto):

    texto = texto.lower().strip()


    # HORA

    if (
        texto == "hora"
        or "que hora es" in texto
        or "qué hora es" in texto
    ):
        return "hora"



    # FECHA

    if (
        "fecha" in texto
        or "que dia es hoy" in texto
        or "qué día es hoy" in texto
    ):
        return "fecha"



    # BATERÍA

    if (
        "bateria" in texto
        or "batería" in texto
    ):
        return "bateria"



    # CLIMA

    if (
        "clima" in texto
        or "tiempo" in texto
        or "temperatura" in texto
        or "pronostico" in texto
        or "pronóstico" in texto
    ):
        return "clima"



    # IDENTIDAD

    if (
        "quien soy" in texto
        or "quién soy" in texto
    ):
        return "identidad"



    # INTERNET / NAVEGADOR

    if (
        "internet" in texto
        or "navegador" in texto
        or "google" in texto
        or "buscar" in texto
    ):
        return "abrir_web"



    # CÁMARA

    if (
        "camara" in texto
        or "cámara" in texto
    ):
        return "camara"



    # AJUSTES

    if (
        "ajustes" in texto
        or "configuracion" in texto
        or "configuración" in texto
    ):
        return "ajustes"



    # APLICACIONES

    if (
        texto.startswith("abre ")
        or texto.startswith("abrir ")
        or "abre " in texto
    ):
        return "abrir_app"



    # CÁLCULOS

    if (
        "+" in texto
        or "-" in texto
        or "*" in texto
        or "/" in texto
    ):
        return "calculo"



    return "conversacion"
