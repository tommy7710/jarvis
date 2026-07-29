import requests

from config import GROQ_API_KEY, MODEL

from brain.memory import (
    recordar,
    buscar_recuerdo,
    guardar_historial
)

from brain.personality import Personality
from brain.intent import detectar_intencion


from skills.system import (
    hora,
    fecha
)

from skills.battery import bateria
from skills.weather import clima


URL = "https://api.groq.com/openai/v1/chat/completions"


personalidad = Personality()



def responder(mensaje):

    texto = mensaje.lower().strip()



    # ==============================
    # Guardar nombre del usuario
    # ==============================

    if "mi nombre es" in texto:

        nombre = (
            texto.split(
                "mi nombre es"
            )[-1]
            .strip()
        )


        if nombre:

            nombre = nombre.title()


            recordar(
                "nombre",
                nombre
            )


            return (
                f"Perfecto, señor. "
                f"He guardado su nombre como {nombre}."
            )



    # ==============================
    # Comandos rápidos del sistema
    # ==============================

    intencion = detectar_intencion(
        mensaje
    )


    respuesta = None



    if intencion == "hora":

        respuesta = hora()



    elif intencion == "fecha":

        respuesta = fecha()



    elif intencion == "bateria":

        respuesta = bateria()



    elif intencion == "clima":

        respuesta = clima()



    elif intencion == "identidad":

        nombre = buscar_recuerdo(
            "nombre"
        )


        if nombre:

            respuesta = (
                f"Usted es {nombre}, señor. "
                "Es el usuario registrado en mi memoria."
            )

        else:

            respuesta = (
                "Señor, todavía no tengo "
                "información guardada sobre usted."
            )



    # ==============================
    # Nuevos comandos naturales
    # ==============================

    if respuesta is None:


        if "quien soy" in texto:

            nombre = buscar_recuerdo(
                "nombre"
            )


            if nombre:

                respuesta = (
                    f"Usted es {nombre}, señor. "
                    "Mi usuario registrado."
                )

            else:

                respuesta = (
                    "Todavía no tengo su nombre "
                    "guardado."
                )



        elif (
            "estado del sistema" in texto
            or "estado de jarvis" in texto
        ):

            respuesta = (
                "Sistema JARVIS operativo, señor. "
                "Núcleo de inteligencia activo."
            )



    # ==============================
    # Devolver respuesta local
    # ==============================

    if respuesta:


        guardar_historial(
            mensaje,
            respuesta
        )


        return respuesta



    # ==============================
    # Inteligencia Groq
    # ==============================


    nombre = buscar_recuerdo(
        "nombre"
    )


    contexto = personalidad.obtener_personalidad(
        nombre
    )


    headers = {

        "Authorization":
        f"Bearer {GROQ_API_KEY}",

        "Content-Type":
        "application/json"

    }



    data = {

        "model": MODEL,

        "messages": [

            {
                "role": "system",
                "content": contexto
            },


            {
                "role": "user",
                "content": mensaje
            }

        ]

    }



    try:


        respuesta = requests.post(

            URL,

            headers=headers,

            json=data,

            timeout=30

        )


        respuesta.raise_for_status()



        datos = respuesta.json()



        resultado = (

            datos["choices"][0]

            ["message"]

            ["content"]

        )



        guardar_historial(

            mensaje,

            resultado

        )


        return resultado



    except Exception as e:


        return (

            "Señor, tuve un problema "
            "con mi conexión inteligente: "
            f"{e}"

        )
