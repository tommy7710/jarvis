import subprocess
import json
import platform
import os
from datetime import datetime


def ejecutar(comando):

    try:
        resultado = subprocess.run(
            comando,
            shell=True,
            capture_output=True,
            text=True,
            timeout=5
        )

        if resultado.stdout:
            return resultado.stdout.strip()

        return None

    except:
        return None



def obtener_bateria():

    resultado = ejecutar(
        "termux-battery-status"
    )

    if not resultado:
        return {
            "disponible": False,
            "mensaje": "Sensor de batería no accesible"
        }


    try:

        datos = json.loads(resultado)

        return {
            "disponible": True,
            "porcentaje": datos.get("percentage"),
            "estado": datos.get("status"),
            "temperatura": datos.get("temperature")
        }

    except:

        return {
            "disponible": False,
            "mensaje": "Error leyendo batería"
        }



def obtener_memoria():

    memoria = {}

    try:

        datos = ejecutar(
            "cat /proc/meminfo"
        )

        for linea in datos.split("\n"):

            if "MemTotal" in linea or "MemAvailable" in linea:

                partes = linea.split()

                memoria[
                    partes[0].replace(":", "")
                ] = int(partes[1]) // 1024


    except Exception as e:

        memoria["error"] = str(e)


    return memoria



def obtener_sistema():

    return {

        "android": platform.system(),

        "arquitectura": platform.machine(),

        "hora": datetime.now().strftime(
            "%H:%M:%S"
        )

    }



def obtener_almacenamiento():

    try:

        total, usado, libre = os.statvfs("/").f_blocks, os.statvfs("/").f_blocks - os.statvfs("/").f_bfree, os.statvfs("/").f_bavail

        return {

            "total": round(total / 1024**3,2),

            "libre": round(libre / 1024**3,2)

        }

    except:

        return {
            "error":"No disponible"
        }



def obtener_sensores():

    return {

        "jarvis_sensor": "activo",

        "bateria": obtener_bateria(),

        "memoria": obtener_memoria(),

        "sistema": obtener_sistema(),

        "almacenamiento": obtener_almacenamiento()

    }
