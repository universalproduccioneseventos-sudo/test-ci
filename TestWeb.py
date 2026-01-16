import streamlit as st
import random

# 1. CONFIGURACIÓN
st.set_page_config(page_title="Test de CI Pro", page_icon="🧠")

# FUNCIÓN PARA REINICIAR
def reiniciar_test():
    st.session_state.indice = 0
    st.session_state.aciertos = 0
    st.session_state.finalizado = False
    # Volvemos a elegir preguntas al azar
    st.session_state.preguntas = random.sample(st.session_state.banco, 5)

# 2. INICIALIZACIÓN DEL BANCO (Solo una vez)
if 'banco' not in st.session_state:
    st.session_state.banco = [
        ["¿Qué número sigue: 2, 4, 8, 16, ...?", "32", "24", "40", "A"],
        ["¿Cuál es el número que falta: 5, 10, 20, 40, ...?", "60", "80", "50", "B"],
        ["¿Qué número sigue: 1, 1, 2, 3, 5, ...?", "8", "7", "6", "A"],
        ["Si 3 gatos cazan 3 ratones en 3 min, ¿cuánto tarda 1 gato?", "1 min", "3 min", "9 min", "B"],
        ["¿Qué idioma se habla en Brasil?", "Español", "Francés", "Portugués", "C"],
        ["¿Cuál es el resultado de 2+2x2?", "8", "6", "4", "B"],
        ["¿Cuántos meses tienen 28 días?", "1", "Todos", "Depende", "B"]
    ]
    st.session_state.preguntas = random.sample(st.session_state.banco, 5)
    st.session_state.indice = 0
    st.session_state.aciertos = 0
    st.session_state.finalizado = False

# 3. INTERFAZ DE USUARIO
st.title("🧠 Mi Test de CI Interactivo")

# LÓGICA DE CONTROL (Aquí evitamos el IndexError)
if st.session_state.indice >= len(st.session_state.preguntas):
    st.session_state.finalizado = True

if not st.session_state.finalizado:
    # Mostramos el progreso
    progreso = (st.session_state.indice) / len(st.session_state.preguntas)
    st.progress(progreso)
    
    # Pregunta actual
    pregunta_actual = st.session_state.preguntas[st.session_state.indice]
    st.subheader(f"Pregunta {st.session_state.indice + 1}:")
    st.write(f"### {pregunta_actual[0]}")

    # Botones de respuesta
    col1, col2, col3 = st.columns(3)
    
    if col1.button(f"A) {pregunta_actual[1]}", key=f"btn_a_{st.session_state.indice}"):
        if pregunta_actual[4] == "A": st.session_state.aciertos += 1
        st.session_state.indice += 1
        st.rerun()

    if col2.button(f"B) {pregunta_actual[2]}", key=f"btn_b_{st.session_state.indice}"):
        if pregunta_actual[4] == "B": st.session_state.aciertos += 1
        st.session_state.indice += 1
        st.rerun()

    if col3.button(f"C) {pregunta_actual[3]}", key=f"btn_c_{st.session_state.indice}"):
        if pregunta_actual[4] == "C": st.session_state.aciertos += 1
        st.session_state.indice += 1
        st.rerun()

else:
    # 4. PANTALLA FINAL DE RESULTADOS
    st.balloons()
    ci = 70 + (st.session_state.aciertos * 12)
    st.success("## ¡Felicidades! Has terminado el test.")
    st.metric("Tu Coeficiente Intelectual estimado es:", ci)
    
    if st.button("Intentar de nuevo", on_click=reiniciar_test):
        st.rerun()