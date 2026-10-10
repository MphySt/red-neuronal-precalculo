"""
Proyecto de Semestre - Precálculo
Universidad Mariano Gálvez - Facultad de Ingeniería en Sistemas
2do Semestre 2026

Red neuronal artificial 3-3-2-1 como composición de funciones f(g(x)).
Cada neurona realiza dos pasos:
    1. Transformación afín:   z = (w1·x1) + (w2·x2) + ... + b
    2. Activación no lineal:  a = tanh(z)
La salida de cada capa es la entrada de la siguiente.
"""

import math

DECIMALES = 6  # el proyecto exige mínimo 4; se muestran 6 para mayor precisión


# ---------------------------------------------------------------------------
# 1. DATOS DE ENTRADA
# ---------------------------------------------------------------------------
X1, X2, X3 = 0.5, -0.8, 1.2
entradas = [X1, X2, X3]

# ---------------------------------------------------------------------------
# 2. PESOS Y SESGOS
#    Notación: w2_jk = peso de la capa 2 que va de la entrada k a la neurona j
# ---------------------------------------------------------------------------

# Capa 2 (capa oculta, 3 neuronas: N1, N2, N3)
w2_11, w2_12, w2_13, b2_1 = 0.4, -0.2, 0.6, 0.1     # N1
w2_21, w2_22, w2_23, b2_2 = -0.5, 0.3, 0.1, -0.2    # N2
w2_31, w2_32, w2_33, b2_3 = 0.2, 0.7, -0.4, 0.05    # N3

# Capa 3 (capa oculta, 2 neuronas: N4, N5)
w3_11, w3_12, w3_13, b3_1 = 0.7, -0.4, 0.3, 0.05    # N4
w3_21, w3_22, w3_23, b3_2 = -0.3, 0.8, -0.5, -0.1   # N5

# Capa 4 (capa de salida, 1 neurona: N6)
w4_11, w4_12, b4_1 = 0.6, -0.5, 0.1                 # N6


# ---------------------------------------------------------------------------
# 3. FUNCIONES
# ---------------------------------------------------------------------------
def suma_ponderada(valores, pesos, sesgo):
    """g(x): transformación afín lineal  z = Σ(w·x) + b"""
    z = 0.0
    for x, w in zip(valores, pesos):
        z += w * x
    return z + sesgo


def activacion(z):
    """f(z): función de activación tangente hiperbólica, rango (-1, 1)"""
    return math.tanh(z)


def neurona(valores, pesos, sesgo):
    """Composición f(g(x)): devuelve la suma ponderada z y su activación a"""
    z = suma_ponderada(valores, pesos, sesgo)
    a = activacion(z)
    return z, a


def mostrar(etiqueta_z, z, etiqueta_a, a):
    """Imprime un par (z, a) sin redondear los valores usados en el cálculo"""
    print(f"  {etiqueta_z:<6} = {z:>{DECIMALES + 4}.{DECIMALES}f}    "
          f"{etiqueta_a:<10} = {a:>{DECIMALES + 4}.{DECIMALES}f}")


# ---------------------------------------------------------------------------
# 4. PROPAGACIÓN HACIA ADELANTE (FORWARD PASS)
# ---------------------------------------------------------------------------
def main():
    linea = "=" * 60
    print(linea)
    print("  RED NEURONAL 3-3-2-1  |  Proyecto de Precálculo UMG")
    print(linea)
    print(f"  Entradas: X1 = {X1}, X2 = {X2}, X3 = {X3}\n")

    # --- Etapa 1: Capa 2 (recibe X1, X2, X3) ---
    z2_1, a2_1 = neurona(entradas, [w2_11, w2_12, w2_13], b2_1)
    z2_2, a2_2 = neurona(entradas, [w2_21, w2_22, w2_23], b2_2)
    z2_3, a2_3 = neurona(entradas, [w2_31, w2_32, w2_33], b2_3)

    print("ETAPA 1 - Capa oculta 2 (N1, N2, N3)")
    mostrar("z²₁", z2_1, "a²₁", a2_1)
    mostrar("z²₂", z2_2, "a²₂", a2_2)
    mostrar("z²₃", z2_3, "a²₃", a2_3)

    # --- Etapa 2: Capa 3 (recibe a²₁, a²₂, a²₃) ---
    salidas_capa2 = [a2_1, a2_2, a2_3]
    z3_1, a3_1 = neurona(salidas_capa2, [w3_11, w3_12, w3_13], b3_1)
    z3_2, a3_2 = neurona(salidas_capa2, [w3_21, w3_22, w3_23], b3_2)

    print("\nETAPA 2 - Capa oculta 3 (N4, N5)")
    mostrar("z³₁", z3_1, "a³₁ (ŷ₁)", a3_1)
    mostrar("z³₂", z3_2, "a³₂ (ŷ₂)", a3_2)

    # --- Etapa 3: Capa 4 (recibe a³₁, a³₂) ---
    salidas_capa3 = [a3_1, a3_2]
    z4_1, Y = neurona(salidas_capa3, [w4_11, w4_12], b4_1)

    print("\nETAPA 3 - Capa de salida 4 (N6)")
    mostrar("z⁴₁", z4_1, "Y", Y)

    # --- Resumen ---
    print("\n" + linea)
    print("  RESULTADOS FINALES")
    print(linea)
    print(f"  ŷ₁ = a³₁ = {a3_1:.{DECIMALES}f}")
    print(f"  ŷ₂ = a³₂ = {a3_2:.{DECIMALES}f}")
    print(f"  Y  = tanh(z⁴₁) = {Y:.{DECIMALES}f}")
    print(linea)
    print("  Composición: Y = tanh(W⁴·tanh(W³·tanh(W²·X + b²) + b³) + b⁴)")
    print(linea)


if __name__ == "__main__":
    main()
