import streamlit as st

# --- Configuración de la página ---
st.set_page_config(page_title="Portafolio María José", layout="wide")

# --- Fondo rosado con estilo limpio ---
st.markdown(
    """
    <style>
    body {
        background-color: #ffd6e8;
    }
    .block-container {
        padding-top: 2rem;
    }
    h1, h2, h3 {
        color: #3b3b3b;
        text-align: center;
    }
    a {
        color: #b30059;
        font-weight: bold;
        text-decoration: none;
    }
    a:hover {
        text-decoration: underline;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- Título principal ---
st.title("🌸 Portafolio de Proyectos - María José Velásquez")

# --- Organización en cuadrícula ---
projects = [
    {"name": "Chat PDF", "url": "https://chatpdf-bq2plpj6bfk7aqxej7u5pt.streamlit.app"},
    {"name": "Hand_W", "url": "https://handw-6grwjkqfwizbsymcn2e4v4.streamlit.app"},
    {"name": "OCR", "url": "https://ocr-rgzajcbk2kbsxjeztu2rxn.streamlit.app"},
    {"name": "Ctrl_voice", "url": "https://ctrlvoice-3bq6eeg7pjij6zrw6tbsko.streamlit.app"},
    {"name": "Imm1", "url": "https://imm1-4sgv6qqb7mms7qfkpz6y4b.streamlit.app"},
    {"name": "OCR-Audio", "url": "https://ocr-audio-uf7ynfyx6r8nd2bx2zsgpd.streamlit.app"},
    {"name": "Recep_MQTT", "url": "https://recep-mqtt-pn7tzgyavpvd5tk4q2h6wb.streamlit.app"},
    {"name": "Send_CMqtt", "url": "https://send-cmqtt-8hrjcv7bjrqxh4kggx57zh.streamlit.app"},
    {"name": "TF_IDF", "url": "https://tfidf-qfc4xxs7cdcb7ptkywn7gk.streamlit.app"},
    {"name": "TM", "url": "https://tm-wxyhkcp7fgwks2k7rynxbg.streamlit.app"},
    {"name": "Traductor", "url": "https://traductor-bnujsivx7ixvv2kbaphv7b.streamlit.app"}
]

# --- Mostrar proyectos en una cuadrícula de 3 columnas ---
cols = st.columns(3)

for i, project in enumerate(projects):
    with cols[i % 3]:
        st.subheader(project["name"])
        st.markdown(f"[🔗 Enlace]({project['url']})")

# --- Mensaje final ---
st.markdown("---")
st.markdown(
    "<p style='text-align:center; color:#555;'>✨ Portafolio desarrollado en Streamlit ✨</p>",
    unsafe_allow_html=True
)
