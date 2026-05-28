import streamlit as st
import math

# ======================================================
# KONFIGURASI HALAMAN
# ======================================================
st.set_page_config(
    page_title="Kalkulator pH Larutan",
    page_icon="🧪",
    layout="wide"
)

# ======================================================
# CSS STYLE
# ======================================================
st.markdown("""
<style>

.main {
    background: linear-gradient(to bottom, #e3f2fd, #ffffff);
}

h1 {
    color: #0b5394;
    text-align: center;
    font-size: 45px;
}

h2, h3 {
    color: #134f5c;
}

.box {
    padding: 20px;
    border-radius: 15px;
    background-color: #d9ead3;
    margin-bottom: 20px;
    box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
}

.box2 {
    padding: 20px;
    border-radius: 15px;
    background-color: #cfe2f3;
    margin-bottom: 20px;
    box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
}

.box3 {
    padding: 20px;
    border-radius: 15px;
    background-color: #fce5cd;
    margin-bottom: 20px;
    box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
}

.stButton>button {
    background-color: #0b5394;
    color: white;
    border-radius: 12px;
    height: 50px;
    font-size: 18px;
    width: 100%;
}

.sidebar .sidebar-content {
    background-color: #d0e0ff;
}

.ph-box {
    padding: 25px;
    border-radius: 15px;
    background-color: #fff3cd;
    text-align: center;
    font-size: 25px;
    font-weight: bold;
    color: #7f6000;
}

</style>
""", unsafe_allow_html=True)

# ======================================================
# SIDEBAR
# ======================================================
st.sidebar.title("🧪 MENU NAVIGASI")

menu = st.sidebar.radio(
    "Pilih Menu",
    [
        "Beranda",
        "Masukkan Data",
        "Perhitungan pH",
        "Tentang pH"
    ]
)

# ======================================================
# DATABASE LARUTAN
# ======================================================
data_larutan = {

    # ================= ASAM KUAT =================
    "HCl": ("Asam Kuat", 1),
    "HBr": ("Asam Kuat", 1),
    "HI": ("Asam Kuat", 1),
    "HNO3": ("Asam Kuat", 1),
    "HClO4": ("Asam Kuat", 1),
    "H2SO4": ("Asam Kuat", 2),

    # ================= ASAM LEMAH =================
    "CH3COOH": ("Asam Lemah", 1.8e-5),
    "HF": ("Asam Lemah", 6.8e-4),
    "H2CO3": ("Asam Lemah", 4.3e-7),
    "HCN": ("Asam Lemah", 6.2e-10),
    "HCOOH": ("Asam Lemah", 1.8e-4),
    "H3PO4": ("Asam Lemah", 7.1e-3),
    "C6H5COOH": ("Asam Lemah", 6.3e-5),
    "H2S": ("Asam Lemah", 1.0e-7),
    "HNO2": ("Asam Lemah", 4.5e-4),

    # ================= BASA KUAT =================
    "NaOH": ("Basa Kuat", 1),
    "KOH": ("Basa Kuat", 1),
    "LiOH": ("Basa Kuat", 1),
    "Ca(OH)2": ("Basa Kuat", 2),
    "Ba(OH)2": ("Basa Kuat", 2),
    "Sr(OH)2": ("Basa Kuat", 2),

    # ================= BASA LEMAH =================
    "NH3": ("Basa Lemah", 1.8e-5),
    "NH4OH": ("Basa Lemah", 1.8e-5),
    "CH3NH2": ("Basa Lemah", 4.4e-4),
    "(CH3)2NH": ("Basa Lemah", 5.4e-4),
    "C5H5N": ("Basa Lemah", 1.7e-9),
    "Al(OH)3": ("Basa Lemah", 1.3e-5),

    # ================= BUFFER ASAM =================
    "CH3COOH + CH3COONa": ("Buffer Asam", 1.8e-5),
    "H2CO3 + NaHCO3": ("Buffer Asam", 4.3e-7),
    "HF + NaF": ("Buffer Asam", 6.8e-4),
    "HCOOH + HCOONa": ("Buffer Asam", 1.8e-4),

    # ================= BUFFER BASA =================
    "NH3 + NH4Cl": ("Buffer Basa", 1.8e-5),
    "NH4OH + NH4NO3": ("Buffer Basa", 1.8e-5),
    "CH3NH2 + CH3NH3Cl": ("Buffer Basa", 4.4e-4)
}

