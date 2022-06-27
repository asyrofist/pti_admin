import streamlit as st
from multiapp import MultiApp
from apps import home, surat_keputusan # import your app modules here

st.set_page_config(layout="centered", page_icon="img/hangtuah_icon.jpg", page_title="Surat Keputusan Generator")

app = MultiApp()

# Add all your application here
app.add_app("Home", home.app)
app.add_app("Surat_Keputusan", surat_keputusan.app)

# The main app
app.run()