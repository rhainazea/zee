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
# CSS WARNA & STYLE
# =========================
st.markdown("""
<style>

/* Background utama */
.stApp {
    background-color: #f4f6fb;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #6C63FF, #8E7CFF);
    color: white;
}

/* Judul sidebar */
section[data-testid="stSidebar"] h1,
section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3,
section[data-testid="stSidebar"] label {
    color: white;
}

/* Card */
.card {
    background-color: white;
    padding: 25px;
    border-radius: 18px;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.1);
    margin-bottom: 20px;
}

/* Box hasil */
.hasil-box {
    background: linear-gradient(135deg, #ffffff, #f3f5ff);
    padding: 35px;
    border-radius: 20px;
    text-align: center;
    box-shadow: 0px 5px 15px rgba(0,0,0,0.1);
}

/* Info box */
.info-box {
    background-color: #eef4ff;
    padding: 18px;
    border-radius: 12px;
    border-left: 6px solid #6C63FF;
}

/* Tombol */
.stButton>button {
    background: linear-gradient(90deg, #6C63FF, #8E7CFF);
    color: white;
    border-radius: 12px;
    border: none;
    padding: 10px 20px;
    font-size: 16px;
}

/* Metric */
[data-testid="metric-container"] {
    background-color: white;
    border-radius: 15px;
    padding: 20px;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.08);
}

/* Input */
.stNumberInput, .stSelectbox {
    background-color: white;
    border-radius: 10px;
}

/* Judul */
h1 {
    color: #2c2c2c;
}

</style>
""", unsafe_allow_html=True)

# =========================
# SIDEBAR
# =========================
st.sidebar.title("🧪 KALKULATOR\npH LARUTAN")

