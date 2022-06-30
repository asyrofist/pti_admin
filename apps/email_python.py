import smtplib, ssl, streamlit as st, base64
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def show_pdf(file_path):
    with open(file_path,"rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="800" height="800" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)

def app():
    subject = st.text_input("An email with attachment from Python", placeholder="Enter Subject", key="subject")
    body = st.text_area("This is an email with attachment sent from Python", placeholder="Enter Body", key="body")
    receiver_email = st.text_input("masukkan email pengirim", placeholder="your@gmail.com", key="receiver_email")
    sender_email = "asyrofi@hangtuah.ac.id"
    password = "xrlqddxjncjyvjhb"
    # datafile = "asyrofi.pdf"  # In same directory as script
    # show_pdf(datafile)

    uploaded_file = st.file_uploader("Choose a document: ", type="pdf")
    show_file = st.empty()
    if uploaded_file is not None:
        show_file.info("File received!")
        # for page_layout in extract_pages(uploaded_file):
        #     for element in page_layout:
        #         pdf_display = f'<iframe src="data:application/pdf;base64,{element}" width="800" height="800" type="application/pdf"></iframe>'
        #         st.markdown(pdf_display, unsafe_allow_html=True)

        
        if st.button("Send Email"):
            try:
                message = MIMEMultipart() # Create a multipart message and set headers
                message["From"] = sender_email
                message["To"] = receiver_email
                message["Subject"] = subject
                message["Bcc"] = receiver_email  # Recommended for mass emails
                message.attach(MIMEText(body, "plain")) # Add body to email
                with open(uploaded_file, "rb") as attachment: # Open PDF file in binary mode            
                    part = MIMEBase("application", "octet-stream") # Add file as application/octet-stream
                    part.set_payload(attachment.read()) # Email client can usually download this automatically as attachment
                encoders.encode_base64(part) # Encode file in ASCII characters to send by email
                part.add_header( # Add header as key/value pair to attachment part
                    "Content-Disposition",
                    f"attachment; filename= {uploaded_file}",
                )
                message.attach(part) # Add attachment to message and convert message to string
                text = message.as_string()
                context = ssl.create_default_context() # Log in to server using secure context and send email
                with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                    server.login(sender_email, password)
                    server.sendmail(sender_email, receiver_email, text)
                    st.success("Email sent!")

            except Exception as e:
                if subject == "":
                    st.error("Please Fill Subject Field")
                elif password == "":
                    st.error("Please Fill Password Field")
                elif receiver_email == "":
                    st.error("Please Fill Receiver Email Field")