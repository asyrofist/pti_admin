import streamlit as st
from multiapp import MultiApp
<<<<<<< HEAD
from apps import home, surat_keputusan, surat_tugas, petikan_keputusan,invoice, email_python, email_yag  # import your app modules here
from streamlit_option_menu import option_menu
=======
from apps import home, surat_keputusan, surat_tugas, petikan_keputusan,invoice # import your app modules here
>>>>>>> 329ea97260369597554fde34c6bdee99eff35f21


st.set_page_config(layout="centered", page_icon="img/hangtuah_icon.jpg", page_title="Surat Keputusan Generator")

app = MultiApp()

# Add all your application here
app.add_app("Home", home.app)
app.add_app("Surat Keputusan", surat_keputusan.app)
app.add_app("Surat Tugas", surat_tugas.app)
app.add_app("Petikan Keputusan", petikan_keputusan.app)
app.add_app("Invoice", invoice.app)
<<<<<<< HEAD
app.add_app("email_python", email_python.app)
app.add_app("email_yag", email_yag.app)
=======
>>>>>>> 329ea97260369597554fde34c6bdee99eff35f21

# The main app
app.run()
