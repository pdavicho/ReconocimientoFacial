import streamlit_authenticator as stauth
import streamlit as st

from time import sleep

st.subheader('📑 - Reporte')

st.write("Iniciar sesion...")

def iniciar_sesion():
    username = st.text_input("Usuario: ")
    password = st.text_input("Password: ", type="password")

    if st.button("Ingresar", type="primary"):
        if username == "test" and password == "test":
            st.session_state.logged_in = True
            st.success("Ingreso satisfactorio.")
            sleep(0.5)
            #st.switch_page("pages/3_📑Reporte.py")
        
        else:
            st.error("Incorrect username or password")