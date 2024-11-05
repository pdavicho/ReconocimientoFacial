import streamlit as st

st.set_page_config(page_title='Reconocimiento Facial', page_icon=':👤:', layout='wide')

#st.set_page_config(page_title='Reconocimiento-Facial', layout='wide')
st.header('Sistema de Asistencia usando Reconocimiento Facial')


with st.spinner('Cargando Modelo y conectandose a la BD...'):
    import face_rec

st.success('Sistema Listo')
#st.success('Model loaded sucessfully')
#st.success('Redis db sucessfully connected')