import streamlit as st

# 💗 --- ESTILO PERSONALIZADO ---
page_bg = """
<style>
[data-testid="stAppViewContainer"] {
    background-color: #ffe6f2;
    background-image: linear-gradient(135deg, #ffe6f2 0%, #ffd1e8 100%);
}
[data-testid="stHeader"] {
    background: rgba(255, 192, 203, 0.6);
}
[data-testid="stSidebar"] {
    background-color: #ffd6e7;
}
h1, h2, h3, h4, h5, h6 {
    color: #c2185b;
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
.grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 1.2rem;
    margin-top: 1.5rem;
}
.card {
    background: white;
    border-radius: 15px;
    padding: 1rem;
    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    text-align: center;
}
.card h3 {
    color: #c2185b;
    margin-bottom: 0.5rem;
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# --- Título principal ---
st.title("💗 Aplicaciones de Inteligencia Artificial")

# --- Sidebar ---
with st.sidebar:
    st.subheader("Aplicaciones con Inteligencia Artificial")
    st.write(
        "La inteligencia artificial permite mejorar la toma de decisiones con el uso de datos, "
        "automatizar tareas rutinarias y proporcionar análisis avanzados en tiempo real, lo que "
        "resulta en una mayor eficiencia y precisión en diversos campos."
    )

# --- Enlace general ---
url_ia = "https://sites.google.com/view/aplicacionesdeia/inicio"
st.subheader("En el siguiente enlace puedes encontrar páginas y ejercicios prácticos")
st.write(f"🔗 [Abrir enlace general]({url_ia})")

# --- Lista de proyectos ---
projects = [
    ("Analisis de texto", "https://dnmzepv2h4xmw6yxwzvcrr.streamlit.app"),
    ("Chat PDF", "https://chatpdf-gwuf3xshqmb2cb4bjgkivd.streamlit.app"),
    ("Ctrl_Voice", "https://ctrlvoice-jjdnyj4h7uqjkzdzjndskm.streamlit.app"),
    ("DrawRecog", "https://drawrecog-ftmxxecetrks53qqf7ep5x.streamlit.app"),
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
    ("Yolov5", "https://yolov5-whntcxc7whqvtxa57gjal5.streamlit.app")
]

# --- Cuadrícula sin vacío ---
html_grid = '<div class="grid">'
for name, link in projects:
    html_grid += f"""
    <div class="card">
        <h3>{name}</h3>
        <a href="{link}" target="_blank">Abrir aplicación 🚀</a>
    </div>
    """
html_grid += "</div>"
st.markdown(html_grid, unsafe_allow_html=True)

# --- Pie de página ---
st.markdown("---")
st.caption("💗 Desarrollado por María José Velásquez — Portafolio de aplicaciones con IA 💻")
