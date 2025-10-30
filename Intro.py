import streamlit as st
from PIL import Image
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
 image = Image.open('txt_to_audio2.png')
 st.image(image, width=190)
 url = "https://dnmzepv2h4xmw6yxwzvcrr.streamlit.app"
 st.write(f" [Enlace]({url})")

 st.subheader("Chat PDF")
 image = Image.open('txt_to_audio.png')
 st.image(image, width=200)
 url = "https://chatpdf-gwuf3xshqmb2cb4bjgkivd.streamlit.app"
 st.write(f" [Enlace]({url})")

 st.subheader("Ctrl_voice")
 image = Image.open('OIG5.jpg')
 st.image(image, width=200)
 url = "https://ctrlvoice-jjdnyj4h7uqjkzdzjndskm.streamlit.app"
 st.write(f" [Enlace]({url})")

with col2: 
 st.subheader("drawrecog")
 image = Image.open('OIG8.jpg')
 st.image(image, width=200)
 url = "https://drawrecog-ftmxxecetrks53qqf7ep5x.streamlit.app/"
 st.write(f" [Enlace]({url})")

 st.subheader("hand_w")
 image = Image.open('data_analisis.png')
 st.image(image, width=190)
 url = "https://mtubb8lilvvh68zsisjjhy.streamlit.app"
 st.write(f" [Enlace]({url})")

 st.subheader("imm1")
 image = Image.open('OIG3.jpg')
 st.image(image, width=200)
 url = "https://aetvf8ckuvwtmhegftsne8.streamlit.app"
 st.write(f" [Enlace]({url})")


with col3: 
 st.subheader("intro")
 image = Image.open('Chat_pdf.png')
 st.image(image, width=190)
 url = "https://gnj4sr3tzwfb2tuwcru6in.streamlit.app"
 st.write(f" [Enlace]({url})")

 st.subheader("ocr ")
 image = Image.open('OIG4.jpg')
 st.image(image, width=200)
 url = "https://4ohjzp2brxgz8xgirrhxz2.streamlit.app"
 st.write(f" [Enlace]({url})")

 st.subheader("ocr-audio ")
 image = Image.open('OIG6.jpg')
 st.image(image, width=200)
 url = "https://ocr-audio-4b6rtzrvvqybdrbkgxjvge.streamlit.app"
 st.write(f" [Enlace]({url})")

 st.subheader("recep_mqtt ")
 image = Image.open('OIG6.jpg')
 st.image(image, width=200)
 url = "https://recepmqtt-bkharxblreeetctedowmsr.streamlit.app"
 st.write(f" [Enlace]({url})")
  
 st.subheader("send_cmqtt  ")
 image = Image.open('OIG6.jpg')
 st.image(image, width=200)
 url = "https://sendcmqtt-cvkmcjjdmz6lsgjgbuawix.streamlit.app"
 st.write(f" [Enlace]({url})")

 st.subheader("tf_idf ")
 image = Image.open('OIG6.jpg')
 st.image(image, width=200)
 url = "https://ckv67faaexydbykhj23gqb.streamlit.app"
 st.write(f" [Enlace]({url})")

 st.subheader("tm ")
 image = Image.open('OIG6.jpg')
 st.image(image, width=200)
 url = "https://g8ww5stpf5eekifywa5mbt.streamlit.app"
 st.write(f" [Enlace]({url})")

st.subheader("traductor ")
 image = Image.open('OIG6.jpg')
 st.image(image, width=200)
 url = "https://traductor-bnujsivx7ixvv2kbaphv7b.streamlit.app"
 st.write(f" [Enlace]({url})")

st.subheader("tx2_analisis ")
 image = Image.open('OIG6.jpg')
 st.image(image, width=200)
 url = "https://7ibuhcfwsvaamifxn984vx.streamlit.app"
 st.write(f" [Enlace]({url})")

st.subheader("vision_app")
 image = Image.open('OIG6.jpg')
 st.image(image, width=200)
 url = "https://visionapp-npw2s56o4vuqtnvrxrxv5n.streamlit.app"
 st.write(f" [Enlace]({url})")

st.subheader("yolov5 ")
 image = Image.open('OIG6.jpg')
 st.image(image, width=200)
 url = "https://yolov5-whntcxc7whqvtxa57gjal5.streamlit.app"
 st.write(f" [Enlace]({url})")

