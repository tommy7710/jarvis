from brain.ai import responder

print("=" * 40)
print("🤖 JARVIS ANDROID v0.1")
print("Escribe 'salir' para terminar.")
print("=" * 40)

while True:
    mensaje = input("\nTú: ")

    if mensaje.lower() == "salir":
        print("JARVIS: Hasta luego.")
        break

    respuesta = responder(mensaje)
    print("JARVIS:", respuesta)
