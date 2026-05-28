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

.ph-box {
    padding: 25px;
    border-radius: 15px;
    background-color: #fff3cd;
    text-align: center;
    font-size: 25px;
    font-weight: bold;
    color: #7f6000;
    margin-top: 20px;
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
        "Campuran Larutan",
        "Tentang pH"
    ]
)

# ======================================================
# DATABASE LARUTAN
# ======================================================
data_larutan = {

    # ASAM KUAT
    "HCl": ("Asam Kuat", 1),
    "HBr": ("Asam Kuat", 1),
    "HI": ("Asam Kuat", 1),
    "HNO3": ("Asam Kuat", 1),
    "HClO4": ("Asam Kuat", 1),
    "H2SO4": ("Asam Kuat", 2),

    # ASAM LEMAH
    "CH3COOH": ("Asam Lemah", 1.8e-5),
    "HF": ("Asam Lemah", 6.8e-4),
    "H2CO3": ("Asam Lemah", 4.3e-7),
    "HCN": ("Asam Lemah", 6.2e-10),
    "HCOOH": ("Asam Lemah", 1.8e-4),
    "H3PO4": ("Asam Lemah", 7.1e-3),

    # BASA KUAT
    "NaOH": ("Basa Kuat", 1),
    "KOH": ("Basa Kuat", 1),
    "LiOH": ("Basa Kuat", 1),
    "Ca(OH)2": ("Basa Kuat", 2),
    "Ba(OH)2": ("Basa Kuat", 2),

    # BASA LEMAH
    "NH3": ("Basa Lemah", 1.8e-5),
    "NH4OH": ("Basa Lemah", 1.8e-5),
    "CH3NH2": ("Basa Lemah", 4.4e-4),

    # BUFFER ASAM
    "CH3COOH + CH3COONa": ("Buffer Asam", 1.8e-5),
    "HF + NaF": ("Buffer Asam", 6.8e-4),

    # BUFFER BASA
    "NH3 + NH4Cl": ("Buffer Basa", 1.8e-5),
    "NH4OH + NH4NO3": ("Buffer Basa", 1.8e-5)
}

# ======================================================
# BERANDA
# ======================================================
if menu == "Beranda":

    st.title("🧪 KALKULATOR pH LARUTAN")

    st.markdown("""
    <div class='box'>
    <h2>👋 Selamat Datang</h2>
    <p>
    Aplikasi ini digunakan untuk menghitung pH berbagai jenis larutan
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
        pH : {round(ph,2)}
        </div>
        """, unsafe_allow_html=True)

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

    molaritas = st.number_input("Molaritas", value=0.1)
    ka = st.number_input("Ka", value=1.8e-5, format="%.10f")
    kb = st.number_input("Kb", value=1.8e-5, format="%.10f")

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

# ======================================================
# CAMPURAN LARUTAN
# ======================================================
elif menu == "Campuran Larutan":

    st.title("⚗️ PERHITUNGAN CAMPURAN LARUTAN")

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

        # ==================================================
        # ASAM KUAT + BASA KUAT
        # ==================================================
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

        # ==================================================
        # ASAM LEMAH + BASA KUAT
        # ==================================================
        elif tipe == "Asam Lemah + Basa Kuat":

            if mol1 > mol2:

                sisa_asam = mol1 - mol2
                garam = mol2

                pKa = -math.log10(Ka)

                ph = pKa + math.log10(garam / sisa_asam)

                sifat = "Buffer Asam"

            elif mol1 == mol2:

                konsentrasi = mol2 / volume_total

                oh = math.sqrt((1e-14 / Ka) * konsentrasi)

                poh = -math.log10(oh)

                ph = 14 - poh

                sifat = "Garam"

            else:

                sisa_oh = mol2 - mol1

                oh = sisa_oh / volume_total

                poh = -math.log10(oh)

                ph = 14 - poh

                sifat = "Basa"

        # ==================================================
        # BASA LEMAH + ASAM KUAT
        # ==================================================
        elif tipe == "Basa Lemah + Asam Kuat":

            if mol1 > mol2:

                sisa_basa = mol1 - mol2
                garam = mol2

                pKb = -math.log10(Kb)

                poh = pKb + math.log10(garam / sisa_basa)

                ph = 14 - poh

                sifat = "Buffer Basa"

            elif mol1 == mol2:

                konsentrasi = mol2 / volume_total

                h = math.sqrt((1e-14 / Kb) * konsentrasi)

                ph = -math.log10(h)

                sifat = "Garam"

            else:

                sisa_h = mol2 - mol1

                h = sisa_h / volume_total

                ph = -math.log10(h)

                sifat = "Asam"

        # ==================================================
        # GARAM ASAM LEMAH
        # ==================================================
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

        st.subheader("📘 Langkah Perhitungan")

        st.write(f"Mol larutan 1 = {mol1:.4f} mol")
        st.write(f"Mol larutan 2 = {mol2:.4f} mol")
        st.write(f"Volume total = {volume_total:.4f} L")

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

    st.success("Aplikasi dibuat untuk membantu pembelajaran kimia.")
