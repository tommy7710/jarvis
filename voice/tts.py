import subprocess


def hablar(texto):

    texto = texto.replace(
        "JARVIS",
        "Yarvis"
    )

    texto = texto.replace(
        "Jarvis",
        "Yarvis"
    )


    subprocess.run(
        [
            "espeak-ng",
            "-v",
            "es",
            "-s",
            "145",
            "-p",
            "40",
            texto
        ]
    )
