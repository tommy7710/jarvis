import json
import os
from datetime import datetime


MEMORY_FILE = "data/memory.json"


MEMORIA_BASE = {
    "usuario": {
        "nombre": "",
        "forma_trato": "señor",
        "preferencias": [],
        "proyectos": [],
        "notas": []
    },
    "recuerdos": {},
    "historial": []
}


def cargar_memoria():
    if not os.path.exists(MEMORY_FILE):
        guardar_memoria(MEMORIA_BASE)
        return MEMORIA_BASE.copy()

    try:
        with open(MEMORY_FILE, "r", encoding="utf-8") as archivo:
            memoria = json.load(archivo)

        # Reparar datos faltantes
        for seccion, valores in MEMORIA_BASE.items():
            if seccion not in memoria:
                memoria[seccion] = valores

        return memoria

    except Exception:
        guardar_memoria(MEMORIA_BASE)
        return MEMORIA_BASE.copy()



def guardar_memoria(memoria):

    os.makedirs("data", exist_ok=True)

    with open(MEMORY_FILE, "w", encoding="utf-8") as archivo:
        json.dump(
            memoria,
            archivo,
            indent=4,
            ensure_ascii=False
        )



# =====================
# RECUERDOS GENERALES
# =====================

def recordar(clave, valor):

    memoria = cargar_memoria()

    memoria["recuerdos"][clave] = valor

    guardar_memoria(memoria)



def buscar_recuerdo(clave):

    memoria = cargar_memoria()

    return memoria["recuerdos"].get(clave)



def borrar_recuerdo(clave):

    memoria = cargar_memoria()

    if clave in memoria["recuerdos"]:
        del memoria["recuerdos"][clave]

    guardar_memoria(memoria)



# =====================
# USUARIO
# =====================

def guardar_usuario(campo, valor):

    memoria = cargar_memoria()

    memoria["usuario"][campo] = valor

    guardar_memoria(memoria)



def obtener_usuario(campo):

    memoria = cargar_memoria()

    return memoria["usuario"].get(campo)



# =====================
# PREFERENCIAS
# =====================

def agregar_preferencia(preferencia):

    memoria = cargar_memoria()

    if preferencia not in memoria["usuario"]["preferencias"]:
        memoria["usuario"]["preferencias"].append(preferencia)

    guardar_memoria(memoria)



def obtener_preferencias():

    memoria = cargar_memoria()

    return memoria["usuario"]["preferencias"]



# =====================
# PROYECTOS
# =====================

def agregar_proyecto(proyecto):

    memoria = cargar_memoria()

    memoria["usuario"]["proyectos"].append(proyecto)

    guardar_memoria(memoria)



def obtener_proyectos():

    memoria = cargar_memoria()

    return memoria["usuario"]["proyectos"]



# =====================
# NOTAS
# =====================

def agregar_nota(nota):

    memoria = cargar_memoria()

    memoria["usuario"]["notas"].append(
        {
            "texto": nota,
            "fecha": datetime.now().isoformat()
        }
    )

    guardar_memoria(memoria)



def obtener_notas():

    memoria = cargar_memoria()

    return memoria["usuario"]["notas"]



# =====================
# HISTORIAL
# =====================

def guardar_conversacion(usuario, respuesta):

    memoria = cargar_memoria()

    memoria["historial"].append(
        {
            "fecha": datetime.now().isoformat(),
            "usuario": usuario,
            "jarvis": respuesta
        }
    )

    # Guardar últimas 200 conversaciones
    memoria["historial"] = memoria["historial"][-200:]

    guardar_memoria(memoria)



# Compatibilidad con ai.py antiguo
def guardar_historial(usuario, respuesta):

    guardar_conversacion(usuario, respuesta)



def obtener_historial():

    memoria = cargar_memoria()

    return memoria["historial"]



# =====================
# PERFIL COMPLETO
# =====================

def obtener_perfil():

    memoria = cargar_memoria()

    return memoria["usuario"]



def reiniciar_memoria():

    guardar_memoria(MEMORIA_BASE)
