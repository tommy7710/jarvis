import subprocess



APLICACIONES = {

    "youtube": "com.google.android.youtube",

    "whatsapp": "com.whatsapp",

    "camara": "com.android.camera2",

    "ajustes": "com.android.settings"

}



def ejecutar_comando(accion, datos=None):

    if datos is None:
        datos = {}


    if accion == "abrir_app":

        return abrir_aplicacion(
            datos.get("app")
        )


    elif accion == "abrir_web":

        return abrir_web(
            datos.get("url")
        )


    elif accion == "camara":

        return abrir_aplicacion(
            "camara"
        )


    elif accion == "ajustes":

        return abrir_aplicacion(
            "ajustes"
        )


    return (
        "Señor, esa acción no está disponible."
    )



def abrir_aplicacion(nombre):

    if not nombre:

        return (
            "Señor, no indicó una aplicación."
        )


    nombre = nombre.lower().strip()


    paquete = APLICACIONES.get(nombre)


    if not paquete:

        return (
            f"Señor, no tengo configurada "
            f"la aplicación {nombre}."
        )


    try:

        subprocess.run(
            [
                "am",
                "start",
                "-a",
                "android.intent.action.MAIN",
                "-p",
                paquete
            ],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )


        return (
            f"Abriendo {nombre}, señor."
        )


    except Exception as e:

        return (
            f"Error ejecutando aplicación: {e}"
        )



def abrir_web(url):

    if not url:

        url = "https://www.google.com"


    try:

        subprocess.run(
            [
                "am",
                "start",
                "-a",
                "android.intent.action.VIEW",
                "-d",
                url
            ],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )


        return (
            "Abriendo navegador, señor."
        )


    except Exception as e:

        return (
            f"Error abriendo navegador: {e}"
        )
