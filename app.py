import streamlit as st
from multiapp import MultiApp
from apps import home, surat_keputusan, surat_tugas, petikan_keputusan,invoice  # import your app modules here

st.set_page_config(layout="centered", page_icon="img/hangtuah_icon.jpg", page_title="Surat Keputusan Generator")

app = MultiApp()

# Add all your application here
app.add_app("Home", home.app)
app.add_app("Surat Keputusan", surat_keputusan.app)
app.add_app("Surat Tugas", surat_tugas.app)
app.add_app("Petikan Keputusan", petikan_keputusan.app)
app.add_app("Invoice", invoice.app)

# The main app
app.run()