# ======================================================
# BERANDA
# ======================================================
if menu == "Beranda":

    st.title("🧪 KALKULATOR pH LARUTAN")

    st.image(
        "https://cdn-icons-png.flaticon.com/512/2784/2784487.png",
        width=180
    )

    st.markdown("""
    <div class='box'>
    <h2>👋 Selamat Datang</h2>
    <p>
    Aplikasi Kalkulator pH Larutan berbasis Python dan Streamlit
    untuk membantu menghitung pH berbagai jenis larutan secara cepat,
    mudah, dan interaktif.
    </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='box2'>
    <h3>🎯 Tujuan Pembuatan Kalkulator pH</h3>
    <ul>
        <li>Mempermudah perhitungan pH</li>
        <li>Mengurangi kesalahan perhitungan</li>
        <li>Membantu proses pembelajaran</li>
        <li>Mempercepat analisis larutan</li>
        <li>Menentukan sifat larutan</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("📊 Skala pH")

    st.progress(1)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.error("🟥 pH 0 - 6 : ASAM")

    with col2:
        st.warning("🟨 pH 7 : NETRAL")

    with col3:
        st.success("🟦 pH 8 - 14 : BASA")

# ======================================================
# MASUKKAN DATA
# ======================================================
elif menu == "Masukkan Data":

    st.title("📥 MASUKKAN DATA LARUTAN")

    pilihan = st.selectbox(
        "🧪 Pilih Rumus Kimia",
        list(data_larutan.keys())
    )

    konsentrasi = st.number_input(
        "Masukkan Konsentrasi (M)",
        min_value=0.0001,
        value=0.1
    )

    if st.button("🔍 ANALISIS LARUTAN"):

        jenis, nilai = data_larutan[pilihan]

        # ================= PERHITUNGAN =================
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

        # ================= OUTPUT =================
        st.markdown(f"""
        <div class='ph-box'>
        🧪 HASIL ANALISIS
        <br><br>
        Rumus Kimia : {pilihan}
        <br>
        Jenis Larutan : {jenis}
        <br>
        pH Larutan : {round(ph,2)}
        </div>
        """, unsafe_allow_html=True)

        if "Asam" in jenis:
            st.error("Larutan Bersifat Asam")

        elif "Basa" in jenis:
            st.success("Larutan Bersifat Basa")

# ======================================================
# PERHITUNGAN PH
# ======================================================
elif menu == "Perhitungan pH":

    st.title("🧮 PERHITUNGAN pH")

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

    if st.button("🧪 HITUNG pH"):

        # ================= ASAM KUAT =================
        if jenis == "Asam Kuat":

            h = molaritas
            ph = -math.log10(h)

        # ================= ASAM LEMAH =================
        elif jenis == "Asam Lemah":

            if ka == 0:
                st.error("Masukkan nilai Ka")
                st.stop()

            h = math.sqrt(ka * molaritas)
            ph = -math.log10(h)

        # ================= BASA KUAT =================
        elif jenis == "Basa Kuat":

            oh = molaritas
            poh = -math.log10(oh)
            ph = 14 - poh

        # ================= BASA LEMAH =================
        elif jenis == "Basa Lemah":

            if kb == 0:
                st.error("Masukkan nilai Kb")
                st.stop()

            oh = math.sqrt(kb * molaritas)
            poh = -math.log10(oh)
            ph = 14 - poh

        # ================= BUFFER ASAM =================
        elif jenis == "Buffer Asam":

            asam = st.number_input(
                "Konsentrasi Asam [HA]",
                value=0.1
            )

            garam = st.number_input(
                "Konsentrasi Garam [A-]",
                value=0.1
            )

            if ka == 0:
                st.error("Masukkan Ka")
                st.stop()

            pka = -math.log10(ka)
            ph = pka + math.log10(garam/asam)

        # ================= BUFFER BASA =================
        elif jenis == "Buffer Basa":

            basa = st.number_input(
                "Konsentrasi Basa [B]",
                value=0.1
            )

            garam = st.number_input(
                "Konsentrasi Garam [BH+]",
                value=0.1
            )

            if kb == 0:
                st.error("Masukkan Kb")
                st.stop()

            pkb = -math.log10(kb)
            poh = pkb + math.log10(garam/basa)
            ph = 14 - poh

        st.markdown(f"""
        <div class='ph-box'>
        📊 HASIL PERHITUNGAN
        <br><br>
        Jenis Larutan : {jenis}
        <br>
        pH Larutan : {round(ph,2)}
        </div>
        """, unsafe_allow_html=True)

# ======================================================
# TENTANG PH
# ======================================================
elif menu == "Tentang pH":

    st.title("📘 TENTANG pH")

    st.markdown("""
    <div class='box'>
    <h3>Pengertian pH</h3>

    <p>
    pH larutan adalah ukuran yang digunakan untuk menyatakan
    tingkat keasaman atau kebasaan suatu larutan.
    Nilai pH menunjukkan banyaknya konsentrasi ion hidrogen (H⁺)
    di dalam larutan.
    </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='box2'>

    <h3>📚 Rumus pH</h3>

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

    st.subheader("🧪 Contoh Larutan")

    st.write("""
    - Asam Kuat : HCl, HNO3, H2SO4
    - Asam Lemah : CH3COOH, HF, HCN
    - Basa Kuat : NaOH, KOH, Ba(OH)2
    - Basa Lemah : NH3, NH4OH
    - Buffer Asam : CH3COOH + CH3COONa
    - Buffer Basa : NH3 + NH4Cl
    """)

    st.image(
        "https://cdn-icons-png.flaticon.com/512/4341/4341139.png",
        width=200
    )

    st.success("Aplikasi dibuat untuk membantu pembelajaran kimia khususnya materi pH larutan.")
