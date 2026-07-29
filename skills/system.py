from datetime import datetime



def hora():

    ahora = datetime.now()

    return (
        f"Hora del dispositivo: "
        f"{ahora.strftime('%H:%M:%S')}\n"
        f"Fecha: "
        f"{ahora.strftime('%d/%m/%Y')}"
    )



def fecha():

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
        f"Fecha del dispositivo: "
        f"{ahora.strftime('%d/%m/%Y')}\n"
        f"Día: {dia}"
    )