menu = st.sidebar.radio(
    "📌 NAVIGASI",
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

    <h1 style='font-size:45px; color:#6C63FF;'>
    🧪 KALKULATOR pH LARUTAN
    </h1>

    <h2 style='color:#444;'>
    Selamat Datang
    </h2>

    </center>

    <br>

    <p style='font-size:18px;'>

    Aplikasi ini dibuat untuk membantu anda dalam:

    </p>

    <ul style='font-size:18px; line-height:2;'>

        <li>🔹 Menganalisis pH larutan</li>
        <li>🔹 Menentukan jenis larutan</li>

    </ul>

    <br>

    <div class='info-box'>

    📌 Gunakan menu navigasi di sebelah kiri untuk memulai.

    </div>

    </div>
    """, unsafe_allow_html=True)

# =========================
# MASUKAN DATA
# =========================
elif menu == "Masukan Data":

    st.title("📥 Masukan Data")

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

    # =====================
    # KA
    # =====================
    with col1:

        st.markdown("<div class='card'>", unsafe_allow_html=True)

        st.subheader("Ka")

        pakai_ka = st.checkbox("Gunakan Ka")

        if pakai_ka:
            Ka = st.number_input(
                "Masukkan Ka",
                min_value=0.0,
                format="%e"
            )
        else:
            Ka = None
            st.write("Tidak ada")

        st.markdown("</div>", unsafe_allow_html=True)

    # =====================
    # KB
    # =====================
    with col2:

        st.markdown("<div class='card'>", unsafe_allow_html=True)

        st.subheader("Kb")

        pakai_kb = st.checkbox("Gunakan Kb")

        if pakai_kb:
            Kb = st.number_input(
                "Masukkan Kb",
                min_value=0.0,
                format="%e"
            )
        else:
            Kb = None
            st.write("Tidak ada")

        st.markdown("</div>", unsafe_allow_html=True)

    # =====================
    # MOLARITAS
    # =====================
    with col3:

        st.markdown("<div class='card'>", unsafe_allow_html=True)

        st.subheader("Molaritas")

        pakai_m = st.checkbox("Gunakan Molaritas")

        if pakai_m:
            M = st.number_input(
                "Masukkan Molaritas",
                min_value=0.0
            )
        else:
            M = None
            st.write("Tidak ada")

        st.markdown("</div>", unsafe_allow_html=True)

    # =====================
    # NORMALITAS
    # =====================
    with col4:

        st.markdown("<div class='card'>", unsafe_allow_html=True)

        st.subheader("Normalitas")

        pakai_n = st.checkbox("Gunakan Normalitas")

        if pakai_n:
            N = st.number_input(
                "Masukkan Normalitas",
                min_value=0.0
            )
        else:
            N = None
            st.write("Tidak ada")

        st.markdown("</div>", unsafe_allow_html=True)

    # Simpan session
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

    st.title("📊 Hasil Perhitungan pH")

    jenis = st.session_state.get("jenis")
    Ka = st.session_state.get("Ka")
    Kb = st.session_state.get("Kb")
    M = st.session_state.get("M")
    N = st.session_state.get("N")

    if jenis is None:

        st.warning("Silakan isi data terlebih dahulu")

    else:

        try:

            ph = 0

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

                ph = -math.log10(Ka)

            # =====================
            # BUFFER BASA
            # =====================
            elif jenis == "Buffer Basa":

                ph = 14 + math.log10(Kb)

            # =====================
            # WARNA HASIL
            # =====================
            if ph < 7:
                sifat = "ASAM"
                warna = "#ff4b4b"

            elif ph > 7:
                sifat = "BASA"
                warna = "#00b894"

            else:
                sifat = "NETRAL"
                warna = "#0984e3"

            col1, col2 = st.columns(2)

            # =====================
            # RINGKASAN
            # =====================
            with col1:

                st.markdown(f"""
                <div class='card'>

                <h3>📋 Ringkasan Input</h3>

                <p><b>Jenis Larutan :</b> {jenis}</p>
                <p><b>Ka :</b> {Ka}</p>
                <p><b>Kb :</b> {Kb}</p>
                <p><b>Molaritas :</b> {M}</p>
                <p><b>Normalitas :</b> {N}</p>

                </div>
                """, unsafe_allow_html=True)

            # =====================
            # HASIL
            # =====================
            with col2:

                st.markdown(f"""
                <div class='hasil-box'>

                <h2>Nilai pH</h2>

                <h1 style='font-size:70px; color:{warna};'>
                {round(ph,2)}
                </h1>

                <h2>
                Larutan Bersifat
                <span style='color:{warna};'>
                {sifat}
                </span>
                </h2>

                </div>
                """, unsafe_allow_html=True)

            st.markdown(f"""
            <div class='info-box'>

            💡 Perhitungan pH berhasil dilakukan menggunakan rumus {jenis}.

            </div>
            """, unsafe_allow_html=True)

        except:

            st.error("❌ Terjadi kesalahan perhitungan")

# =========================
# TENTANG pH
# =========================
elif menu == "Tentang pH":

    st.title("📘 Tentang pH")

    st.markdown("""
    <div class='card'>

    <h2 style='color:#6C63FF;'>Pengertian pH</h2>

    <p style='font-size:18px;'>
    pH adalah ukuran derajat keasaman atau kebasaan suatu larutan.
    </p>

    <br>

    <h3 style='color:#6C63FF;'>Klasifikasi pH</h3>

    <ul style='line-height:2; font-size:18px;'>

        <li>🔴 pH &lt; 7 → Asam</li>
        <li>🔵 pH = 7 → Netral</li>
        <li>🟢 pH &gt; 7 → Basa</li>

    </ul>

    <br>

    <h3 style='color:#6C63FF;'>Jenis Larutan</h3>

    <ul style='line-height:2; font-size:18px;'>

        <li>Asam Kuat</li>
        <li>Asam Lemah</li>
        <li>Basa Kuat</li>
        <li>Basa Lemah</li>
        <li>Buffer Asam</li>
        <li>Buffer Basa</li>

    </ul>

    </div>
    """, unsafe_allow_html=True)
