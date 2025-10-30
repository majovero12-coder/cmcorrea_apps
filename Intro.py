import math
import streamlit as st

# --- Configuración de la página ---
st.set_page_config(page_title="Portafolio IA - María José Velásquez", layout="wide")

# --- Estilos rosados (solo colores y tipografía) ---
st.markdown(
    """
    <style>
    [data-testid="stAppViewContainer"] {
        background-color: #ffe6f2;
        background-image: linear-gradient(135deg, #ffe6f2 0%, #ffd1e8 100%);
    }
    [data-testid="stSidebar"] {
        background-color: #ffd6e7;
    }
    h1, h2, h3 {
        color: #c2185b;
    }
    .card-title {
        color: #c2185b;
        margin: 0;
        padding: 0;
    }
    .card {
        background-color: #ffffff;
        border-radius: 10px;
        padding: 12px;
        box-shadow: 0px 2px 6px rgba(0,0,0,0.08);
        margin-bottom: 12px;
    }
    a {
        color: #ad1457 !important;
        font-weight: 600;
        text-decoration: none;
    }
    a:hover {
        text-decoration: underline;
        color: #880e4f !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# --- Título y sidebar ---
st.title("💗 Aplicaciones de Inteligencia Artificial")
with st.sidebar:
    st.subheader("Aplicaciones con Inteligencia Artificial")
    st.write(
        "La inteligencia artificial permite mejorar la toma de decisiones con el uso de datos, "
        "automatizar tareas rutinarias y proporcionar análisis avanzados en tiempo real."
    )

# --- Enlace general ---
url_ia = "https://sites.google.com/view/aplicacionesdeia/inicio"
st.subheader("En el siguiente enlace puedes encontrar páginas y ejercicios prácticos")
st.write(f"🔗 [Abrir enlace general]({url_ia})")

st.markdown("---")

# --- Lista EXACTA de proyectos (los mismos del principio) ---
projects = [
    ("Analisis de texto", "https://dnmzepv2h4xmw6yxwzvcrr.streamlit.app"),
    ("Chat PDF", "https://chatpdf-gwuf3xshqmb2cb4bjgkivd.streamlit.app"),
    ("Ctrl_voice", "https://ctrlvoice-jjdnyj4h7uqjkzdzjndskm.streamlit.app"),
    ("Drawrecog", "https://drawrecog-ftmxxecetrks53qqf7ep5x.streamlit.app"),
    ("Hand_W", "https://mtubb8lilvvh68zsisjjhy.streamlit.app"),
    ("Imm1", "https://aetvf8ckuvwtmhegftsne8.streamlit.app"),
    ("Intro", "https://gnj4sr3tzwfb2tuwcru6in.streamlit.app"),
    ("OCR", "https://4ohjzp2brxgz8xgirrhxz2.streamlit.app"),
    ("OCR-Audio", "https://ocr-audio-4b6rtzrvvqybdrbkgxjvge.streamlit.app"),
    ("Recep_MQTT", "https://recepmqtt-bkharxblreeetctedowmsr.streamlit.app"),
    ("Send_CMqtt", "https://sendcmqtt-cvkmcjjdmz6lsgjgbuawix.streamlit.app"),
    ("TF_IDF", "https://ckv67faaexydbykhj23gqb.streamlit.app"),
    ("TM", "https://g8ww5stpf5eekifywa5mbt.streamlit.app"),
    ("Traductor", "https://traductor-bnujsivx7ixvv2kbaphv7b.streamlit.app"),
    ("Tx2_Analisis", "https://7ibuhcfwsvaamifxn984vx.streamlit.app"),
    ("Vision_App", "https://visionapp-npw2s56o4vuqtnvrxrxv5n.streamlit.app"),
    ("Yolov5", "https://yolov5-whntcxc7whqvtxa57gjal5.streamlit.app"),
]

# --- Número de columnas que quieres ver ---
ncols = 3

# --- Calcular distribución casi pareja de proyectos por columna ---
per_col = math.ceil(len(projects) / ncols)
cols_data = [projects[i * per_col:(i + 1) * per_col] for i in range(ncols)]

# --- Crear columnas y renderizar tarjetas (equilibradas) ---
cols = st.columns(ncols)
for col, col_projects in zip(cols, cols_data):
    with col:
        for name, link in col_projects:
            st.markdown(
                f"""
                <div class="card">
                    <h4 class="card-title">{name}</h4>
                    <div><a href="{link}" target="_blank">🔗 Abrir aplicación</a></div>
                </div>
                """,
                unsafe_allow_html=True,
            )

# --- Pie de página ---
st.markdown("---")
st.caption("💗 Desarrollado por María José Velásquez — Portafolio de aplicaciones con IA 💻")

