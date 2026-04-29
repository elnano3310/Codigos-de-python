import requests

TOKEN = "8600601895:AAFV_LTM2pJ8Dva_n7iFhLIQh0aAT6o0uBQ"
CHAT_ID = 6745812236

def enviar_telegram(mensaje):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, data={
        "chat_id": CHAT_ID,
        "text": mensaje
    })

print("Bienvenid@ a la página de empleo de informática")

nombre = input("Hola, ¿cuál es su nombre?")
print("Encantad@", nombre)

edad = input("¿Cuántos años tienes?")

if edad < "16":
    print("Lo siento, no cumples con los requisitos para el puesto")

ubicación = input("¿Dónde vives?")

nivel_educativo = input("¿Cuál es tu nivel educativo?")

if nivel_educativo == "primaria" or nivel_educativo == "eso":
    print("Lo siento, no cumples con los requisitos para el puesto")

elif nivel_educativo == "bachillerato" or nivel_educativo == "formación profesional" or nivel_educativo == "grado universitario":
 if nivel_educativo == "bachillerato":
    tipo = input("¿Qué tipo de bachillerato tienes? ")
    
    if tipo == "tecnológico":
        print("Enhorabuena, cumples los requisitos para este puesto.")
    else:
        print("Lo siento, no cumples con los requisitos para este puesto.")

 elif nivel_educativo == "formación profesional":
    tipo = input("¿Qué tipo de formación profesional tienes? ")
    
    if tipo == "informática":
        print("Enhorabuena, cumples los requisitos para este puesto.")
    else:
        print("Lo siento, no cumples con los requisitos para este puesto.")

 elif nivel_educativo == "grado universitario":
    tipo = input("¿Qué grado universitario tienes? ")
    
    if tipo == "ingeniería informática":
        print("Enhorabuena, cumples los requisitos para este puesto.")
    else:
        print("Lo siento, no cumples con los requisitos para este puesto.")

experiencia = input("¿Tienes experiencia en el sector? (sí/no)")
if experiencia == "sí":
    años_experiencia = input("¿Cuántos años de experiencia tienes?")
    print("¡Genial! Tu experiencia es de", años_experiencia, "años.")

elif experiencia == "no":
    print("No te preocupes, todos empezamos sin experiencia alguna.")

comprobar = input("¿Quieres comprobar toda la información que has introducido? (sí/no)")
if comprobar == "sí":
    print("Nombre:", nombre)
    print("Edad:", edad)
    print("Ubicación:", ubicación)
    print("Nivel educativo:", nivel_educativo)
    print("Experiencia:", experiencia)
elif comprobar == "no":
    print("¡Gracias por tu tiempo, ", nombre, "!")
    
puntuacion = input("¿Que puntuación le darías a esta página de empleo? (1-10)")
if puntuacion >= "1" and puntuacion <= "9":
    comentario = input("¿Alguna sugerencia para mejorar esta página? ")
print("¡Gracias por el feedback, ", nombre, "!", "¡Lo tendremos en cuenta para mejorar la página!")

mensaje = f"""
📋 Nuevo candidato:

👤 Nombre: {nombre}
🎂 Edad: {edad}
📍 Ubicación: {ubicación}
🎓 Nivel educativo: {nivel_educativo}
💼 Experiencia: {experiencia}
⭐ Puntuación: {puntuacion}
💬 Comentario: {comentario}
"""

enviar_telegram(mensaje)