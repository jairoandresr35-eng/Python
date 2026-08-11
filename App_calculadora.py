import streamlit as st

# ── Configuración de página ───────────────────────────────────────────────────
st.set_page_config(
    page_title="Mis Notas del Periodo",
    page_icon="📊",
    layout="centered"
)

# ── Estilos ───────────────────────────────────────────────────────────────────
st.markdown("""
<style>
    .titulo { font-size: 2rem; font-weight: 700; color: #1a1a2e; margin-bottom: 0; }
    .subtitulo { color: #555; font-size: 1rem; margin-bottom: 1.5rem; }
    .seccion { background: #f8f9fa; border-radius: 10px; padding: 1rem 1.2rem; margin-bottom: 1rem; }
    .resultado-box { border-radius: 12px; padding: 1.2rem 1.5rem; margin-bottom: 0.8rem; }
    .verde  { background: #d4edda; border-left: 5px solid #28a745; }
    .amarillo { background: #fff3cd; border-left: 5px solid #ffc107; }
    .rojo   { background: #f8d7da; border-left: 5px solid #dc3545; }
    .azul   { background: #d1ecf1; border-left: 5px solid #17a2b8; }
    .numero-grande { font-size: 2.2rem; font-weight: 800; }
    .etiqueta { font-size: 0.85rem; color: #555; text-transform: uppercase; letter-spacing: 0.05em; }
</style>
""", unsafe_allow_html=True)

# ── Encabezado ────────────────────────────────────────────────────────────────
st.markdown('<p class="titulo">📊 Mis Notas del Periodo</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitulo">Ingresa tus notas y ve cómo vas acumulando puntos</p>', unsafe_allow_html=True)

nombre = st.text_input("Tu nombre", placeholder="Escribe tu nombre aquí")

st.divider()

# ── Funciones auxiliares ──────────────────────────────────────────────────────
def nota_input(label, key):
    val = st.number_input(label, min_value=0.0, max_value=100.0, value=0.0,
                          step=0.5, key=key,
                          help="Deja en 0 si aún no tienes esta nota")
    return val if val > 0 else None

def calcular_aporte(nota, peso):
    if nota is None:
        return 0, 0
    return (nota / 100) * peso, peso

# ── Secciones de ingreso ──────────────────────────────────────────────────────
with st.expander("📝 Evaluaciones (20 pts c/u)", expanded=True):
    col1, col2 = st.columns(2)
    with col1:
        eval1 = nota_input("Evaluación 1", "eval1")
    with col2:
        eval2 = nota_input("Evaluación 2", "eval2")

with st.expander("⚡ Quizzes — promedio de los ingresados (15 pts)", expanded=True):
    col1, col2, col3 = st.columns(3)
    with col1:
        q1 = nota_input("Quiz 1", "q1")
        q2 = nota_input("Quiz 2", "q2")
    with col2:
        q3 = nota_input("Quiz 3", "q3")
        q4 = nota_input("Quiz 4", "q4")
    with col3:
        q5 = nota_input("Quiz 5", "q5")

with st.expander("📁 Trabajos — promedio de los ingresados (10 pts)", expanded=True):
    col1, col2, col3 = st.columns(3)
    with col1:
        t1 = nota_input("Trabajo 1", "t1")
    with col2:
        t2 = nota_input("Trabajo 2", "t2")
    with col3:
        t3 = nota_input("Trabajo 3", "t3")

with st.expander("🎯 Otros componentes", expanded=True):
    col1, col2, col3 = st.columns(3)
    with col1:
        refuerzo = nota_input("Refuerzo (10 pts)", "refuerzo")
    with col2:
        proyecto = nota_input("Proyecto (15 pts)", "proyecto")
    with col3:
        participacion = nota_input("Participación (10 pts)", "participacion")

st.divider()

