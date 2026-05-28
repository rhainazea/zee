import streamlit as st
import math

# =========================
# KONFIGURASI HALAMAN
# =========================
st.set_page_config(
    page_title="Kalkulator pH Larutan",
    page_icon="🧪",
    layout="wide"
)

# =========================
# CSS / WARNA
# =========================
st.markdown("""
<style>
.main {
    background-color: #f4f8ff;
}

h1 {
    color: #0b5394;
    text-align: center;
}

h2, h3 {
    color: #134f5c;
}

.stButton>button {
    background-color: #4a86e8;
    color: white;
    border-radius: 10px;
    height: 45px;
    width: 100%;
    font-size: 16px;
}

.box {
    padding: 20px;
    border-radius: 15px;
    background-color: #d9ead3;
    margin-bottom: 15px;
}

.box2 {
    padding: 20px;
    border-radius: 15px;
    background-color: #cfe2f3;
    margin-bottom: 15px;
}

.box3 {
    padding: 20px;
    border-radius: 15px;
    background-color: #fce5cd;
    margin-bottom: 15px;
}

.sidebar .sidebar-content {
    background-color: #e3f2fd;
}
</style>
""", unsafe_allow_html=True)

# =========================
# SIDEBAR NAVIGASI
# =========================
menu = st.sidebar.radio(
    "📌 Navigasi",
    ["Beranda", "Masukkan Data", "Perhitungan pH", "Tentang pH"]
)

# =========================
# DATABASE SEDERHANA
# =========================
data_larutan = {
    "HCl": ("Asam Kuat", 1),
    "HNO3": ("Asam Kuat", 1),
    "H2SO4": ("Asam Kuat", 2),
    "CH3COOH": ("Asam Lemah", 1.8e-5),
    "HF": ("Asam Lemah", 6.8e-4),
    "NaOH": ("Basa Kuat", 1),
    "KOH": ("Basa Kuat", 1),
    "NH4OH": ("Basa Lemah", 1.8e-5),
    "NH3": ("Basa Lemah", 1.8e-5),
    "CH3COOH + CH3COONa": ("Buffer Asam", 1.8e-5),
    "NH3 + NH4Cl": ("Buffer Basa", 1.8e-5)
}

