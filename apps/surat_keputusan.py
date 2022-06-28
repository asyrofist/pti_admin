from enum import auto
import qrcode, pdfkit, qrcode, streamlit as st
from logging import PlaceHolder, disable
from jinja2 import Environment, PackageLoader, select_autoescape, FileSystemLoader
from datetime import date, datetime
from streamlit.components.v1 import iframe
import base64
import io

def app():
    # st.set_page_config(layout="centered", page_icon="img/hangtuah_icon.jpg", page_title="Surat Keputusan Generator")
    st.title("Surat Keputusan PDF Generator")

    st.write(
        "Aplikasi ini digunakan untuk membuat dokumen dalam bentuk pdf"
    )

    left, right = st.columns(2)

    right.write("Here's the template we'll be using:")
    right.image("img/surat_keputusan.png", width=300)

    env = Environment(loader=FileSystemLoader("."), autoescape=select_autoescape())
    template = env.get_template("apps/surat_keputusan.html")


    left.write("Fill in the data:")
    form = left.form("template_form")
    dekan_fakultas = form.text_input("masukkan ditujukan ke dekan fakultas anda", placeholder= "DEKAN FAKULTAS KEDOKTERAN UNIVERSITAS HANG TUAH")
    nomor_surat_keputusan = form.text_input("masukkan nomor surat keputusan anda", placeholder= "Kep./058/UHT.B0.05/VIII/2021")
    perihal = form.text_input("masukkan perihal pemberian surat keputusan anda", placeholder= "PENGANGKATAN TENAGA PENGAJAR")
    semester = form.text_input("masukkan semester berapa pemberian surat keputusan", placeholder= "SEMESTER GASAL TAHUN AKADEMIK 2021/2022")
    menimbang = form.text_area("masukkan pertimbangan surat keputusan", placeholder= "Bahwa untuk pengangkutan tenaga pengajar pada Fakultas Kedokteran Gigi Universitas Hang Tuah").splitlines()
    mengingat = form.text_area("masukkan pengingat surat keputusan", placeholder= "1. Undang-Undang No. 20 Tahun 2003 tentang Sistem Pendidikan Nasional \n 2. Peraturan Pemerintah No. 60 Tahun 1999 Tentang Pendidikan Tinggi").splitlines()
    memperhatikan = form.text_area("masukkan perhatian surat keputusan ditujukan untuk siapa", placeholder= "Kalender Akademik Universitas Hang Tuah Akademik 2021/2022").splitlines()
    menetapkan = form.text_area("masukkan penetapan surat keputusan", placeholder= "1. Undang-Undang No. 20 Tahun 2003 Tentang Sistem Pendidikan Nasional \n 2. Peraturan Pemerintah No. 60 Tahun 1999 Tentang Pendidikan Tinggi").splitlines()
    tempat_penetapan = form.text_input("masukkan tempat penetapan surat keputusan", placeholder= "Surabaya")
    tanggal_penetapan = form.date_input("Tanggal Penetapan SK", datetime.now())
    status_pejabat = form.selectbox(
        "Pilih status pejabat surat keputusan tersebut ditentukan",
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
    tembusan = form.text_area("masukkan tembusan surat keputusan tersebut ditujukan", placeholder= "1. Ketua Pengurus Yayasan Nala <br> 2. Distribusi A,B,C").splitlines()
    agree = form.checkbox('saya setuju dengan segala kondisi data yang saya isi')
    submit = form.form_submit_button("Generate PDF")
    if agree:
        img_qrcode = qrcode.make(
            { 
                "dekan_fakultas": dekan_fakultas,
                "nomor_surat_keputusan": nomor_surat_keputusan,
                "perihal": perihal,
                "semester": semester,
                "menimbang": menimbang,
                "mengingat": mengingat,
                "memperhatikan": memperhatikan,
                "menetapkan": menetapkan,
                "tempat_penetapan": tempat_penetapan,
                "tanggal_penetapan": tanggal_penetapan,
                "status_pejabat": status_pejabat,
                "pejabat_yang_menandatangani": pejabat_yang_menandatangani,
                "tembusan": tembusan,
            }
        )

        if submit:
            html = template.render(
                dekan_fakultas= dekan_fakultas,
                nomor_surat_keputusan= nomor_surat_keputusan,
                perihal= perihal,
                semester= semester,
                menimbang= menimbang,
                mengingat= mengingat,
                memperhatikan= memperhatikan,
                menetapkan= menetapkan,
                tempat_penetapan= tempat_penetapan,
                tanggal_penetapan= tanggal_penetapan,
                status_pejabat= status_pejabat,
                pejabat_yang_menandatangani= pejabat_yang_menandatangani,
                tembusan= tembusan,
                img_qrcode= img_qrcode,
                date=date.today().strftime("%B %d, %Y"),
            )

            # pdf = pdfkit.from_file(html,False)
            pdf = pdfkit.from_string(html, False)
            st.balloons()

            right.success("🎉 Surat Keputusan anda sudah diterbitkan!")
            right.download_button(
                "⬇️ Download PDF",
                data=pdf,
                file_name="{}.pdf".format(nomor_surat_keputusan),
                mime="application/octet-stream",
            )
