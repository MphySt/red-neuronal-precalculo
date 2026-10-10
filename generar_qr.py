"""
Genera un código QR que apunta al repositorio de GitHub del proyecto.
Requiere: pip install "qrcode[pil]"
"""

import qrcode

URL_REPOSITORIO = "https://github.com/MphySt/red-neuronal-precalculo"
ARCHIVO_SALIDA = "qr_repositorio.png"

qr = qrcode.QRCode(
    version=None,                                       # tamaño automático
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # tolera ~30% de daño
    box_size=12,
    border=4,
)
qr.add_data(URL_REPOSITORIO)
qr.make(fit=True)

imagen = qr.make_image(fill_color="black", back_color="white")
imagen.save(ARCHIVO_SALIDA)

print(f"QR generado: {ARCHIVO_SALIDA}")
print(f"Apunta a:    {URL_REPOSITORIO}")
