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
# CSS CUSTOM
# =========================
st.markdown("""
<style>

.main {
    background-color: #f5f6fa;
}

h1, h2, h3 {
    color: #1f1f1f;
}

.stButton>button {
    background-color: #6C63FF;
    color: white;
    border-radius: 10px;
    border: none;
    padding: 10px 20px;
}

.card {
    background-color: white;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0px 0px 10px rgba(0,0,0,0.1);
    margin-bottom: 20px;
}

.hasil-box {
    background-color: white;
    padding: 30px;
    border-radius: 15px;
    text-align: center;
    box-shadow: 0px 0px 10px rgba(0,0,0,0.1);
}

.info-box {
    background-color: #eef4ff;
    padding: 15px;
    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)

# =========================
# SIDEBAR
# =========================
st.sidebar.title("🧪 KALKULATOR\npH LARUTAN")

menu = st.sidebar.radio(
    "NAVIGASI",
    [
        "Beranda",
        "Masukan Data",
        "Hasil pH",
        "Tentang pH"
    ]
)

# =========================
# BERANDA
# =========================
if menu == "Beranda":

    st.markdown("""
    <div class='card'>
    <center>
    <h1>🧪 KALKULATOR pH LARUTAN</h1>
    <h2 style='color:#6C63FF;'>Selamat Datang</h2>
    </center>

    <br>

    <p style='font-size:18px;'>
    Aplikasi ini dibuat untuk membantu anda dalam:
    </p>

    <ul style='font-size:18px;'>
        <li>Menganalisis pH larutan</li>
        <li>Menentukan jenis larutan</li>
    </ul>

    <br>

    <div class='info-box'>
    Gunakan menu navigasi di sebelah kiri untuk memulai
    </div>

    </div>
    """, unsafe_allow_html=True)

# =========================
# MASUKAN DATA
# =========================
elif menu == "Masukan Data":

    st.title("Masukan Data")

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

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.markdown("<div class='card'>", unsafe_allow_html=True)

        pakai_ka = st.checkbox("Gunakan Ka")

        if pakai_ka:
            Ka = st.number_input(
                "Masukkan Ka",
                min_value=0.0,
                format="%e"
            )
        else:
            Ka = None
            st.write("Ka : Tidak ada")

        st.markdown("</div>", unsafe_allow_html=True)

    with col2:

        st.markdown("<div class='card'>", unsafe_allow_html=True)

        pakai_kb = st.checkbox("Gunakan Kb")

        if pakai_kb:
            Kb = st.number_input(
                "Masukkan Kb",
                min_value=0.0,
                format="%e"
            )
        else:
            Kb = None
            st.write("Kb : Tidak ada")

        st.markdown("</div>", unsafe_allow_html=True)

    with col3:

        st.markdown("<div class='card'>", unsafe_allow_html=True)

        pakai_m = st.checkbox("Gunakan Molaritas")

        if pakai_m:
            M = st.number_input(
                "Masukkan Molaritas",
                min_value=0.0
            )
        else:
            M = None
            st.write("Molaritas : Tidak ada")

        st.markdown("</div>", unsafe_allow_html=True)

    with col4:

        st.markdown("<div class='card'>", unsafe_allow_html=True)

        pakai_n = st.checkbox("Gunakan Normalitas")

        if pakai_n:
            N = st.number_input(
                "Masukkan Normalitas",
                min_value=0.0
            )
        else:
            N = None
            st.write("Normalitas : Tidak ada")

        st.markdown("</div>", unsafe_allow_html=True)

    st.session_state["jenis"] = jenis
    st.session_state["Ka"] = Ka
    st.session_state["Kb"] = Kb
    st.session_state["M"] = M
    st.session_state["N"] = N

    st.success("✅ Data berhasil disimpan!")

# =========================
# HASIL pH
# =========================
elif menu == "Hasil pH":

    st.title("Hasil Perhitungan pH")

    jenis = st.session_state.get("jenis")
    Ka = st.session_state.get("Ka")
    Kb = st.session_state.get("Kb")
    M = st.session_state.get("M")
    N = st.session_state.get("N")

    if jenis is None:

        st.warning("Silakan isi data terlebih dahulu")

    else:

        ph = None

        try:

            # =====================
            # ASAM KUAT
            # =====================
            if jenis == "Asam Kuat":

                H = M if M else N
                ph = -math.log10(H)

            # =====================
            # ASAM LEMAH
            # =====================
            elif jenis == "Asam Lemah":

                H = math.sqrt(Ka * M)
                ph = -math.log10(H)

            # =====================
            # BASA KUAT
            # =====================
            elif jenis == "Basa Kuat":

                OH = M if M else N
                pOH = -math.log10(OH)
                ph = 14 - pOH

            # =====================
            # BASA LEMAH
            # =====================
            elif jenis == "Basa Lemah":

                OH = math.sqrt(Kb * M)
                pOH = -math.log10(OH)
                ph = 14 - pOH

            # =====================
            # BUFFER ASAM
            # =====================
            elif jenis == "Buffer Asam":

                pKa = -math.log10(Ka)
                ph = pKa

            # =====================
            # BUFFER BASA
            # =====================
            elif jenis == "Buffer Basa":

                pKb = -math.log10(Kb)
                ph = 14 - pKb

            # =====================
            # TAMPILAN HASIL
            # =====================

            col1, col2 = st.columns([1,1])

            with col1:

                st.markdown(f"""
                <div class='card'>
                <h3>Ringkasan Input</h3>

                <p><b>Jenis Larutan :</b> {jenis}</p>
                <p><b>Ka :</b> {Ka}</p>
                <p><b>Kb :</b> {Kb}</p>
                <p><b>Molaritas :</b> {M}</p>
                <p><b>Normalitas :</b> {N}</p>

                </div>
                """, unsafe_allow_html=True)

            with col2:

                sifat = ""
                warna = ""

                if ph < 7:
                    sifat = "ASAM"
                    warna = "red"

                elif ph > 7:
                    sifat = "BASA"
                    warna = "green"

                else:
                    sifat = "NETRAL"
                    warna = "blue"

                st.markdown(f"""
                <div class='hasil-box'>

                <h2>Nilai pH</h2>

                <h1 style='font-size:60px; color:{warna};'>
                {round(ph,2)}
                </h1>

                <h3>
                Larutan bersifat 
                <span style='color:{warna};'>{sifat}</span>
                </h3>

                </div>
                """, unsafe_allow_html=True)

            st.markdown(f"""
            <div class='info-box'>
            <h4>Perhitungan ({jenis})</h4>

            <p>Nilai pH berhasil dihitung menggunakan rumus yang sesuai.</p>
            </div>
            """, unsafe_allow_html=True)

        except:

            st.error("Terjadi kesalahan perhitungan")

# =========================
# TENTANG pH
# =========================
elif menu == "Tentang pH":

    st.title("Tentang pH")

    st.markdown("""
    <div class='card'>

    <h2 style='color:#6C63FF;'>Pengertian pH</h2>

    <p>
    pH adalah ukuran derajat keasaman atau kebasaan suatu larutan.
    </p>

    <br>

    <h3>Nilai pH</h3>

    <ul>
        <li>pH < 7 → Bersifat asam</li>
        <li>pH = 7 → Netral</li>
        <li>pH > 7 → Bersifat basa</li>
    </ul>

    <br>

    <h2 style='color:#6C63FF;'>Jenis Larutan</h2>

    <h4>1. Asam Kuat</h4>
    <p>Asam yang terionisasi sempurna.</p>

    <h4>2. Asam Lemah</h4>
    <p>Asam yang terionisasi sebagian.</p>

    <h4>3. Basa Kuat</h4>
    <p>Basa yang terionisasi sempurna.</p>

    <h4>4. Basa Lemah</h4>
    <p>Basa yang terionisasi sebagian.</p>

    <h4>5. Buffer Asam</h4>
    <p>Larutan penyangga dengan pH asam.</p>

    <h4>6. Buffer Basa</h4>
    <p>Larutan penyangga dengan pH basa.</p>

    </div>
    """, unsafe_allow_html=True)
