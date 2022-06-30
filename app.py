import streamlit as st
from multiapp import MultiApp
from apps import home, surat_keputusan, surat_tugas, petikan_keputusan,invoice, email_python, email_yag  # import your app modules here

st.set_page_config(layout="centered", page_icon="img/hangtuah_icon.jpg", page_title="Surat Keputusan Generator")

app = MultiApp()

# Add all your application here
app.add_app("Home", home.app)
app.add_app("Surat Keputusan", surat_keputusan.app)
app.add_app("Surat Tugas", surat_tugas.app)
app.add_app("Petikan Keputusan", petikan_keputusan.app)
app.add_app("Invoice", invoice.app)
app.add_app("email_python", email_python.app)
app.add_app("email_yag", email_yag.app)

# The main app
app.run()
