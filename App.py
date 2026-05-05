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

st.title("Proceso de selección - Informática")

# ===== DATOS PERSONALES =====
st.header("Datos personales")

nombre = st.text_input("Nombre")
genero = st.selectbox("Género", ["Hombre", "Mujer", "Otro", "Prefiero no decirlo"])
edad = st.number_input("Edad", min_value=0)

ubicacion = st.text_input("Ubicación")

# ===== FORMACIÓN (NUEVO SISTEMA LIMPIO) =====
st.header("Formación")

nivel = st.selectbox(
    "Nivel educativo",
    ["Primaria", "ESO", "Bachillerato", "Formación Profesional", "Grado universitario"]
)

opciones_formacion = {
    "Bachillerato": ["Ciencias y Tecnología", "Humanidades y Sociales", "Artes", "Otros"],
    "Formación Profesional": ["Informática / Tecnología", "Administración", "Electricidad", "Sanidad", "Otros"],
    "Grado universitario": ["Ingeniería / Informática", "Matemáticas / Física", "Empresa / Economía", "Otros"]
}

tipo_formacion = None

if nivel in opciones_formacion:
    tipo_formacion = st.selectbox(
        "¿Qué especialidad has cursado?",
        opciones_formacion[nivel]
    )

especialidad = st.text_input("Observaciones adicionales")

# ===== EXPERIENCIA =====
st.header("Experiencia y habilidades")

experiencia = st.selectbox("¿Tienes experiencia?", ["Sí", "No"])
años = st.number_input("Años de experiencia", min_value=0)

lenguajes = st.multiselect(
    "Lenguajes de programación",
    ["Python", "Java", "C++", "JavaScript", "Otros"]
)

ingles = st.selectbox("Nivel de inglés", ["Bajo", "Medio", "Alto"])
equipo = st.slider("Trabajo en equipo", 1, 10)
disponibilidad = st.selectbox("Disponibilidad", ["Inmediata", "1 mes", "Más de 1 mes"])

# ===== FEEDBACK =====
st.header("Feedback")

puntuacion = st.slider("Puntuación de la página", 1, 10)
comentario = st.text_input("Comentario")

# ===== BOTÓN FINAL =====
if st.button("Evaluar candidato"):

    apto = True
    motivos = []

    # ===== VALIDACIONES =====

    if edad < 18:
        apto = False
        motivos.append("Menor de edad")

    if nivel in ["Primaria", "ESO"]:
        apto = False
        motivos.append("Nivel educativo insuficiente")

    if nivel == "Bachillerato":
        if tipo_formacion != "Ciencias y Tecnología":
            apto = False
            motivos.append("Bachillerato no orientado a tecnología")

    if nivel == "Formación Profesional":
        if tipo_formacion != "Informática / Tecnología":
            apto = False
            motivos.append("FP no relacionada con informática")

    if nivel == "Grado universitario":
        if tipo_formacion != "Ingeniería / Informática":
            apto = False
            motivos.append("Grado no relacionado con informática")

    if experiencia == "No":
        apto = False
        motivos.append("Sin experiencia laboral")

    if len(lenguajes) == 0:
        apto = False
        motivos.append("No conoce lenguajes de programación")

    if ingles == "Bajo":
        apto = False
        motivos.append("Nivel de inglés bajo")

    if equipo < 5:
        apto = False
        motivos.append("Baja capacidad de trabajo en equipo")

    # ===== RESULTADO =====

    if apto:
        st.success("✅ APTO para el puesto")
        motivo_final = "Cumple todos los requisitos"
    else:
        st.error("❌ NO APTO")
        st.write("Motivos:")
        for m in motivos:
            st.write(f"- {m}")
        motivo_final = ", ".join(motivos)

    # ===== TELEGRAM =====

    mensaje = f"""
📋 Nuevo candidato:

👤 Nombre: {nombre}
⚧ Género: {genero}
🎂 Edad: {edad}
📍 Ubicación: {ubicacion}

🎓 Nivel: {nivel}
📚 Formación: {tipo_formacion if tipo_formacion else "N/A"}
📝 Observaciones: {especialidad}

💼 Experiencia: {experiencia} ({años} años)
💻 Lenguajes: {", ".join(lenguajes)}

🌍 Inglés: {ingles}
🤝 Equipo: {equipo}/10
⏱ Disponibilidad: {disponibilidad}

🎯 Resultado: {"APTO" if apto else "NO APTO"}
📌 Motivos: {motivos if motivos else "Ninguno"}

⭐ Puntuación: {puntuacion}
💬 Comentario: {comentario}
"""

    enviar_telegram(mensaje)
    st.success("Datos enviados correctamente 📲")
