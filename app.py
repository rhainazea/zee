```python
import streamlit as st
import math

# Konfigurasi halaman
st.set_page_config(
    page_title="Kalkulator pH Larutan",
    page_icon="🧪",
    layout="wide"
)

# =========================
# SIDEBAR NAVIGASI
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

    st.write("### Selamat Datang")

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

    # Opsi input
    opsi_ka = st.checkbox("Gunakan Ka")
    opsi_kb = st.checkbox("Gunakan Kb")
    opsi_m = st.checkbox("Gunakan Molaritas")
    opsi_n = st.checkbox("Gunakan Normalitas")

    Ka = None
    Kb = None
    M = None
    N = None

    if opsi_ka:
        Ka = st.number_input("Masukkan Ka", min_value=0.0, format="%e")

    else:
        st.write("Ka : Tidak ada")

    if opsi_kb:
        Kb = st.number_input("Masukkan Kb", min_value=0.0, format="%e")

    else:
        st.write("Kb : Tidak ada")

    if opsi_m:
        M = st.number_input("Masukkan Molaritas (M)", min_value=0.0)

    else:
        st.write("Molaritas : Tidak ada")

    if opsi_n:
        N = st.number_input("Masukkan Normalitas (N)", min_value=0.0)

    else:
        st.write("Normalitas : Tidak ada")

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

    jenis = st.session_state.get("jenis", None)
    Ka = st.session_state.get("Ka", None)
    Kb = st.session_state.get("Kb", None)
    M = st.session_state.get("M", None)
    N = st.session_state.get("N", None)

    if jenis is None:
        st.warning("Silakan isi data terlebih dahulu pada menu 'Masukan Data'")
    else:

        ph = None

        try:

            # =====================
            # ASAM KUAT
            # =====================
            if jenis == "Asam Kuat":

                if M:
                    H = M
                elif N:
                    H = N
                else:
                    H = 0

                ph = -math.log10(H)

            # =====================
            # ASAM LEMAH
            # =====================
            elif jenis == "Asam Lemah":

                if Ka and M:
                    H = math.sqrt(Ka * M)
                    ph = -math.log10(H)

            # =====================
            # BASA KUAT
            # =====================
            elif jenis == "Basa Kuat":

                if M:
                    OH = M
                elif N:
                    OH = N
                else:
                    OH = 0

                poh = -math.log10(OH)
                ph = 14 - poh

            # =====================
            # BASA LEMAH
            # =====================
            elif jenis == "Basa Lemah":

                if Kb and M:
                    OH = math.sqrt(Kb * M)
                    poh = -math.log10(OH)
                    ph = 14 - poh

            # =====================
            # BUFFER ASAM
            # =====================
            elif jenis == "Buffer Asam":

                if Ka and M:
                    pKa = -math.log10(Ka)
                    ph = pKa

            # =====================
            # BUFFER BASA
            # =====================
            elif jenis == "Buffer Basa":

                if Kb and M:
                    pKb = -math.log10(Kb)
                    poh = pKb
                    ph = 14 - poh

            # =====================
            # OUTPUT
            # =====================
            if ph is not None:

                st.success(f"Jenis Larutan : {jenis}")
                st.info(f"Nilai pH = {round(ph, 2)}")

                if ph < 7:
                    st.write("Larutan bersifat ASAM")

                elif ph > 7:
                    st.write("Larutan bersifat BASA")

                else:
                    st.write("Larutan bersifat NETRAL")

            else:
                st.error("Data belum lengkap untuk perhitungan")

        except:
            st.error("Terjadi kesalahan dalam perhitungan")

# =========================
# TENTANG pH
# =========================
elif menu == "Tentang pH":

    st.title("📘 Tentang pH")

    st.write("""
    ### Pengertian pH
    
    pH adalah ukuran derajat keasaman atau kebasaan suatu larutan.
    
    Nilai pH berkisar antara:
    
    • pH < 7  → Bersifat asam  
    • pH = 7  → Netral  
    • pH > 7  → Bersifat basa  
    
    ### Jenis Larutan
    
    #### 1. Asam Kuat
    Asam yang terionisasi sempurna dalam air.
    
    Contoh:
    • HCl  
    • HNO3  
    
    #### 2. Asam Lemah
    Asam yang terionisasi sebagian dalam air.
    
    Contoh:
    • CH3COOH  
    
    #### 3. Basa Kuat
    Basa yang terionisasi sempurna.
    
    Contoh:
    • NaOH  
    • KOH  
    
    #### 4. Basa Lemah
    Basa yang terionisasi sebagian.
    
    Contoh:
    • NH4OH  
    
    #### 5. Buffer Asam
    Larutan yang mempertahankan pH asam.
    
    #### 6. Buffer Basa
    Larutan yang mempertahankan pH basa.
    """)
```
