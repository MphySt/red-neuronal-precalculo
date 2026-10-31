"""
Proyecto de Semestre - Precálculo
Universidad Mariano Gálvez - Facultad de Ingeniería en Sistemas
2do Semestre 2026

Aplicación de escritorio: abre la demo interactiva de la red neuronal
3-3-2-1 (index.html) en una ventana nativa.

    pip install -r requirements.txt
    python app.py
"""

from pathlib import Path

import webview

INDEX = Path(__file__).resolve().parent / "index.html"


def main():
    webview.create_window(
        "Red Neuronal 3-3-2-1 · Precálculo UMG",
        str(INDEX),
        width=1280,
        height=860,
        min_size=(900, 600),
    )
    webview.start()


if __name__ == "__main__":
    main()
