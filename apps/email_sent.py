import email
from email import message
from email.quoprimime import body_check
from multiprocessing import connection
from sre_parse import SPECIAL_CHARS
from click import password_option
import streamlit as st
import smtplib  as s
import os
from PIL import Image
from win32com.client import Dispatch

def speak(str):
    speak = Dispatch(("SAPI.SpVoice"))
    speak.Speak(str)


def app():
    st.title("Email Sender Web Application")
    st.write("Build with Streamlit and Python")
    activites = ["Send Email", "Send Email with Attachment", "Send Email with Image"]
    if activites == "Send Email":
        email_sender = st.text_input("Enter User Email -")
        password = st.text_input("Enter User Password -", type= "password")
        email_receiver = st.text_input("Enter Receiver Email -")
        subject = st.text_input("your subject -")
        body = st.text_area("your body -")
        if st.button("send email"):
            try:
                connection = s.SMTP('SMTP.gmail.com', 587)
                connection.starttls()
                connection.login(email_sender, password)
                message = "Subject:{}\n\n{}".format(subject, body)
                connection.sendmail(email_sender, email_receiver)
                connection.quit()
                st.success("Email Send Successfully")
                speak("Email Send Successfully")
            except Exception as e:
                if email_sender == "":
                    st.error("Please Fill User Email Field")
                    speak("Please Fill User Email Field")
                elif password == "":
                    st.error("Please Fill Password Field")
                    speak("Please Fill Password Field")                  
                elif email_receiver == "":
                    st.error("Please Fill Receiver Email Field")
                    speak("Please Fill Receiver Email Field")      
                else:
                    a = os.system("ping -n 1 google.com")
                    if a == 1:
                        st.error("Please connect your internet")                                 
                        speak("Please connect your internet")
                    else:
                        st.error("Wrong Email or Password!")
                        speak("Wrong Email or Password!")