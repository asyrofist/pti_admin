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
    untuk = form.text_area("masukkan peruntukan surat tugas", placeholder= "1. melaksanakan tugas disamping tugas dan tanggung jawab yang ada ditunjuk dalam kepanitian kegiaan vaksinasi massal di lingungan sivitas akademika universitas hang tuah dan masyarakat sekitar kampus UHT, sesuai daftar dalam lampiran surat. 2 Pelaksanaan kegiatan terhitung sejak surat dikeluarkan hingga selesai pelaksanaan, 3. melaksanakan tugas ini dengan seksama dan penuh rasa tanggung jawab.")
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
