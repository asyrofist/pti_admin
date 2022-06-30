import email, smtplib, ssl, os, streamlit as st
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import qrcode, pdfkit, qrcode, streamlit as st, base64, io
from enum import auto
from logging import PlaceHolder, disable
from jinja2 import Environment, PackageLoader, select_autoescape, FileSystemLoader
from datetime import date, datetime
from streamlit.components.v1 import iframe

def app():
    # st.set_page_config(layout="centered", page_icon="img/hangtuah_icon.jpg", page_title="Surat Keputusan Generator")
    st.title("Surat Tugas PDF Generator")

    st.write(
        "Aplikasi ini digunakan untuk membuat dokumen dalam bentuk pdf"
    )

    left, right = st.columns(2)

    right.write("Here's the template we'll be using:")
    right.image("img/surat_tugas.png", width=300)

    env = Environment(loader=FileSystemLoader("."), autoescape=select_autoescape())
    template = env.get_template("apps/surat_tugas.html")


    left.write("Fill in the data:")
    form = left.form("template_form")
    nomor_surat_keputusan = form.text_input("masukkan nomor surat keputusan anda", placeholder= "S.Gas/1796/UHT.A0/VIII/2021")
    pertimbangan = form.text_area("masukkan pertimbangan surat tugas anda", placeholder= "Bahwa dipandang perlu mengeluarkan Surat Tugas dalam Rangka Dinas").splitlines()
    dasar = form.text_area("masukkan dasar pemberian surat tugas", placeholder= "1. Kepentingan dinas lembaga").splitlines()
    kepada = form.text_area("masukkan kepada surat tugas diberikan", placeholder= "Nama-nama dalam lampiran Surat Tugas").splitlines()
    untuk = form.text_area("masukkan peruntukan surat tugas", placeholder= "1. melaksanakan tugas disamping tugas dan tanggung jawab yang ada ditunjuk dalam kepanitian kegiaan vaksinasi massal di lingungan sivitas akademika universitas hang tuah dan masyarakat sekitar kampus UHT, sesuai daftar dalam lampiran surat. 2 Pelaksanaan kegiatan terhitung sejak surat dikeluarkan hingga selesai pelaksanaan, 3. melaksanakan tugas ini dengan seksama dan penuh rasa tanggung jawab.").splitlines()
    tempat_penetapan = form.text_input("masukkan tempat penetapan surat tugas", placeholder= "Surabaya")
    tanggal_penetapan = form.date_input("Tanggal Penetapan Surat Tugas", datetime.now())
    status_pejabat = form.selectbox(
        "Pilih status pejabat surat tugas tersebut ditentukan",
        ["Rektor", "Wakil Rektor 1", "Wakil Rektor 2", 'Wakil Rektor 3', 
        'Dekan FVP', 'Dekan FTIK', 'Dekan FISIP', 'Dekan FH', 'Dekan F.PSI',
        'Dekan FK', 'Dekan FKG',
        'Ka. Lembaga Penjaminan Mutu', 'Ka. Lembaga Pengembangan Pendidikan dan Pengajaran',
        'Ka. Biro Perencanaan dan Pengembangan', 'Ka. Biro Kepegawaian', 
        'Ka. Biro Administrasi Keuangan', 'Ka. Biro Rumah Tanggan', 'Ka. UPT KS & Humas',
        'Ka. Perpustakaan', 'Ka. Pusat Teknologi Informasi'],
        index=10,
    )
    pejabat_yang_menandatangani = form.selectbox(
        "Pilih Pejabat yang menandatangi",
        ["Dr. RA. Nora Leiyana, drg., M.H.,Kes., FICD", "Soenaryati, S.Sos", 
        'Hadi Soesilo, dr., Sp.M., Sp.KL', 'Dr. Ir. Ninis Trisyani, M.P', 
        'Prof. Dr. David  S. Perdanakusuma, dr., Sp.BP-RE(K)',
        'Dr. Ir. Sudirman, S.IP., S.E., M.AP., M.H', 
        'Dr. Dian Mulawarmanti, drg., MS.', 'Lita Agustian, drg., M.H. Kes.',
        'Bambang Sucahyo, drg. Sp. Ort.', 'Prof. Dr. Ir. Suparno, M.M., CIQaR'],
        index=0,
    )
    tembusan = form.text_area("masukkan tembusan surat tugas tersebut ditujukan", placeholder= "1. Ketua Pengurus Yayasan Nala <br> 2. Distribusi A,B,C").splitlines()
    agree = form.checkbox('saya setuju dengan segala kondisi data yang saya isi')
    submit = form.form_submit_button("Generate PDF")
    if agree:
        img_qrcode = qrcode.make(
            { 
                "nomor_surat_keputusan": nomor_surat_keputusan,
                "pertimbangan": pertimbangan,
                "dasar": dasar,
                "kepada": kepada,
                "untuk": untuk,
                "tempat_penetapan": tempat_penetapan,
                "tanggal_penetapan": tanggal_penetapan,
                "status_pejabat": status_pejabat,
                "pejabat_yang_menandatangani": pejabat_yang_menandatangani,
                "tembusan": tembusan,
            }
        )

        if submit:
            html = template.render(
                nomor_surat_keputusan= nomor_surat_keputusan,
                pertimbangan= pertimbangan,
                dasar= dasar,
                kepada= kepada,
                untuk= untuk,
                tempat_penetapan= tempat_penetapan,
                tanggal_penetapan= tanggal_penetapan,
                status_pejabat= status_pejabat,
                pejabat_yang_menandatangani= pejabat_yang_menandatangani,
                tembusan= tembusan,
                img_qrcode= img_qrcode,
                date=date.today().strftime("%B %d, %Y"),
            )

            pdf = pdfkit.from_string(html, False)
            st.balloons()

            right.success("🎉 Surat Keputusan anda sudah diterbitkan!")
            right.download_button(
                "⬇️ Download PDF",
                data=pdf,
                file_name="{}.pdf".format(nomor_surat_keputusan),
                mime="application/octet-stream",
            )

            form2 = right.form("email_form")
            subject = form2.text_input("An email with attachment from Python", placeholder="Enter Subject", key="subject")
            body = form2.text_area("This is an email with attachment sent from Python", placeholder="Enter Body", key="body")
            receiver_email = form2.text_input("masukkan email pengirim", placeholder="your@gmail.com", key="receiver_email")
            sender_email = "asyrofi@hangtuah.ac.id"
            password = "xrlqddxjncjyvjhb"
            filename = pdf  # In same directory as script
            submit_send_email = form2.form_submit_button("Send Email")
            if submit_send_email:
                try:
                    message = MIMEMultipart() # Create a multipart message and set headers
                    message["From"] = sender_email
                    message["To"] = receiver_email
                    message["Subject"] = subject
                    message["Bcc"] = receiver_email  # Recommended for mass emails
                    message.attach(MIMEText(body, "plain")) # Add body to email
                    with open(filename, "rb") as attachment: # Open PDF file in binary mode            
                        part = MIMEBase("application", "octet-stream") # Add file as application/octet-stream
                        part.set_payload(attachment.read()) # Email client can usually download this automatically as attachment
                    encoders.encode_base64(part) # Encode file in ASCII characters to send by email
                    part.add_header( # Add header as key/value pair to attachment part
                        "Content-Disposition",
                        f"attachment; filename= {filename}",
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


