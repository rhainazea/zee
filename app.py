import streamlit as st
import math

# =========================================================
# KONFIGURASI HALAMAN
# =========================================================
st.set_page_config(
    page_title="Kalkulator pH Larutan",
    page_icon="🧪",
    layout="wide"
)

# =========================================================
# BACKGROUND + CSS STYLE
# =========================================================
st.markdown("""
<style>

.stApp {
    background-image: linear-gradient(
        rgba(255,255,255,0.92),
        rgba(255,255,255,0.92)
    ),
    url("https://images.unsplash.com/photo-1532187643603-ba119ca4109e");

    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}

/* Overlay transparan */
.main::before {
    content: "";
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: rgba(255,255,255,0.82);
    z-index: -1;
}

/* Judul */
h1 {
    color: #0b5394;
    text-align: center;
    font-size: 45px;
    font-weight: bold;
}

/* Subjudul */
h2, h3 {
    color: #134f5c;
}

/* Box hijau */
.box {
    padding: 20px;
    border-radius: 20px;
    background: rgba(217, 234, 211, 0.9);
    margin-bottom: 20px;
    backdrop-filter: blur(5px);
}

/* Box biru */
.box2 {
    padding: 20px;
    border-radius: 20px;
    background: rgba(207, 226, 243, 0.9);
    margin-bottom: 20px;
    backdrop-filter: blur(5px);
}

/* Box kuning */
.box3 {
    padding: 20px;
    border-radius: 20px;
    background: rgba(252, 229, 205, 0.9);
    margin-bottom: 20px;
    backdrop-filter: blur(5px);
}

/* Box hasil */
.ph-box {
    padding: 25px;
    border-radius: 20px;
    background: linear-gradient(to right, #fff3cd, #ffe599);
    text-align: center;
    font-size: 26px;
    font-weight: bold;
    color: #7f6000;
    margin-top: 20px;
    box-shadow: 0px 0px 15px rgba(0,0,0,0.2);
}

/* Tombol */
.stButton>button {
    background: linear-gradient(to right, #0b5394, #3c78d8);
    color: white;
    border-radius: 15px;
    height: 50px;
    font-size: 18px;
    border: none;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: linear-gradient(to bottom, #dbeafe, #b6d7ff);
}

/* Input */
.stNumberInput, .stSelectbox {
    background-color: rgba(255,255,255,0.85);
    border-radius: 10px;
    padding: 5px;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# SIDEBAR MENU
# =========================================================
st.sidebar.title("🧪 MENU NAVIGASI")

menu = st.sidebar.radio(
    "Pilih Menu",
    [
        "🏠 Beranda",
        "🧪 Masukkan Data",
        "🧮 Perhitungan pH",
        "⚗️ Campuran Larutan",
        "📘 Tentang pH"
    ]
)

# =========================================================
# DATABASE LARUTAN
# =========================================================
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
    "HCN": ("Asam Lemah", 6.2e-10),
    "HCOOH": ("Asam Lemah", 1.8e-4),
    "H2CO3": ("Asam Lemah", 4.3e-7),
    "H3PO4": ("Asam Lemah", 7.1e-3),
    "H2S": ("Asam Lemah", 1.0e-7),
    "C6H5COOH": ("Asam Lemah", 6.3e-5),
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

    # ================= BUFFER ASAM =================
    "CH3COOH + CH3COONa": ("Buffer Asam", 1.8e-5),
    "HF + NaF": ("Buffer Asam", 6.8e-4),
    "HCOOH + HCOONa": ("Buffer Asam", 1.8e-4),
    "H2CO3 + NaHCO3": ("Buffer Asam", 4.3e-7),

    # ================= BUFFER BASA =================
    "NH3 + NH4Cl": ("Buffer Basa", 1.8e-5),
    "NH4OH + NH4NO3": ("Buffer Basa", 1.8e-5),
    "CH3NH2 + CH3NH3Cl": ("Buffer Basa", 4.4e-4)
}

# =========================================================
# BERANDA
# =========================================================
if menu == "🏠 Beranda":

    st.title("🧪 KALKULATOR pH LARUTAN")

    st.image(
        "https://cdn-icons-png.flaticon.com/512/2784/2784487.png",
        width=220
    )

    st.markdown("""
    <div class='box'>
    <h2>👋 Selamat Datang</h2>

    <p>
    Aplikasi ini digunakan untuk membantu menghitung pH larutan
    secara cepat, mudah, dan interaktif.
    </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='box2'>
    <h3>🎯 Tujuan Pembuatan</h3>

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

    col1, col2, col3 = st.columns(3)

    with col1:
        st.error("🟥 pH 0 - 6 = ASAM")

    with col2:
        st.warning("🟨 pH 7 = NETRAL")

    with col3:
        st.success("🟦 pH 8 - 14 = BASA")

# =========================================================
# MASUKKAN DATA
# =========================================================
elif menu == "🧪 Masukkan Data":

    st.title("🧪 ANALISIS LARUTAN")

    pilihan = st.selectbox(
        "Pilih Rumus Kimia",
        list(data_larutan.keys())
    )

    konsentrasi = st.number_input(
        "Masukkan Konsentrasi (M)",
        min_value=0.0001,
        value=0.1
    )

    if st.button("🔍 ANALISIS"):

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
        <div class='ph-box'>
        🧪 HASIL ANALISIS
        <br><br>
        Rumus Kimia : {pilihan}
        <br>
        Jenis Larutan : {jenis}
        <br>
        pH = {round(ph,2)}
        </div>
        """, unsafe_allow_html=True)

# =========================================================
# PERHITUNGAN pH
# =========================================================
elif menu == "🧮 Perhitungan pH":

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

    molaritas = st.number_input("Molaritas", value=0.1)

    ka = st.number_input(
        "Ka",
        value=1.8e-5,
        format="%.10f"
    )

    kb = st.number_input(
        "Kb",
        value=1.8e-5,
        format="%.10f"
    )

    if st.button("🧪 HITUNG pH"):

        if jenis == "Asam Kuat":
            ph = -math.log10(molaritas)

        elif jenis == "Asam Lemah":
            h = math.sqrt(ka * molaritas)
            ph = -math.log10(h)

        elif jenis == "Basa Kuat":
            poh = -math.log10(molaritas)
            ph = 14 - poh

        elif jenis == "Basa Lemah":
            oh = math.sqrt(kb * molaritas)
            poh = -math.log10(oh)
            ph = 14 - poh

        elif jenis == "Buffer Asam":
            asam = st.number_input("Konsentrasi Asam", value=0.1)
            garam = st.number_input("Konsentrasi Garam", value=0.1)

            pKa = -math.log10(ka)
            ph = pKa + math.log10(garam/asam)

        elif jenis == "Buffer Basa":
            basa = st.number_input("Konsentrasi Basa", value=0.1)
            garam = st.number_input("Konsentrasi Garam", value=0.1)

            pKb = -math.log10(kb)
            poh = pKb + math.log10(garam/basa)
            ph = 14 - poh

        st.markdown(f"""
        <div class='ph-box'>
        📊 HASIL PERHITUNGAN
        <br><br>
        Jenis Larutan : {jenis}
        <br>
        pH = {round(ph,2)}
        </div>
        """, unsafe_allow_html=True)

# =========================================================
# CAMPURAN LARUTAN
# =========================================================
elif menu == "⚗️ Campuran Larutan":

    st.title("⚗️ CAMPURAN LARUTAN")

    tipe = st.selectbox(
        "Pilih Jenis Campuran",
        [
            "Asam Kuat + Basa Kuat",
            "Asam Lemah + Basa Kuat",
            "Basa Lemah + Asam Kuat",
            "Garam dari Asam Lemah"
        ]
    )

    M1 = st.number_input("Molaritas Larutan 1", value=0.1)
    V1 = st.number_input("Volume Larutan 1 (mL)", value=50.0)

    M2 = st.number_input("Molaritas Larutan 2", value=0.1)
    V2 = st.number_input("Volume Larutan 2 (mL)", value=50.0)

    Ka = st.number_input("Ka ", value=1.8e-5, format="%.10f")
    Kb = st.number_input("Kb ", value=1.8e-5, format="%.10f")

    if st.button("🧪 HITUNG CAMPURAN"):

        mol1 = M1 * V1 / 1000
        mol2 = M2 * V2 / 1000

        volume_total = (V1 + V2) / 1000

        if tipe == "Asam Kuat + Basa Kuat":

            if mol1 > mol2:
                sisa = mol1 - mol2
                h = sisa / volume_total
                ph = -math.log10(h)
                sifat = "Asam"

            elif mol2 > mol1:
                sisa = mol2 - mol1
                oh = sisa / volume_total
                poh = -math.log10(oh)
                ph = 14 - poh
                sifat = "Basa"

            else:
                ph = 7
                sifat = "Netral"

        elif tipe == "Asam Lemah + Basa Kuat":

            if mol1 > mol2:
                sisa_asam = mol1 - mol2
                garam = mol2

                pKa = -math.log10(Ka)
                ph = pKa + math.log10(garam/sisa_asam)

                sifat = "Buffer Asam"

            else:
                sisa_oh = mol2 - mol1
                oh = sisa_oh / volume_total
                poh = -math.log10(oh)
                ph = 14 - poh
                sifat = "Basa"

        elif tipe == "Basa Lemah + Asam Kuat":

            if mol1 > mol2:
                sisa_basa = mol1 - mol2
                garam = mol2

                pKb = -math.log10(Kb)
                poh = pKb + math.log10(garam/sisa_basa)

                ph = 14 - poh
                sifat = "Buffer Basa"

            else:
                sisa_h = mol2 - mol1
                h = sisa_h / volume_total
                ph = -math.log10(h)
                sifat = "Asam"

        elif tipe == "Garam dari Asam Lemah":

            konsentrasi = mol1 / volume_total

            oh = math.sqrt((1e-14 / Ka) * konsentrasi)

            poh = -math.log10(oh)

            ph = 14 - poh
            sifat = "Basa"

        st.markdown(f"""
        <div class='ph-box'>
        ⚗️ HASIL CAMPURAN
        <br><br>
        pH = {round(ph,2)}
        <br>
        Sifat Larutan = {sifat}
        </div>
        """, unsafe_allow_html=True)

        st.write(f"Mol larutan 1 = {mol1:.4f} mol")
        st.write(f"Mol larutan 2 = {mol2:.4f} mol")
        st.write(f"Volume total = {volume_total:.4f} L")

# =========================================================
# TENTANG pH
# =========================================================
elif menu == "📘 Tentang pH":

    st.title("📘 TENTANG pH")

    st.markdown("""
    <div class='box'>
    <h3>Pengertian pH</h3>
    pH larutan adalah ukuran yang digunakan untuk menyatakan
    tingkat keasaman atau kebasaan suatu larutan.
    Nilai pH menunjukkan banyaknya konsentrasi ion hidrogen (H⁺)
    di dalam larutan. 
    pH didefinisikan oleh Sørensen pada tahun 1909 sebagai logaritma negatif dari aktivitas ion hidrogen dalam larutan. Secara matematis, pH dinyatakan sebagai:
pH = -log₁₀[H⁺]
Pada suhu 25°C, hubungan antara pH dan pOH dinyatakan oleh persamaan:
pH + pOH = 14    (pKw = 14 pada 25°C)
Nilai Kw (konstanta autoionisasi air) pada suhu 25°C adalah 1.0 × 10⁻¹⁴, sehingga pada larutan netral, [H⁺] = [OH⁻] = 1.0 × 10⁻⁷ M dan pH = 7.
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='box2'>

        <h3>📚 Rumus pH</h3>

    <b>Asam Kuat</b><br>
    pH = -log[H⁺]

    <br><br>

    <b>Asam Lemah</b><br>
    pH = ½(pKa - log C)

    <br><br>

  <b>Basa Kuat</b><br>
    pOH = -log[OH⁻]
    <br>
    pH = 14 - pOH

    <br><br>

    <b>Basa Lemah</b><br>
    pOH = ½(pKb - log C)
    <br>
    pH = 14 - pOH

    <br><br>

    <b>Buffer Asam</b><br>
    pH = pKa + log([A⁻]/[HA])
    <br><br>

    <b>Buffer Basa</b><br>
    pOH = pKb + log([B]/[BH⁺])
    <br>
    pH = 14 - pOH

    </div>
    """, unsafe_allow_html=True)
    st.success("🧪 Aplikasi dibuat untuk membantu pembelajaran kimia.")
