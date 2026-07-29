from datetime import datetime
import platform


def obtener_hora():

    ahora = datetime.now()

    return (
        f"Hora del dispositivo: {ahora.strftime('%H:%M:%S')}\n"
        f"Fecha: {ahora.strftime('%d/%m/%Y')}"
    )



def obtener_fecha():

    ahora = datetime.now()

    dias = {
        "Monday": "lunes",
        "Tuesday": "martes",
        "Wednesday": "miércoles",
        "Thursday": "jueves",
        "Friday": "viernes",
        "Saturday": "sábado",
        "Sunday": "domingo"
    }

    dia = dias.get(
        ahora.strftime("%A"),
        ahora.strftime("%A")
    )

    return (
        f"Fecha del dispositivo: {ahora.strftime('%d/%m/%Y')}\n"
        f"Día: {dia}"
    )



def estado_android():

    ahora = datetime.now()

    return (
        "Estado del sistema Android:\n"
        f"- Hora: {ahora.strftime('%H:%M:%S')}\n"
        "- Termux: activo\n"
        "- Núcleo JARVIS: online\n"
        f"- Arquitectura: {platform.machine()}"
    )
