import streamlit as st
import requests

TOKEN = "8600601895:AAFV_LTM2pJ8Dva_n7iFhLIQh0aAT6o0uBQ"
CHAT_ID = 6745812236

def enviar_telegram(mensaje):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, data={
        "chat_id": CHAT_ID,
        "text": mensaje
    })

if "paso" not in st.session_state:
    st.session_state.paso = 0

if "datos" not in st.session_state:
    st.session_state.datos = {}

st.title("Página de empleo de informática")

if st.session_state.paso == 0:
    nombre = st.text_input("Hola, ¿cuál es tu nombre?")
    edad = st.number_input("¿Cuántos años tienes?", min_value=0, step=1)

    if st.button("Continuar"):
        st.session_state.datos["nombre"] = nombre
        st.session_state.datos["edad"] = edad
        st.session_state.paso += 1

elif st.session_state.paso == 1:
    ubicacion = st.text_input("¿Dónde vives?")
    nivel = st.selectbox(
        "¿Cuál es tu nivel educativo?",
        ["Primaria", "ESO", "Bachillerato", "Formación Profesional", "Grado universitario"]
    )

    if st.button("Continuar"):
        st.session_state.datos["ubicacion"] = ubicacion
        st.session_state.datos["nivel"] = nivel
        st.session_state.paso += 1

elif st.session_state.paso == 2:
    experiencia = st.selectbox("¿Tienes experiencia en el sector?", ["Sí", "No"])

    if experiencia == "Sí":
        años = st.number_input("¿Cuántos años de experiencia tienes?", min_value=0)
    else:
        años = 0

    if st.button("Continuar"):
        st.session_state.datos["experiencia"] = experiencia
        st.session_state.datos["años"] = años
        st.session_state.paso += 1

elif st.session_state.paso == 3:
    puntuacion = st.slider("¿Qué puntuación le das a esta página?", 1, 10)
    comentario = st.text_input("¿Alguna sugerencia?")

    if st.button("Enviar"):
        datos = st.session_state.datos

        mensaje = f"""
📋 Nuevo candidato:

👤 Nombre: {datos.get("nombre")}
🎂 Edad: {datos.get("edad")}
📍 Ubicación: {datos.get("ubicacion")}
🎓 Nivel: {datos.get("nivel")}
💼 Experiencia: {datos.get("experiencia")}
⭐ Puntuación: {puntuacion}
💬 Comentario: {comentario}
"""

        enviar_telegram(mensaje)

        st.success("¡Enviado correctamente 👍!")