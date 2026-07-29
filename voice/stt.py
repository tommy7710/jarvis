import subprocess
import json


def escuchar():

    try:

        resultado = subprocess.run(
            [
                "termux-speech-to-text"
            ],
            capture_output=True,
            text=True,
            timeout=60
        )


        if not resultado.stdout:
            return ""


        datos = json.loads(
            resultado.stdout
        )


        return datos.get(
            "text",
            ""
        )


    except Exception as e:

        print(
            "Error de reconocimiento:",
            e
        )

        return ""
