import yagmail, streamlit as st
from pdfminer.high_level import extract_pages


def app():
    subject_to = st.text_input("An email with attachment from Python", placeholder="Enter Subject", key="subject_to")
    body = st.text_area("This is an email with attachment sent from Python", placeholder="Enter Body", key="body")
    receiver = st.text_input("masukkan email pengirim", placeholder="your@gmail.com", key="receiver")
    # filename = "asyrofi.pdf"

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
            yag = yagmail.SMTP("asyrofi@hangutah.ac.id", "xrlqddxjncjyvjhb")
            yag.send(
                to= receiver,
                subject= subject_to,
                contents= body, 
                attachments= uploaded_file,

            )
        except Exception as e:
            if subject_to == "":
                st.error("Please Fill Subject Field")
            elif body == "":
                st.error("Please Fill Body Field")
            elif receiver == "":
                st.error("Please Fill Receiver Email Field")

