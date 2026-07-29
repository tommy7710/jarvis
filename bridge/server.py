import sys
import os
import json
import traceback
from http.server import BaseHTTPRequestHandler, HTTPServer


# =====================================
# RUTA DEL PROYECTO JARVIS
# =====================================

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

sys.path.insert(
    0,
    BASE_DIR
)


from brain.ai import responder


try:
    from voice.tts import hablar
except Exception:
    hablar = None



# =====================================
# CONFIGURACIÓN
# =====================================

HOST = "0.0.0.0"
PORT = 8080



# =====================================
# SERVIDOR JARVIS
# =====================================

class JarvisHandler(BaseHTTPRequestHandler):


    def log_message(self, formato, *args):
        """
        Mantener logs normales
        """
        print(
            "%s - - [%s] %s"
            %
            (
                self.client_address[0],
                self.log_date_time_string(),
                formato % args
            )
        )


    def responder_json(self, datos):

        respuesta = json.dumps(
            datos,
            ensure_ascii=False
        )


        self.send_response(200)

        self.send_header(
            "Content-Type",
            "application/json; charset=utf-8"
        )

        self.end_headers()


        self.wfile.write(
            respuesta.encode("utf-8")
        )



    # ===============================
    # Estado del servidor
    # ===============================

    def do_GET(self):

        if self.path == "/":

            self.responder_json(
                {
                    "jarvis": "online",
                    "sistema": "Android + Termux",
                    "servicio": "bridge",
                    "puerto": PORT
                }
            )

        else:

            self.responder_json(
                {
                    "error":
                    "Ruta no encontrada"
                }
            )



    # ===============================
    # Comunicación con Android
    # ===============================

    def do_POST(self):

        try:


            if self.path != "/jarvis":

                self.responder_json(
                    {
                        "error":
                        "Ruta incorrecta"
                    }
                )

                return



            tamaño = int(
                self.headers.get(
                    "Content-Length",
                    0
                )
            )


            datos = self.rfile.read(
                tamaño
            )


            recibido = json.loads(
                datos.decode("utf-8")
            )


            mensaje = recibido.get(
                "mensaje",
                ""
            )


            print(
                "📱 Android:",
                mensaje
            )


            if not mensaje:

                self.responder_json(
                    {
                        "respuesta":
                        "No escuché nada."
                    }
                )

                return



            # =========================
            # Cerebro
            # =========================

            respuesta = responder(
                mensaje
            )


            print(
                "🤖 JARVIS:",
                respuesta
            )



            # =========================
            # Voz
            # =========================

            if hablar:

                try:

                    hablar(
                        respuesta
                    )

                except Exception as voz_error:

                    print(
                        "Error voz:",
                        voz_error
                    )



            self.responder_json(
                {
                    "estado":
                    "ok",

                    "respuesta":
                    respuesta
                }
            )



        except Exception as error:


            print(
                "ERROR:",
                error
            )

            traceback.print_exc()


            self.responder_json(
                {
                    "estado":
                    "error",

                    "mensaje":
                    str(error)
                }
            )





# =====================================
# INICIO
# =====================================

def iniciar():

    print("=" * 45)
    print("🤖 JARVIS BRIDGE ONLINE")
    print("Sistema: Android + Termux")
    print(
        f"Escuchando: {HOST}:{PORT}"
    )
    print(
        "Esperando conexión de la app..."
    )
    print("=" * 45)


    servidor = HTTPServer(
        (
            HOST,
            PORT
        ),
        JarvisHandler
    )


    try:

        servidor.serve_forever()


    except Exception as error:

        print(
            "Error servidor:",
            error
        )


    finally:

        servidor.server_close()

        print(
            "🤖 JARVIS Bridge cerrado"
        )



if __name__ == "__main__":

    iniciar()
