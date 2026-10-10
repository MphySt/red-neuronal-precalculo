# Red Neuronal 3-3-2-1 como Composición de Funciones

Proyecto de semestre de **Precálculo** — Universidad Mariano Gálvez, Facultad de Ingeniería en Sistemas, 2do Semestre 2026.

Autor: Moorphy Meda

## Objetivo

Demostrar que una red neuronal artificial es, internamente, una **composición de funciones** f(g(x)). Cada neurona aplica dos pasos:

1. **Transformación afín:** `z = (w₁·x₁) + (w₂·x₂) + ... + b`
2. **Activación:** `a = tanh(z)`, que mantiene el resultado entre -1 y 1

La salida de cada capa es la entrada de la siguiente:

```
Y = tanh(W⁴·tanh(W³·tanh(W²·X + b²) + b³) + b⁴)
```

## Arquitectura

| Capa | Neuronas | Recibe |
|---|---|---|
| 1 (entrada) | X₁, X₂, X₃ | — |
| 2 (oculta) | N1, N2, N3 | X₁, X₂, X₃ |
| 3 (oculta) | N4, N5 | a²₁, a²₂, a²₃ |
| 4 (salida) | N6 | a³₁, a³₂ |

## Demo interactiva

**https://mphyst.github.io/red-neuronal-precalculo/**

Página web ([index.html](index.html)) donde se pueden mover las entradas X₁, X₂, X₃ con controles deslizantes, hacer clic en cada neurona para ver su cálculo paso a paso (g(x) y luego f(z) = tanh(z)), ver la gráfica de tanh con cada neurona y animar la propagación capa por capa. No requiere instalación: también se puede abrir `index.html` directamente en el navegador.

## Cómo ejecutar

```bash
python red_neuronal.py
```

No requiere librerías externas (usa `math.tanh`).

Para regenerar el código QR:

```bash
pip install -r requirements.txt
python generar_qr.py
```

## Resultados

| Neurona | z | a = tanh(z) |
|---|---|---|
| N1 | 1.180000 | 0.827452 |
| N2 | -0.570000 | -0.515359 |
| N3 | -0.890000 | -0.711394 |
| N4 (ŷ₁) | 0.621942 | 0.552479 |
| N5 (ŷ₂) | -0.404826 | -0.384071 |
| N6 (Y) | 0.623522 | **0.553576** |

## Código QR del repositorio

![QR del repositorio](qr_repositorio.png)

## Referencias

- Flórez, R. (2018).
- Goodfellow, I., Bengio, Y. y Courville, A. (2016). *Deep Learning*. MIT Press.
