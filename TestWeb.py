import streamlit as st
import random

# 1. CONFIGURACIÓN DE LA PÁGINA
st.set_page_config(page_title="Test de CI Pro", page_icon="🧠")

# FUNCIÓN PARA REINICIAR
def reiniciar_test():
    st.session_state.indice = 0
    st.session_state.aciertos = 0
    st.session_state.finalizado = False
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

# Lógica para terminar
if st.session_state.indice >= len(st.session_state.preguntas):
    st.session_state.finalizado = True

if not st.session_state.finalizado:
    # Mostramos progreso
    progreso = (st.session_state.indice) / len(st.session_state.preguntas)
    st.progress(progreso)
    
    pregunta_actual = st.session_state.preguntas[st.session_state.indice]
    st.subheader(f"Pregunta {st.session_state.indice + 1}:")
    st.write(f"### {pregunta_actual[0]}")

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
    # 4. PANTALLA FINAL CON TABLA DE RANGOS
    st.balloons()
    ci = 70 + (st.session_state.aciertos * 12)
    st.success(f"## ¡Test Finalizado!")
    st.metric("Tu Coeficiente Intelectual estimado es:", int(ci))
    
  import streamlit as st
import random

# 1. CONFIGURACIÓN (Línea verificada: Correcta)
st.set_page_config(page_title="Test de CI Profesional", page_icon="🧠")

# FUNCIÓN DE REINICIO (Línea verificada: Correcta)
# Se encarga de limpiar el progreso y elegir 10 preguntas nuevas del banco
def reiniciar_test():
    st.session_state.indice = 0
    st.session_state.aciertos = 0
    st.session_state.finalizado = False
    if 'banco' in st.session_state:
        st.session_state.preguntas = random.sample(st.session_state.banco, 10)

# 2. INICIALIZACIÓN DEL BANCO (Línea verificada: Estructura de lista correcta)
if 'banco' not in st.session_state:
    st.session_state.banco = [
        ["¿Qué número sigue: 2, 4, 8, 16, ...?", "32", "24", "40", "A"],
        ["¿Cuál es el número que falta: 5, 10, 20, 40, ...?", "60", "80", "50", "B"],
        ["¿Qué número sigue: 1, 1, 2, 3, 5, ...?", "8", "7", "6", "A"],
        ["Si 3 gatos cazan 3 ratones en 3 min, ¿cuánto tarda 1 gato?", "1 min", "3 min", "9 min", "B"],
        ["¿Qué idioma se habla en Brasil?", "Español", "Francés", "Portugués", "C"],
        ["¿Cuál es el resultado de 2+2x2?", "8", "6", "4", "B"],
        ["¿Cuántos meses tienen 28 días?", "1", "Todos", "Depende", "B"],
        ["¿Qué pesa más: un kilo de hierro o un kilo de paja?", "Hierro", "Paja", "Pesan igual", "C"],
        ["Si el hijo de Juan es el padre de mi hijo, ¿qué soy yo de Juan?", "Su hijo", "Su nieto", "Su padre", "A"],
        ["¿Qué número sigue la serie: 1, 4, 9, 16, 25, ...?", "30", "36", "42", "B"],
        ["París es a Francia como Madrid es a...", "España", "Italia", "Portugal", "A"],
        ["¿Cuál es el planeta más cercano al Sol?", "Tierra", "Marte", "Mercurio", "C"],
        ["¿Cuántas patas tiene una araña?", "6", "8", "10", "B"],
        ["¿Qué gas necesitamos para respirar?", "Hidrógeno", "Oxígeno", "Nitrógeno", "B"],
        ["¿Cuál es el océano más grande?", "Atlántico", "Índico", "Pacífico", "C"]
        # PUEDES AGREGAR MÁS AQUÍ SIGUIENDO EL MISMO FORMATO
    ]
    # Selección inicial de 10 preguntas
    st.session_state.preguntas = random.sample(st.session_state.banco, 10)
    st.session_state.indice = 0
    st.session_state.aciertos = 0
    st.session_state.finalizado = False

# 3. LÓGICA DE NAVEGACIÓN (Línea verificada: Evita el error 'Index Out of Range')
if st.session_state.indice >= len(st.session_state.preguntas):
    st.session_state.finalizado = True

# 4. INTERFAZ DE USUARIO
st.title("🧠 Test de Inteligencia Profesional")

if not st.session_state.finalizado:
    # Barra de progreso
    progreso = (st.session_state.indice) / len(st.session_state.preguntas)
    st.progress(progreso)
    
    # Extraer pregunta actual
    pregunta_actual = st.session_state.preguntas[st.session_state.indice]
    
    st.subheader(f"Pregunta {st.session_state.indice + 1} de 10")
    st.info(f"### {pregunta_actual[0]}")

    # Columnas para los botones (Línea verificada: Estética y funcionalidad)
    col1, col2, col3 = st.columns(3)
    
    # Sistema de respuestas con llaves únicas para evitar conflictos
    if col1.button(f"A) {pregunta_actual[1]}", key=f"a_{st.session_state.indice}"):
        if pregunta_actual[4] == "A": st.session_state.aciertos += 1
        st.session_state.indice += 1
        st.rerun()

    if col2.button(f"B) {pregunta_actual[2]}", key=f"b_{st.session_state.indice}"):
        if pregunta_actual[4] == "B": st.session_state.aciertos += 1
        st.session_state.indice += 1
        st.rerun()

    if col3.button(f"C) {pregunta_actual[3]}", key=f"c_{st.session_state.indice}"):
        if pregunta_actual[4] == "C": st.session_state.aciertos += 1
        st.session_state.indice += 1
        st.rerun()

else:
    # 5. RESULTADOS FINALES (Línea verificada: Matemática exacta)
    st.balloons()
    # Fórmula: 70 base + (7 puntos por acierto). Máximo = 140.
    ci_resultado = 70 + (st.session_state.aciertos * 7)
    
    st.success("## 🎉 ¡Análisis Completado!")
    st.metric("Tu Coeficiente Intelectual es:", f"{ci_resultado} pts")
    st.write(f"Respondiste correctamente **{st.session_state.aciertos}** de 10 preguntas.")
    
    # Tabla de rangos profesional
    st.divider()
    st.subheader("📊 Escala de Inteligencia")
    tabla = {
        "Puntaje CI": ["130+", "120-129", "110-119", "90-109", "80-89", "<80"],
        "Clasificación": ["Muy Superior", "Superior", "Promedio Alto", "Promedio Normal", "Promedio Bajo", "Muy Bajo"]
    }
    st.table(tabla)
    
    # Botón de reinicio
    st.button("Realizar otra evaluación", on_click=reiniciar_test)