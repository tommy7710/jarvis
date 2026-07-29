import requests


def obtener_estado():

    try:

        respuesta = requests.get(
            "http://127.0.0.1:8765/status",
            timeout=5
        )

        return respuesta.json()

    except Exception as e:

        return {
            "error": str(e)
        }


if __name__ == "__main__":

    print(
        obtener_estado()
    )
