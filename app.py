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
# SIDEBAR
# =========================
menu = st.sidebar.radio(
    "📌 Navigasi",
    ["Beranda", "Masukan Data", "Hasil pH", "Tentang pH"]
)

# =========================
# BERANDA
# =========================
if menu == "Beranda":

    st.title("🧪 KALKULATOR pH LARUTAN")

    st.subheader("Selamat Datang")

    st.write("""
    Aplikasi ini dibuat untuk membantu anda dalam:
    
    • Menganalisis pH larutan  
    • Menentukan jenis larutan  
    
    Gunakan menu navigasi di sebelah kiri untuk memulai.
    """)

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

    st.subheader("Input Parameter")

    # Input Ka
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

    # Input Kb
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

    # Input Molaritas
    pakai_m = st.checkbox("Gunakan Molaritas")

    if pakai_m:
        M = st.number_input(
            "Masukkan Molaritas (M)",
            min_value=0.0
        )
    else:
        M = None
        st.write("Molaritas : Tidak ada")

    # Input Normalitas
    pakai_n = st.checkbox("Gunakan Normalitas")

    if pakai_n:
        N = st.number_input(
            "Masukkan Normalitas (N)",
            min_value=0.0
        )
    else:
        N = None
        st.write("Normalitas : Tidak ada")

    # Simpan data
    st.session_state["jenis"] = jenis
    st.session_state["Ka"] = Ka
    st.session_state["Kb"] = Kb
    st.session_state["M"] = M
    st.session_state["N"] = N

    st.success("Data berhasil disimpan!")

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

        ph = None

        try:

            # =====================
            # ASAM KUAT
            # =====================
            if jenis == "Asam Kuat":

                if M is not None and M > 0:
                    H = M

                elif N is not None and N > 0:
                    H = N

                else:
                    st.error("Masukkan Molaritas atau Normalitas")
                    st.stop()

                ph = -math.log10(H)

            # =====================
            # ASAM LEMAH
            # =====================
            elif jenis == "Asam Lemah":

                if Ka and M:
                    H = math.sqrt(Ka * M)
                    ph = -math.log10(H)

                else:
                    st.error("Masukkan Ka dan Molaritas")
                    st.stop()

            # =====================
            # BASA KUAT
            # =====================
            elif jenis == "Basa Kuat":

                if M is not None and M > 0:
                    OH = M

                elif N is not None and N > 0:
                    OH = N

                else:
                    st.error("Masukkan Molaritas atau Normalitas")
                    st.stop()

                pOH = -math.log10(OH)
                ph = 14 - pOH

            # =====================
            # BASA LEMAH
            # =====================
            elif jenis == "Basa Lemah":

                if Kb and M:
                    OH = math.sqrt(Kb * M)
                    pOH = -math.log10(OH)
                    ph = 14 - pOH

                else:
                    st.error("Masukkan Kb dan Molaritas")
                    st.stop()

            # =====================
            # BUFFER ASAM
            # =====================
            elif jenis == "Buffer Asam":

                if Ka:
                    pKa = -math.log10(Ka)
                    ph = pKa

                else:
                    st.error("Masukkan Ka")
                    st.stop()

            # =====================
            # BUFFER BASA
            # =====================
            elif jenis == "Buffer Basa":

                if Kb:
                    pKb = -math.log10(Kb)
                    pOH = pKb
                    ph = 14 - pOH

                else:
                    st.error("Masukkan Kb")
                    st.stop()

            # =====================
            # OUTPUT
            # =====================
            st.success(f"Jenis Larutan : {jenis}")

            st.metric("Nilai pH", round(ph, 2))

            if ph < 7:
                st.error("Larutan bersifat ASAM")

            elif ph > 7:
                st.success("Larutan bersifat BASA")

            else:
                st.info("Larutan bersifat NETRAL")

        except:
            st.error("Terjadi kesalahan pada perhitungan")

# =========================
# TENTANG pH
# =========================
elif menu == "Tentang pH":

    st.title("📘 Tentang pH")

    st.write("""
    ### Pengertian pH
    
    pH adalah ukuran derajat keasaman atau kebasaan suatu larutan.
    
    ### Klasifikasi pH
    
    • pH < 7  → Asam  
    • pH = 7  → Netral  
    • pH > 7  → Basa  
    
    ---
    
    ### Jenis Larutan
    
    #### 1. Asam Kuat
    Terionisasi sempurna dalam air.
    
    Contoh:
    - HCl
    - HNO3
    
    #### 2. Asam Lemah
    Terionisasi sebagian.
    
    Contoh:
    - CH3COOH
    
    #### 3. Basa Kuat
    Terionisasi sempurna.
    
    Contoh:
    - NaOH
    - KOH
    
    #### 4. Basa Lemah
    Terionisasi sebagian.
    
    Contoh:
    - NH4OH
    
    #### 5. Buffer Asam
    Larutan penyangga dengan pH asam.
    
    #### 6. Buffer Basa
    Larutan penyangga dengan pH basa.
    """)
