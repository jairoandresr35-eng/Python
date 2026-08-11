# ══════════════════════════════════════
# SISTEMA DE NOTAS — Bloque 1
# Ingreso de datos de un estudiante
# ══════════════════════════════════════

nombre = input("Nombre del estudiante: ")

# ── Evaluaciones ──────────────────────
eval1 = input("Evaluación 1 (Enter si no hay nota): ")
eval2 = input("Evaluación 2 (Enter si no hay nota): ")

# ── Quizzes (5 en total) ──────────────
q1 = input("Quiz 1 (Enter si no hay nota): ")
q2 = input("Quiz 2 (Enter si no hay nota): ")
q3 = input("Quiz 3 (Enter si no hay nota): ")
q4 = input("Quiz 4 (Enter si no hay nota): ")
q5 = input("Quiz 5 (Enter si no hay nota): ")

# ── Trabajos (3 en total) ─────────────
t1 = input("Trabajo 1 (Enter si no hay nota): ")
t2 = input("Trabajo 2 (Enter si no hay nota): ")
t3 = input("Trabajo 3 (Enter si no hay nota): ")

# ── Otros ─────────────────────────────
refuerzo     = input("Refuerzo (Enter si no hay nota): ")
proyecto     = input("Proyecto (Enter si no hay nota): ")
participacion = input("Participación (Enter si no hay nota): ")

# ══════════════════════════════════════
# Bloque 2 — Convertir y validar notas
# ══════════════════════════════════════

def convertir_nota(valor, nombre_componente):
    if valor == "":
        return None
    try:
        nota = float(valor)
        if nota < 10 or nota > 100:
            print(f"  ADVERTENCIA: {nombre_componente}: la nota debe estar entre 10 y 100. Se omite.")
            return None
        return nota
    except ValueError:
        print(f"  ADVERTENCIA: {nombre_componente}: '{valor}' no es un número válido. Se omite.")
        return None

# ── Aplicar validación a cada nota ────
eval1 = convertir_nota(eval1, "Evaluación 1")
eval2 = convertir_nota(eval2, "Evaluación 2")

q1 = convertir_nota(q1, "Quiz 1")
q2 = convertir_nota(q2, "Quiz 2")
q3 = convertir_nota(q3, "Quiz 3")
q4 = convertir_nota(q4, "Quiz 4")
q5 = convertir_nota(q5, "Quiz 5")

t1 = convertir_nota(t1, "Trabajo 1")
t2 = convertir_nota(t2, "Trabajo 2")
t3 = convertir_nota(t3, "Trabajo 3")

refuerzo      = convertir_nota(refuerzo,      "Refuerzo")
proyecto      = convertir_nota(proyecto,      "Proyecto")
participacion = convertir_nota(participacion, "Participación")
# ══════════════════════════════════════
# Bloque 3 — Calcular puntos
# ══════════════════════════════════════

def calcular_aporte(nota, peso):
    if nota is None:
        return 0, 0  # puntos aportados, peso evaluado
    return (nota / 100) * peso, peso

# ── Evaluaciones ──────────────────────
pts_eval1, pct_eval1 = calcular_aporte(eval1, 20)
pts_eval2, pct_eval2 = calcular_aporte(eval2, 20)

# ── Quizzes — promedio de los ingresados ──
quizzes = [q for q in [q1, q2, q3, q4, q5] if q is not None]
if quizzes:
    promedio_quizzes = sum(quizzes) / len(quizzes)
    pts_quizzes, pct_quizzes = calcular_aporte(promedio_quizzes, 15)
else:
    promedio_quizzes = None
    pts_quizzes, pct_quizzes = 0, 0

# ── Trabajos — promedio de los ingresados ──
trabajos = [t for t in [t1, t2, t3] if t is not None]
if trabajos:
    promedio_trabajos = sum(trabajos) / len(trabajos)
    pts_trabajos, pct_trabajos = calcular_aporte(promedio_trabajos, 10)
else:
    promedio_trabajos = None
    pts_trabajos, pct_trabajos = 0, 0

# ── Otros ─────────────────────────────
pts_refuerzo,      pct_refuerzo      = calcular_aporte(refuerzo,      10)
pts_proyecto,      pct_proyecto      = calcular_aporte(proyecto,      15)
pts_participacion, pct_participacion = calcular_aporte(participacion, 10)

# ── Totales ───────────────────────────
puntos_acumulados   = pts_eval1 + pts_eval2 + pts_quizzes + pts_trabajos + pts_refuerzo + pts_proyecto + pts_participacion
porcentaje_evaluado = pct_eval1 + pct_eval2 + pct_quizzes + pct_trabajos + pct_refuerzo + pct_proyecto + pct_participacion
porcentaje_restante = 100 - porcentaje_evaluado

# ── Nota proyectada ───────────────────
if porcentaje_evaluado > 0:
    nota_proyectada = (puntos_acumulados / porcentaje_evaluado) * 100
else:
    nota_proyectada = 0

# ── Nota mínima en lo que falta ───────
puntos_necesarios = 70 - puntos_acumulados
if porcentaje_restante > 0:
    nota_minima = (puntos_necesarios / porcentaje_restante) * 100
else:
    nota_minima = None

# ── Verificación rápida ───────────────
print(f"\nPuntos acumulados:   {puntos_acumulados:.1f}")
print(f"Porcentaje evaluado: {porcentaje_evaluado}%")
print(f"Nota proyectada:     {nota_proyectada:.1f}")