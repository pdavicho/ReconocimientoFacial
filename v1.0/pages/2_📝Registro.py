import streamlit as st
from Inicio import face_rec
import cv2
import numpy as np
from streamlit_webrtc import webrtc_streamer
import av

#st.set_page_config(page_title='Registro', page_icon=':📝:', layout='wide')
#st.set_page_config(page_title='Registration Form')
st.subheader('📝 - Registrar Usuario')

##Init Registration Form
registration_form = face_rec.RegistrationForm()

#Step1: Collect Person name and role
#Form
person_name = st.text_input(label='Nombre', placeholder='Nombre y Apellido')
role = st.selectbox(label='Seleccionar Cargo', options=('Académico', 'Administrativo', 'Servicios'))

st.divider()
st.markdown('Iniciar cámara y registrar al menos 200 ejemplos')


#Step2: Collect facial embedding of that person
def video_callback_func(frame):
    img = frame.to_ndarray(format='bgr24')
    reg_img, embedding = registration_form.get_embeddings(img)
    #Two Steps Process
    #1st step save data into local computer txt
    if embedding is not None:
        with open('face_embedding.txt', mode='ab') as f:
            np.savetxt(f, embedding)



    return av.VideoFrame.from_ndarray(reg_img, format='bgr24')

webrtc_streamer(key='registration', video_frame_callback=video_callback_func,
                rtc_configuration={
        "iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]
    }
                )


#Step3: Save the data in redis database
st.markdown('Presionar Guardar, para almacenar los datos.')

if st.button('Guardar'):
    #return_val = registration_form.save_data_in_redis_db(person_name, role)
    #if return_val == True:
        st.success(f'{person_name} registrado exitosamente')
   # elif return_val == 'name_false':
   #     st.error('Ingrese el nombre: no dejar vacio o con espacios.')

    #elif return_val == 'file_false':
     #   st.error('Por favor refresque la página y ejecute nuevamente.')
