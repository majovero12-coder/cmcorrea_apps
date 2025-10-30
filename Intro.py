import streamlit as st
from PIL import Image
# 💗 --- ESTILO PERSONALIZADO (fondo rosado y sidebar) ---
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
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

st.title("Aplicaciones de Inteligencia Artificial.")

with st.sidebar:
  st.subheader("Aplicaciones con Inteligencia Artificial.")
  parrafo = (
    "La inteligencia artificial permite mejorar la toma de decisiones con el uso de datos, "
    "automatizar tareas rutinarias y proporcionar análisis avanzados en tiempo real, lo que "
    "resulta en una mayor eficiencia y precisión en diversos campos."
  )
  st.write(parrafo)

url_ia="https://sites.google.com/view/aplicacionesdeia/inicio"
st.subheader("En el siguiente enlace puedes encontrar páginas y ejercicios prácticos")
st.write(f"Enlace para páginas y ejercicios: [Enlace]({url_ia})")
col1, col2, col3 = st.columns(3)

with col1:
 
 st.subheader("Analisis de texto")
 url = "https://dnmzepv2h4xmw6yxwzvcrr.streamlit.app"
 st.write(f" [Enlace]({url})")

 st.subheader("Chat PDF")
 url = "https://chatpdf-gwuf3xshqmb2cb4bjgkivd.streamlit.app"
 st.write(f" [Enlace]({url})")

 st.subheader("Ctrl_voice")
 url = "https://ctrlvoice-jjdnyj4h7uqjkzdzjndskm.streamlit.app"
 st.write(f" [Enlace]({url})")

with col2: 
 st.subheader("drawrecog")
 url = "https://drawrecog-ftmxxecetrks53qqf7ep5x.streamlit.app/"
 st.write(f" [Enlace]({url})")

 st.subheader("hand_w")
 url = "https://mtubb8lilvvh68zsisjjhy.streamlit.app"
 st.write(f" [Enlace]({url})")

 st.subheader("imm1")
 url = "https://aetvf8ckuvwtmhegftsne8.streamlit.app"
 st.write(f" [Enlace]({url})")


with col3: 
 st.subheader("intro")
 url = "https://gnj4sr3tzwfb2tuwcru6in.streamlit.app"
 st.write(f" [Enlace]({url})")

 st.subheader("ocr ")
 url = "https://4ohjzp2brxgz8xgirrhxz2.streamlit.app"
 st.write(f" [Enlace]({url})")

 st.subheader("ocr-audio ")
 url = "https://ocr-audio-4b6rtzrvvqybdrbkgxjvge.streamlit.app"
 st.write(f" [Enlace]({url})")

 st.subheader("recep_mqtt ")
 url = "https://recepmqtt-bkharxblreeetctedowmsr.streamlit.app"
 st.write(f" [Enlace]({url})")
  
 st.subheader("send_cmqtt  ")
 url = "https://sendcmqtt-cvkmcjjdmz6lsgjgbuawix.streamlit.app"
 st.write(f" [Enlace]({url})")

 st.subheader("tf_idf ")
 url = "https://ckv67faaexydbykhj23gqb.streamlit.app"
 st.write(f" [Enlace]({url})")

 st.subheader("tm ")
 url = "https://g8ww5stpf5eekifywa5mbt.streamlit.app"
 st.write(f" [Enlace]({url})")
    
st.subheader("Traductor")
url = "https://traductor-bnujsivx7ixvv2kbaphv7b.streamlit.app"
st.write(f"[Abrir]({url})")

st.subheader("Tx2_Analisis")
url = "https://7ibuhcfwsvaamifxn984vx.streamlit.app"
st.write(f"[Abrir]({url})")

st.subheader("Vision_app")
url = "https://visionapp-npw2s56o4vuqtnvrxrxv5n.streamlit.app"
st.write(f"[Abrir]({url})")

st.subheader("Yolov5")
url = "https://yolov5-whntcxc7whqvtxa57gjal5.streamlit.app"
st.write(f"[Abrir]({url})")

st.markdown("---")
st.caption("💗 Desarrollado por María José Velásquez — Portafolio de aplicaciones con IA 💻")


st.subheader("yolov5 ")
url = "https://yolov5-whntcxc7whqvtxa57gjal5.streamlit.app"
 st.write(f" [Enlace]({url})")

