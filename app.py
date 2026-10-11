
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Explorador del Valle Inquietante",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 Explorador del Valle Inquietante")

st.write(
    "Bienvenido a esta experiencia interactiva. "
    "Evalúa diferentes rostros según su apariencia humana "
    "y el nivel de inquietud que te producen."
)

st.info(
    "Tus respuestas nos ayudarán a explorar la relación "
    "entre el realismo humano y la inquietud percibida."
)

st.header("1. Evalúa las imágenes")

imagenes = [
    {
        "nombre": "Rostro artificial",
        "realismo": 1,
        "url": "https://placehold.co/500x350?text=Rostro+artificial"
    },
    {
        "nombre": "Rostro estilizado",
        "realismo": 3,
        "url": "https://placehold.co/500x350?text=Rostro+estilizado"
    },
    {
        "nombre": "Rostro casi humano",
        "realismo": 7,
        "url": "https://placehold.co/500x350?text=Casi+humano"
    },
    {
        "nombre": "Rostro realista",
        "realismo": 10,
        "url": "https://placehold.co/500x350?text=Rostro+realista"
    }
]

resultados = []

for i, imagen in enumerate(imagenes):
    st.subheader(imagen["nombre"])
    st.image(imagen["url"], width=350)

    inquietud = st.slider(
        f"¿Qué tan inquietante te parece? ({imagen['nombre']})",
        min_value=0,
        max_value=10,
        value=0,
        key=f"inquietud_{i}"
    )

    resultados.append({
        "Imagen": imagen["nombre"],
        "Semejanza humana": imagen["realismo"],
        "Inquietud": inquietud
    })

st.divider()

st.header("2. Cuestionario")

sensacion = st.radio(
    "¿Qué sensación predominó al observar las imágenes?",
    [
        "Tranquilidad",
        "Curiosidad",
        "Indiferencia",
        "Incomodidad",
        "Inquietud"
    ]
)

caracteristica = st.selectbox(
    "¿Qué característica influyó más en tu percepción?",
    [
        "Los ojos",
        "La expresión facial",
        "La textura de la piel",
        "Las proporciones del rostro",
        "El aspecto general"
    ]
)

comentario = st.text_area(
    "¿Quieres explicar alguna de tus respuestas? (Opcional)"
)

st.divider()

st.header("3. Tu gráfica del Valle Inquietante")

if st.button("Generar mi gráfica"):
    df = pd.DataFrame(resultados)

    df = df.sort_values("Semejanza humana")

    fig, ax = plt.subplots(figsize=(9, 5))

    ax.plot(
        df["Semejanza humana"],
        df["Inquietud"],
        marker="o"
    )

    ax.set_title("Semejanza humana e inquietud percibida")
    ax.set_xlabel("Semejanza con la apariencia humana")
    ax.set_ylabel("Inquietud percibida (0-10)")
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.grid(True)

    st.pyplot(fig)

    st.subheader("Tus respuestas")
    st.dataframe(df, use_container_width=True)

    st.write("Sensación predominante:", sensacion)
    st.write("Característica más influyente:", caracteristica)

    if comentario:
        st.write("Comentario:", comentario)

    csv = df.to_csv(index=False).encode("utf-8")

    st.download_button(
        "Descargar mis puntuaciones en CSV",
        data=csv,
        file_name="resultados_valle_inquietante.csv",
        mime="text/csv"
    )
