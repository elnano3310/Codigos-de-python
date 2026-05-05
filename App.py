import streamlit as st
import requests

# ===== TELEGRAM =====
TOKEN = "8600601895:AAFV_LTM2pJ8Dva_n7iFhLIQh0aAT6o0uBQ"
CHAT_ID = 6745812236

def enviar_telegram(mensaje):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, data={
        "chat_id": CHAT_ID,
        "text": mensaje
    })

# ===== ESTADO =====
if "paso" not in st.session_state:
    st.session_state.paso = 0

if "datos" not in st.session_state:
    st.session_state.datos = {}

if "apto" not in st.session_state:
    st.session_state.apto = True

st.title("Página de empleo de informática")

# ===== PASO 1 =====
if st.session_state.paso == 0:

    st.text_input("Hola, ¿cuál es tu nombre?", key="nombre")
    st.selectbox("¿Cuál es tu género?", ["Hombre", "Mujer", "Otro", "Prefiero no decirlo"], key="genero")
    st.number_input("¿Cuántos años tienes?", min_value=0, step=1, key="edad")

    if st.button("Continuar"):
        st.session_state.datos["nombre"] = st.session_state.nombre
        st.session_state.datos["genero"] = st.session_state.genero
        st.session_state.datos["edad"] = st.session_state.edad

        if st.session_state.edad < 16:
            st.session_state.apto = False

        st.session_state.paso += 1

# ===== PASO 2 =====
elif st.session_state.paso == 1:

    st.text_input("¿Dónde vives?", key="ubicacion")

    st.selectbox(
        "¿Cuál es tu nivel educativo?",
        ["Primaria", "ESO", "Bachillerato", "Formación Profesional", "Grado universitario"],
        key="nivel"
    )

    if st.button("Continuar"):
        st.session_state.datos["ubicacion"] = st.session_state.ubicacion
        st.session_state.datos["nivel"] = st.session_state.nivel

        if st.session_state.nivel in ["Primaria", "ESO"]:
            st.session_state.apto = False

        st.session_state.paso += 1

# ===== PASO 3 =====
elif st.session_state.paso == 2:

    nivel = st.session_state.datos["nivel"]

    if nivel == "Bachillerato":
        st.selectbox("Tipo de bachillerato", ["Tecnológico", "Otros"], key="tipo_bach")

    if nivel == "Formación Profesional":
        st.selectbox("Tipo de FP", ["Informática", "Otros"], key="tipo_fp")

    if nivel == "Grado universitario":
        st.selectbox("Grado", ["Ingeniería Informática", "Otros"], key="tipo_uni")

    st.selectbox("¿Tienes experiencia?", ["Sí", "No"], key="experiencia")

    if st.session_state.experiencia == "Sí":
        st.number_input("¿Cuántos años de experiencia?", min_value=0, key="años")

    if st.button("Continuar"):

        nivel = st.session_state.datos["nivel"]

        # VALIDACIONES
        if nivel == "Bachillerato" and st.session_state.tipo_bach != "Tecnológico":
            st.session_state.apto = False

        if nivel == "Formación Profesional" and st.session_state.tipo_fp != "Informática":
            st.session_state.apto = False

        if nivel == "Grado universitario" and st.session_state.tipo_uni != "Ingeniería Informática":
            st.session_state.apto = False

        st.session_state.datos["experiencia"] = st.session_state.experiencia

        st.session_state.paso += 1

# ===== PASO 4 =====
elif st.session_state.paso == 3:

    puntuacion = st.slider("¿Qué puntuación le das a la página?", 1, 10)
    comentario = st.text_input("¿Alguna sugerencia?")

    # RESULTADO FINAL
    if st.session_state.apto:
        st.success("✅ Eres APTO para el puesto")
        resultado = "APTO"
    else:
        st.error("❌ No cumples los requisitos")
        resultado = "NO APTO"

    if st.button("Enviar"):

        d = st.session_state.datos

        mensaje = f"""
📋 Nuevo candidato:

👤 Nombre: {d.get("nombre")}
⚧ Género: {d.get("genero")}
🎂 Edad: {d.get("edad")}
📍 Ubicación: {d.get("ubicacion")}
🎓 Nivel: {d.get("nivel")}
💼 Experiencia: {d.get("experiencia")}
🎯 Resultado: {resultado}
⭐ Puntuación: {puntuacion}
💬 Comentario: {comentario}
"""

        enviar_telegram(mensaje)

        st.success("Datos enviados correctamente 📲")