# =========================
# BERANDA
# =========================
if menu == "Beranda":

    st.title("🧪 KALKULATOR pH LARUTAN")

    st.image(
        "https://cdn-icons-png.flaticon.com/512/3655/3655599.png",
        width=150
    )

    st.markdown("""
    <div class='box'>
    <h3>👋 Selamat Datang</h3>
    <p>
    Aplikasi ini digunakan untuk membantu menghitung pH larutan secara cepat,
    mudah, dan interaktif.
    </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='box2'>
    <h3>🎯 Tujuan Pembuatan Kalkulator pH Larutan</h3>
    <ul>
        <li>Mempermudah perhitungan pH</li>
        <li>Mengurangi kesalahan perhitungan</li>
        <li>Membantu proses pembelajaran</li>
        <li>Mempercepat analisis larutan</li>
        <li>Menentukan sifat larutan</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

    st.success("Gunakan menu navigasi di sebelah kiri untuk mulai menggunakan aplikasi.")

# =========================
# MASUKKAN DATA
# =========================
elif menu == "Masukkan Data":

    st.title("📥 Masukkan Data Larutan")

    pilihan = st.selectbox(
        "Pilih Rumus Kimia",
        list(data_larutan.keys())
    )

    konsentrasi = st.number_input(
        "Masukkan Konsentrasi (M)",
        min_value=0.0001,
        value=0.1
    )

    if st.button("🔍 Tentukan Jenis Larutan"):

        jenis, nilai = data_larutan[pilihan]

        if jenis == "Asam Kuat":
            h = konsentrasi * nilai
            ph = -math.log10(h)

        elif jenis == "Asam Lemah":
            h = math.sqrt(nilai * konsentrasi)
            ph = -math.log10(h)

        elif jenis == "Basa Kuat":
            oh = konsentrasi * nilai
            poh = -math.log10(oh)
            ph = 14 - poh

        elif jenis == "Basa Lemah":
            oh = math.sqrt(nilai * konsentrasi)
            poh = -math.log10(oh)
            ph = 14 - poh

        elif jenis == "Buffer Asam":
            ph = 4.75

        elif jenis == "Buffer Basa":
            ph = 9.25

        st.markdown(f"""
        <div class='box3'>
        <h3>📊 Hasil Analisis</h3>
        <p><b>Rumus Kimia :</b> {pilihan}</p>
        <p><b>Jenis Larutan :</b> {jenis}</p>
        <p><b>pH Larutan :</b> {round(ph,2)}</p>
        </div>
        """, unsafe_allow_html=True)

# =========================
# PERHITUNGAN PH
# =========================
elif menu == "Perhitungan pH":

    st.title("🧮 Perhitungan pH")

    jenis = st.selectbox(
        "Pilih Jenis Larutan",
        [
            "Asam Kuat",
            "Asam Lemah",
            "Basa Kuat",
            "Basa Lemah",
            "Buffer Asam",
            "Buffer Basa"
        ]
    )

    st.subheader("📌 Input Data")

    ka = st.number_input("Masukkan Ka", value=0.0)
    kb = st.number_input("Masukkan Kb", value=0.0)
    molaritas = st.number_input("Masukkan Molaritas", value=0.1)
    normalitas = st.number_input("Masukkan Normalitas", value=0.0)

    if st.button("🧪 Hitung pH"):

        if jenis == "Asam Kuat":
            if normalitas > 0:
                h = normalitas
            else:
                h = molaritas

            ph = -math.log10(h)

        elif jenis == "Asam Lemah":
            if ka == 0:
                st.error("Masukkan nilai Ka")
            else:
                h = math.sqrt(ka * molaritas)
                ph = -math.log10(h)

        elif jenis == "Basa Kuat":
            if normalitas > 0:
                oh = normalitas
            else:
                oh = molaritas

            poh = -math.log10(oh)
            ph = 14 - poh

        elif jenis == "Basa Lemah":
            if kb == 0:
                st.error("Masukkan nilai Kb")
            else:
                oh = math.sqrt(kb * molaritas)
                poh = -math.log10(oh)
                ph = 14 - poh

        elif jenis == "Buffer Asam":
            asam = st.number_input("Konsentrasi Asam", value=0.1)
            garam = st.number_input("Konsentrasi Garam", value=0.1)

            if ka == 0:
                st.error("Masukkan Ka")
            else:
                pka = -math.log10(ka)
                ph = pka + math.log10(garam/asam)

        elif jenis == "Buffer Basa":
            basa = st.number_input("Konsentrasi Basa", value=0.1)
            garam = st.number_input("Konsentrasi Garam", value=0.1)

            if kb == 0:
                st.error("Masukkan Kb")
            else:
                pkb = -math.log10(kb)
                poh = pkb + math.log10(garam/basa)
                ph = 14 - poh

        st.success(f"✅ Jenis Larutan : {jenis}")
        st.info(f"📌 pH Larutan = {round(ph,2)}")

# =========================
# TENTANG PH
# =========================
elif menu == "Tentang pH":

    st.title("📘 Tentang pH")

    st.markdown("""
    <div class='box'>
    <h3>Pengertian pH</h3>
    <p>
    pH larutan adalah ukuran yang digunakan untuk menyatakan tingkat
    keasaman atau kebasaan suatu larutan.
    Nilai pH menunjukkan banyaknya konsentrasi ion hidrogen (H⁺)
    di dalam larutan.
    </p>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("📚 Rumus pH")

    st.markdown("""
    <div class='box2'>

    <b>Asam Kuat</b><br>
    pH = -log[H⁺] = -log(C)
    <br><br>

    <b>Asam Lemah</b><br>
    pH = ½(pKa - log C)
    <br><br>

    <b>Basa Kuat</b><br>
    pOH = -log[OH⁻]<br>
    pH = 14 - pOH
    <br><br>

    <b>Basa Lemah</b><br>
    pOH = ½(pKb - log C)<br>
    pH = 14 - pOH
    <br><br>

    <b>Buffer Asam</b><br>
    pH = pKa + log([A⁻]/[HA])
    <br><br>

    <b>Buffer Basa</b><br>
    pOH = pKb + log([B]/[BH⁺])<br>
    pH = 14 - pOH

    </div>
    """, unsafe_allow_html=True)

    st.image(
        "https://cdn-icons-png.flaticon.com/512/2784/2784487.png",
        width=200
    )

    st.success("Aplikasi ini dibuat untuk membantu pembelajaran kimia khususnya materi pH larutan.")
