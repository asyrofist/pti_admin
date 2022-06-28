import streamlit as st

def app():
    st.image("https://hangtuah.ac.id/wp-content/uploads/2017/06/logo-uht.png", width=300)
    st.markdown(
        """
        Berikut ini adalah tampilan utama dari program.
        Beberapa Fitur yang tersedia disini adalah seperti pembuatan:
        """)

    left1, right1 = st.columns(2)
    left1.header("Surat Keputusan")
    left1.markdown(
        """
        Dokumen ini adalah surat atau sebuah ketetapan yang dibuat
        oleh perusahaan atau badan tertentu di dalam bentuk tertulis 
        dan berdasarkan pada peraturan perundangan-undangan yang mengatur.
        dengan elemen yang digunakan yaitu:\n
        1. Dekan Fakultas
        2. Nomor Surat Keputusan
        3. Perihal
        4. Semester
        5. Menimbang
        6. Mengingat
        7. Memperhatikan
        8. Menetapkan
        9. Tempat Penetapan
        10. Tanggal Penetapan
        11. Status Pejabat
        12. Tembusan 
        """
        )
    right1.image("img/surat_keputusan.png", width=300)

    left2, right2 = st.columns(2)
    left2.header("Surat Tugas")
    left2.markdown(
        """
        Dokumen ini adalah surat resmi yang berfungsi 
        sebagai media yang tepat untuk memberitahukan 
        mengenai suatu tugas tertentu.
        dengan elemen yang digunakan yaitu:\n
        1. Nomor Surat Keputusan
        2. Pertimbangan
        3. Dasar
        4. Kepada
        5. Untuk
        6. Tempat Penetapan
        7. Tanggal Penetapan
        8. Status Pejabat
        9. Pejabat Yang menandatangani
        10. Tembusan
        """
        )

    right2.image("img/surat_tugas.png", width=300)

    left3, right3 = st.columns(2)
    left3.header("Petikan Keputusan")
    left3.markdown(
        """
        Dokumen ini adalah petikan dapat berarti kutipan atau nukilan.
        Jadi dari segi bahasa, petikan putusan pengadilan berarti kutipan 
        atau nukilan dari putusan pengadilan
        salinan putusan merupakan turunan putusan yang diterbitkan oleh pengadilan. 
        Sedangkan, petikan putusan merupakan kutipan isi dari putusan yang memuat amar putusan
        dengan elemen yang digunakan yaitu:\n
        1. Dekan Fakultas
        2. Nomor Surat Keputusan
        3. Perihal
        4. Semester
        5. Menimbang
        6. Mengingat
        7. Memperhatikan
        8. Menetapkan
        9. Status Pejabat
        10. Pejabat yang menandatangani
        11. Tembusan
        """
        )


    right3.image("img/petikan_keputusan.png", width=300)

    st.write("untuk panduan penggunaan program bisa dilihat pada tautan berikut ini:")
    st.write("https://drive.google.com/file/d/1ZUflQUTjhPlmUoL2YPw2NfUAEBYHUOWi/view?usp=sharing")

    st.write("untuk questionare dan survey, silahkan kunjungi website kami berikut ini:")
    st.write("https://forms.gle/Y41VykFwTJJmmYKs6")

    st.markdown(
        """
        Referensi:
        1. https://haloedukasi.com/surat-keputusan
        2. https://idcloudhost.com/contoh-surat-tugas-fungsi-manfaat-dan-prosedur-lengkapnya/
        3. https://www.hukumonline.com/klinik/a/perbedaan-antara-petikan-dengan-salinan-lt50849c2f208c2
        """
    )