# ── Calcular ──────────────────────────────────────────────────────────────────
if st.button("📊 Ver mis resultados", use_container_width=True, type="primary"):

    pts_eval1, pct_eval1 = calcular_aporte(eval1, 20)
    pts_eval2, pct_eval2 = calcular_aporte(eval2, 20)

    quizzes = [q for q in [q1, q2, q3, q4, q5] if q is not None]
    if quizzes:
        promedio_quizzes = sum(quizzes) / len(quizzes)
        pts_quizzes, pct_quizzes = calcular_aporte(promedio_quizzes, 15)
    else:
        pts_quizzes, pct_quizzes = 0, 0

    trabajos = [t for t in [t1, t2, t3] if t is not None]
    if trabajos:
        promedio_trabajos = sum(trabajos) / len(trabajos)
        pts_trabajos, pct_trabajos = calcular_aporte(promedio_trabajos, 10)
    else:
        pts_trabajos, pct_trabajos = 0, 0

    pts_refuerzo,      pct_refuerzo      = calcular_aporte(refuerzo,      10)
    pts_proyecto,      pct_proyecto      = calcular_aporte(proyecto,      15)
    pts_participacion, pct_participacion = calcular_aporte(participacion, 10)

    puntos_acumulados   = pts_eval1 + pts_eval2 + pts_quizzes + pts_trabajos + pts_refuerzo + pts_proyecto + pts_participacion
    porcentaje_evaluado = pct_eval1 + pct_eval2 + pct_quizzes + pct_trabajos + pct_refuerzo + pct_proyecto + pct_participacion
    porcentaje_restante = 100 - porcentaje_evaluado

    if porcentaje_evaluado > 0:
        nota_proyectada = (puntos_acumulados / porcentaje_evaluado) * 100
    else:
        nota_proyectada = 0

    puntos_necesarios = 70 - puntos_acumulados
    if porcentaje_restante > 0:
        nota_minima = (puntos_necesarios / porcentaje_restante) * 100
    else:
        nota_minima = None

    # ── Resultados ────────────────────────────────────────────────────────────
    if nombre:
        st.markdown(f"### Resultados de **{nombre}**")
    else:
        st.markdown("### Tus resultados")

    col1, col2 = st.columns(2)

    with col1:
        color = "verde" if puntos_acumulados >= 70 else "amarillo" if puntos_acumulados >= 50 else "rojo"
        st.markdown(f"""
        <div class="resultado-box {color}">
            <div class="etiqueta">Puntos acumulados</div>
            <div class="numero-grande">{puntos_acumulados:.1f}<span style="font-size:1rem"> / 100</span></div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class="resultado-box azul">
            <div class="etiqueta">Porcentaje evaluado</div>
            <div class="numero-grande">{porcentaje_evaluado}<span style="font-size:1rem">%</span></div>
            <div style="font-size:0.85rem; color:#555">Falta: {porcentaje_restante}%</div>
        </div>
        """, unsafe_allow_html=True)

    col3, col4 = st.columns(2)

    with col3:
        color_p = "verde" if nota_proyectada >= 70 else "amarillo" if nota_proyectada >= 60 else "rojo"
        st.markdown(f"""
        <div class="resultado-box {color_p}">
            <div class="etiqueta">Nota proyectada</div>
            <div class="numero-grande">{nota_proyectada:.1f}</div>
            <div style="font-size:0.85rem; color:#555">Si sigues igual hasta el final</div>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        if nota_minima is not None:
            if nota_minima <= 0:
                texto_minima = "¡Ya aprobaste! 🎉"
                color_m = "verde"
                val_minima = "—"
            elif nota_minima > 100:
                texto_minima = "Muy difícil alcanzar 70 pts"
                color_m = "rojo"
                val_minima = f"{nota_minima:.1f}"
            else:
                texto_minima = "En lo que falta para llegar a 70 pts"
                color_m = "amarillo"
                val_minima = f"{nota_minima:.1f}"

            st.markdown(f"""
            <div class="resultado-box {color_m}">
                <div class="etiqueta">Nota mínima necesaria</div>
                <div class="numero-grande">{val_minima}</div>
                <div style="font-size:0.85rem; color:#555">{texto_minima}</div>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="resultado-box verde">
                <div class="etiqueta">Nota mínima necesaria</div>
                <div class="numero-grande">¡Listo! 🎉</div>
                <div style="font-size:0.85rem; color:#555">Ya completaste el 100%</div>
            </div>
            """, unsafe_allow_html=True)

    # ── Desglose ──────────────────────────────────────────────────────────────
    st.divider()
    st.markdown("#### Desglose por componente")

    componentes = {
        "Evaluación 1 (20%)":   (pts_eval1,         pct_eval1),
        "Evaluación 2 (20%)":   (pts_eval2,         pct_eval2),
        "Quizzes (15%)":        (pts_quizzes,       pct_quizzes),
        "Trabajos (10%)":       (pts_trabajos,      pct_trabajos),
        "Refuerzo (10%)":       (pts_refuerzo,      pct_refuerzo),
        "Proyecto (15%)":       (pts_proyecto,      pct_proyecto),
        "Participación (10%)":  (pts_participacion, pct_participacion),
    }

    for comp, (pts, pct) in componentes.items():
        if pct > 0:
            porcentaje_logrado = (pts / pct) * 100
            barra = "🟩" * int(porcentaje_logrado // 20) + "⬜" * (5 - int(porcentaje_logrado // 20))
            st.markdown(f"**{comp}** — {pts:.1f} pts &nbsp; {barra}")
        else:
            st.markdown(f"**{comp}** — *(sin nota ingresada)*")