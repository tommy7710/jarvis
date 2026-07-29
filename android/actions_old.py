import subprocess



def abrir_aplicacion(nombre):

    aplicaciones = {

        "youtube":
        "com.google.android.youtube",

        "chrome":
        "com.android.chrome",

        "camara":
        "com.android.camera"

    }


    paquete = aplicaciones.get(
        nombre.lower()
    )


    if not paquete:

        return (
            "Señor, no conozco esa aplicación."
        )


    try:

        subprocess.run(
            [
                "am",
                "start",
                "-n",
                f"{paquete}/.MainActivity"
            ],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )


        return (
            f"Abriendo {nombre}, señor."
        )


    except Exception as e:

        return f"Error ejecutando aplicación: {e}"
