import streamlit as st

# --- Configuración de la página ---
st.set_page_config(page_title="Portafolio María José", layout="wide")

# --- Fondo rosado con el mismo estilo del anterior ---
st.markdown(
    """
    <style>
    body {
        background-color: #ffe6f2;
    }
    .block-container {
        padding-top: 1rem;
        padding-bottom: 1rem;
    }
    h1, h2, h3 {
        color: #2b2b2b;
    }
    a {
        color: #b30059;
        font-weight: bold;
        text-decoration: none;
    }
    a:hover {
        text-decoration: underline;
    }
    .project-card {
        background-color: #ffd6e8;
        padding: 1rem;
        border-radius: 10px;
        text-align: center;
        box-shadow: 0px 2px 6px rgba(0,0,0,0.1);
        margin-bottom: 1rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- Título principal ---
st.title("🌸 Portafolio de Proyectos - María José Velásquez")

# --- Lista de proyectos ---
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

# --- Mostrar en cuadrícula ajustada de 3 columnas ---
cols = st.columns(3)

for i, project in enumerate(projects):
    col = cols[i % 3]
    with col:
        st.markdown(
            f"""
            <div class="project-card">
                <h3>{project['name']}</h3>
                <a href="{project['url']}" target="_blank">🔗 Enlace</a>
            </div>
            """,
            unsafe_allow_html=True
        )

# --- Pie de página ---
st.markdown("---")
st.markdown(
    "<p style='text-align:center; color:#444;'>✨ Portafolio desarrollado en Streamlit ✨</p>",
    unsafe_allow_html=True
)
