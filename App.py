import streamlit as st
import requests

# ===== TELEGRAM =====
TOKEN = "T8600601895:AAFV_LTM2pJ8Dva_n7iFhLIQh0aAT6o0uBQ"
CHAT_ID = 6745812236
def enviar_telegram(mensaje):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, data={
        "chat_id": CHAT_ID,
        "text": mensaje
    })

# ===== INTERFAZ =====
st.title("Bienvenid@ a la página de empleo de informática")

nombre = st.text_input("Hola, ¿cuál es tu nombre?")

if nombre:
    st.write("Encantad@", nombre)

edad = st.number_input("¿Cuántos años tienes?", min_value=0, step=1)

ubicacion = st.text_input("¿Dónde vives?")

nivel_educativo = st.selectbox(
    "¿Cuál es tu nivel educativo?",
    ["Primaria", "ESO", "Bachillerato", "Formación Profesional", "Grado universitario"]
)

# ===== LÓGICA =====
if st.button("Continuar"):

    if edad < 16:
        st.error("Lo siento, no cumples con los requisitos para el puesto")
        st.stop()

    if nivel_educativo in ["Primaria", "ESO"]:
        st.error("Lo siento, no cumples con los requisitos para el puesto")
        st.stop()

    # BACHILLERATO
    if nivel_educativo == "Bachillerato":
        tipo = st.selectbox("¿Qué tipo de bachillerato tienes?", ["Tecnológico", "Otros"])

        if tipo == "Tecnológico":
            st.success("Enhorabuena, cumples los requisitos")
        else:
            st.error("Lo siento, no cumples con los requisitos")
            st.stop()

    # FP
    if nivel_educativo == "Formación Profesional":
        tipo = st.selectbox("¿Qué tipo de FP tienes?", ["Informática", "Otros"])

        if tipo == "Informática":
            st.success("Enhorabuena, cumples los requisitos")
        else:
            st.error("Lo siento, no cumples con los requisitos")
            st.stop()

    # UNIVERSIDAD
    if nivel_educativo == "Grado universitario":
        tipo = st.selectbox("¿Qué grado tienes?", ["Ingeniería Informática", "Otros"])

        if tipo == "Ingeniería Informática":
            st.success("Enhorabuena, cumples los requisitos")
        else:
            st.error("Lo siento, no cumples con los requisitos")
            st.stop()

    experiencia = st.selectbox("¿Tienes experiencia en el sector?", ["Sí", "No"])

    if experiencia == "Sí":
        años = st.number_input("¿Cuántos años de experiencia tienes?", min_value=0)

    comprobar = st.checkbox("¿Quieres comprobar toda la información?")

    if comprobar:
        st.write("Nombre:", nombre)
        st.write("Edad:", edad)
        st.write("Ubicación:", ubicacion)
        st.write("Nivel educativo:", nivel_educativo)
        st.write("Experiencia:", experiencia)

    puntuacion = st.slider("¿Qué puntuación le das a esta página?", 1, 10)

    comentario = st.text_input("¿Alguna sugerencia para mejorar?")

    st.success(f"¡Gracias por el feedback, {nombre}!")

    # ===== ENVIAR A TELEGRAM =====
    mensaje = f"""
📋 Nuevo candidato:

👤 Nombre: {nombre}
🎂 Edad: {edad}
📍 Ubicación: {ubicacion}
🎓 Nivel: {nivel_educativo}
💼 Experiencia: {experiencia}
⭐ Puntuación: {puntuacion}
💬 Comentario: {comentario}
"""

    enviar_telegram(mensaje)