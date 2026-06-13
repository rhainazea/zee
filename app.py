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

.main::before {
    content: "";
    position: fixed;
    top: 0; left: 0; right: 0; bottom: 0;
    background: rgba(255,255,255,0.82);
    z-index: -1;
}

h1 { color: #0b5394; text-align: center; font-size: 45px; font-weight: bold; }
h2, h3 { color: #134f5c; }

.box {
    padding: 20px; border-radius: 20px;
    background: rgba(217, 234, 211, 0.9);
    margin-bottom: 20px; backdrop-filter: blur(5px);
}
.box2 {
    padding: 20px; border-radius: 20px;
    background: rgba(207, 226, 243, 0.9);
    margin-bottom: 20px; backdrop-filter: blur(5px);
}
.box3 {
    padding: 20px; border-radius: 20px;
    background: rgba(252, 229, 205, 0.9);
    margin-bottom: 20px; backdrop-filter: blur(5px);
}
.ph-box {
    padding: 25px; border-radius: 20px;
    background: linear-gradient(to right, #fff3cd, #ffe599);
    text-align: center; font-size: 26px; font-weight: bold;
    color: #7f6000; margin-top: 20px;
    box-shadow: 0px 0px 15px rgba(0,0,0,0.2);
}

/* Kotak langkah rumus */
.step-box {
    padding: 18px 22px; border-radius: 16px;
    background: rgba(235, 245, 255, 0.95);
    border-left: 5px solid #3c78d8;
    margin-top: 18px; font-size: 15px;
    line-height: 2;
}
.step-box h4 { color: #0b5394; margin-bottom: 8px; font-size: 17px; }
.step-box code {
    background: rgba(255,255,255,0.8);
    padding: 2px 8px; border-radius: 6px;
    font-size: 14px; color: #1a1a2e;
}

.stButton>button {
    background: linear-gradient(to right, #0b5394, #3c78d8);
    color: white; border-radius: 15px; height: 50px;
    font-size: 18px; border: none;
}
section[data-testid="stSidebar"] {
    background: linear-gradient(to bottom, #dbeafe, #b6d7ff);
}
.stNumberInput, .stSelectbox {
    background-color: rgba(255,255,255,0.85);
    border-radius: 10px; padding: 5px;
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
    "HCl": ("Asam Kuat", 1),
    "HBr": ("Asam Kuat", 1),
    "HI": ("Asam Kuat", 1),
    "HNO3": ("Asam Kuat", 1),
    "HClO4": ("Asam Kuat", 1),
    "H2SO4": ("Asam Kuat", 2),
    "CH3COOH": ("Asam Lemah", 1.8e-5),
    "HF": ("Asam Lemah", 6.8e-4),
    "HCN": ("Asam Lemah", 6.2e-10),
    "HCOOH": ("Asam Lemah", 1.8e-4),
    "H2CO3": ("Asam Lemah", 4.3e-7),
    "H3PO4": ("Asam Lemah", 7.1e-3),
    "H2S": ("Asam Lemah", 1.0e-7),
    "C6H5COOH": ("Asam Lemah", 6.3e-5),
    "HNO2": ("Asam Lemah", 4.5e-4),
    "NaOH": ("Basa Kuat", 1),
    "KOH": ("Basa Kuat", 1),
    "LiOH": ("Basa Kuat", 1),
    "Ca(OH)2": ("Basa Kuat", 2),
    "Ba(OH)2": ("Basa Kuat", 2),
    "Sr(OH)2": ("Basa Kuat", 2),
    "NH3": ("Basa Lemah", 1.8e-5),
    "NH4OH": ("Basa Lemah", 1.8e-5),
    "CH3NH2": ("Basa Lemah", 4.4e-4),
    "(CH3)2NH": ("Basa Lemah", 5.4e-4),
    "C5H5N": ("Basa Lemah", 1.7e-9),
    "CH3COOH + CH3COONa": ("Buffer Asam", 1.8e-5),
    "HF + NaF": ("Buffer Asam", 6.8e-4),
    "HCOOH + HCOONa": ("Buffer Asam", 1.8e-4),
    "H2CO3 + NaHCO3": ("Buffer Asam", 4.3e-7),
    "NH3 + NH4Cl": ("Buffer Basa", 1.8e-5),
    "NH4OH + NH4NO3": ("Buffer Basa", 1.8e-5),
    "CH3NH2 + CH3NH3Cl": ("Buffer Basa", 4.4e-4),
}

# =========================================================
# BERANDA
# =========================================================
if menu == "🏠 Beranda":
    st.title("🧪 KALKULATOR pH LARUTAN")
    st.image("https://cdn-icons-png.flaticon.com/512/2784/2784487.png", width=220)
    st.markdown("""
    <div class='box'>
    <h2>👋 Selamat Datang</h2>
    <p>Aplikasi ini digunakan untuk membantu menghitung pH larutan secara cepat, mudah, dan interaktif.</p>
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
    with col1: st.error("🟥 pH 0 - 6 = ASAM")
    with col2: st.warning("🟨 pH 7 = NETRAL")
    with col3: st.success("🟦 pH 8 - 14 = BASA")

# =========================================================
# MASUKKAN DATA
# =========================================================
elif menu == "🧪 Masukkan Data":
    st.title("🧪 ANALISIS LARUTAN")
    pilihan = st.selectbox("Pilih Rumus Kimia", list(data_larutan.keys()))
    konsentrasi = st.number_input("Masukkan Konsentrasi (M)", min_value=0.0001, value=0.1)

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
        🧪 HASIL ANALISIS<br><br>
        Rumus Kimia : {pilihan}<br>
        Jenis Larutan : {jenis}<br>
        pH = {round(ph,2)}
        </div>
        """, unsafe_allow_html=True)

# =========================================================
# PERHITUNGAN pH  ← DIUBAH: tampilkan langkah rumus
# =========================================================
elif menu == "🧮 Perhitungan pH":
    st.title("🧮 PERHITUNGAN pH")

    jenis = st.selectbox(
        "Pilih Jenis Larutan",
        ["Asam Kuat", "Asam Lemah", "Basa Kuat", "Basa Lemah", "Buffer Asam", "Buffer Basa"]
    )

    molaritas = st.number_input("Molaritas (M)", value=0.1, format="%.4f")
    ka = st.number_input("Ka", value=1.8e-5, format="%.10f")
    kb = st.number_input("Kb", value=1.8e-5, format="%.10f")

    # Input tambahan buffer (ditampilkan selalu agar tidak error saat hitung)
    asam_buf  = st.number_input("Konsentrasi Asam (untuk Buffer Asam)", value=0.1, format="%.4f")
    garam_buf = st.number_input("Konsentrasi Garam / Basa (untuk Buffer)", value=0.1, format="%.4f")

    if st.button("🧪 HITUNG pH"):
        ph = None
        langkah_html = ""

        # ---------- ASAM KUAT ----------
        if jenis == "Asam Kuat":
            ph = -math.log10(molaritas)
            langkah_html = f"""
            <div class='step-box'>
                <h4>📐 Langkah Perhitungan — Asam Kuat</h4>
                <b>Rumus:</b> pH = −log[H⁺]<br>
                <b>Karena asam kuat terionisasi sempurna:</b><br>
                &nbsp;&nbsp;[H⁺] = Molaritas = <code>{molaritas:.4f} M</code><br><br>
                <b>Substitusi:</b><br>
                &nbsp;&nbsp;pH = −log(<code>{molaritas:.4f}</code>)<br>
                &nbsp;&nbsp;pH = −(<code>{math.log10(molaritas):.4f}</code>)<br>
                &nbsp;&nbsp;<b>pH = {round(ph, 2)}</b>
            </div>
            """

        # ---------- ASAM LEMAH ----------
        elif jenis == "Asam Lemah":
            h = math.sqrt(ka * molaritas)
            ph = -math.log10(h)
            langkah_html = f"""
            <div class='step-box'>
                <h4>📐 Langkah Perhitungan — Asam Lemah</h4>
                <b>Rumus:</b> [H⁺] = √(Ka × C) &nbsp;→&nbsp; pH = −log[H⁺]<br><br>
                <b>Diketahui:</b><br>
                &nbsp;&nbsp;Ka = <code>{ka:.2e}</code><br>
                &nbsp;&nbsp;C  = <code>{molaritas:.4f} M</code><br><br>
                <b>Langkah 1 — Hitung [H⁺]:</b><br>
                &nbsp;&nbsp;[H⁺] = √({ka:.2e} × {molaritas:.4f})<br>
                &nbsp;&nbsp;[H⁺] = √(<code>{ka * molaritas:.2e}</code>)<br>
                &nbsp;&nbsp;[H⁺] = <code>{h:.4e} M</code><br><br>
                <b>Langkah 2 — Hitung pH:</b><br>
                &nbsp;&nbsp;pH = −log(<code>{h:.4e}</code>)<br>
                &nbsp;&nbsp;<b>pH = {round(ph, 2)}</b>
            </div>
            """

        # ---------- BASA KUAT ----------
        elif jenis == "Basa Kuat":
            poh = -math.log10(molaritas)
            ph  = 14 - poh
            langkah_html = f"""
            <div class='step-box'>
                <h4>📐 Langkah Perhitungan — Basa Kuat</h4>
                <b>Rumus:</b> pOH = −log[OH⁻] &nbsp;→&nbsp; pH = 14 − pOH<br>
                <b>Karena basa kuat terionisasi sempurna:</b><br>
                &nbsp;&nbsp;[OH⁻] = Molaritas = <code>{molaritas:.4f} M</code><br><br>
                <b>Langkah 1 — Hitung pOH:</b><br>
                &nbsp;&nbsp;pOH = −log(<code>{molaritas:.4f}</code>)<br>
                &nbsp;&nbsp;pOH = <code>{round(poh, 4)}</code><br><br>
                <b>Langkah 2 — Hitung pH:</b><br>
                &nbsp;&nbsp;pH = 14 − <code>{round(poh, 4)}</code><br>
                &nbsp;&nbsp;<b>pH = {round(ph, 2)}</b>
            </div>
            """

        # ---------- BASA LEMAH ----------
        elif jenis == "Basa Lemah":
            oh  = math.sqrt(kb * molaritas)
            poh = -math.log10(oh)
            ph  = 14 - poh
            langkah_html = f"""
            <div class='step-box'>
                <h4>📐 Langkah Perhitungan — Basa Lemah</h4>
                <b>Rumus:</b> [OH⁻] = √(Kb × C) &nbsp;→&nbsp; pOH = −log[OH⁻] &nbsp;→&nbsp; pH = 14 − pOH<br><br>
                <b>Diketahui:</b><br>
                &nbsp;&nbsp;Kb = <code>{kb:.2e}</code><br>
                &nbsp;&nbsp;C  = <code>{molaritas:.4f} M</code><br><br>
                <b>Langkah 1 — Hitung [OH⁻]:</b><br>
                &nbsp;&nbsp;[OH⁻] = √({kb:.2e} × {molaritas:.4f})<br>
                &nbsp;&nbsp;[OH⁻] = √(<code>{kb * molaritas:.2e}</code>)<br>
                &nbsp;&nbsp;[OH⁻] = <code>{oh:.4e} M</code><br><br>
                <b>Langkah 2 — Hitung pOH:</b><br>
                &nbsp;&nbsp;pOH = −log(<code>{oh:.4e}</code>)<br>
                &nbsp;&nbsp;pOH = <code>{round(poh, 4)}</code><br><br>
                <b>Langkah 3 — Hitung pH:</b><br>
                &nbsp;&nbsp;pH = 14 − <code>{round(poh, 4)}</code><br>
                &nbsp;&nbsp;<b>pH = {round(ph, 2)}</b>
            </div>
            """

        # ---------- BUFFER ASAM ----------
        elif jenis == "Buffer Asam":
            pka = -math.log10(ka)
            ph  = pka + math.log10(garam_buf / asam_buf)
            langkah_html = f"""
            <div class='step-box'>
                <h4>📐 Langkah Perhitungan — Buffer Asam (Henderson-Hasselbalch)</h4>
                <b>Rumus:</b> pH = pKa + log([A⁻] / [HA])<br><br>
                <b>Diketahui:</b><br>
                &nbsp;&nbsp;Ka   = <code>{ka:.2e}</code><br>
                &nbsp;&nbsp;[HA] = <code>{asam_buf:.4f} M</code> (konsentrasi asam)<br>
                &nbsp;&nbsp;[A⁻] = <code>{garam_buf:.4f} M</code> (konsentrasi garam/basa konjugat)<br><br>
                <b>Langkah 1 — Hitung pKa:</b><br>
                &nbsp;&nbsp;pKa = −log(<code>{ka:.2e}</code>) = <code>{round(pka, 4)}</code><br><br>
                <b>Langkah 2 — Hitung log([A⁻]/[HA]):</b><br>
                &nbsp;&nbsp;log(<code>{garam_buf:.4f}</code> / <code>{asam_buf:.4f}</code>) = log(<code>{garam_buf/asam_buf:.4f}</code>) = <code>{round(math.log10(garam_buf/asam_buf), 4)}</code><br><br>
                <b>Langkah 3 — Hitung pH:</b><br>
                &nbsp;&nbsp;pH = <code>{round(pka, 4)}</code> + <code>{round(math.log10(garam_buf/asam_buf), 4)}</code><br>
                &nbsp;&nbsp;<b>pH = {round(ph, 2)}</b>
            </div>
            """

        # ---------- BUFFER BASA ----------
        elif jenis == "Buffer Basa":
            pkb = -math.log10(kb)
            poh = pkb + math.log10(garam_buf / asam_buf)
            ph  = 14 - poh
            langkah_html = f"""
            <div class='step-box'>
                <h4>📐 Langkah Perhitungan — Buffer Basa (Henderson-Hasselbalch)</h4>
                <b>Rumus:</b> pOH = pKb + log([BH⁺] / [B]) &nbsp;→&nbsp; pH = 14 − pOH<br><br>
                <b>Diketahui:</b><br>
                &nbsp;&nbsp;Kb    = <code>{kb:.2e}</code><br>
                &nbsp;&nbsp;[B]   = <code>{asam_buf:.4f} M</code> (konsentrasi basa)<br>
                &nbsp;&nbsp;[BH⁺] = <code>{garam_buf:.4f} M</code> (konsentrasi garam/asam konjugat)<br><br>
                <b>Langkah 1 — Hitung pKb:</b><br>
                &nbsp;&nbsp;pKb = −log(<code>{kb:.2e}</code>) = <code>{round(pkb, 4)}</code><br><br>
                <b>Langkah 2 — Hitung log([BH⁺]/[B]):</b><br>
                &nbsp;&nbsp;log(<code>{garam_buf:.4f}</code> / <code>{asam_buf:.4f}</code>) = <code>{round(math.log10(garam_buf/asam_buf), 4)}</code><br><br>
                <b>Langkah 3 — Hitung pOH:</b><br>
                &nbsp;&nbsp;pOH = <code>{round(pkb, 4)}</code> + <code>{round(math.log10(garam_buf/asam_buf), 4)}</code> = <code>{round(poh, 4)}</code><br><br>
                <b>Langkah 4 — Hitung pH:</b><br>
                &nbsp;&nbsp;pH = 14 − <code>{round(poh, 4)}</code><br>
                &nbsp;&nbsp;<b>pH = {round(ph, 2)}</b>
            </div>
            """

        # Tampilkan kotak langkah rumus
        st.markdown(langkah_html, unsafe_allow_html=True)

        # Tampilkan hasil akhir
        st.markdown(f"""
        <div class='ph-box'>
        📊 HASIL PERHITUNGAN<br><br>
        Jenis Larutan : {jenis}<br>
        pH = {round(ph, 2)}
        </div>
        """, unsafe_allow_html=True)

# =========================================================
# CAMPURAN LARUTAN  ← DIUBAH: tampilkan langkah rumus
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

    M1 = st.number_input("Molaritas Larutan 1", value=0.1, format="%.4f")
    V1 = st.number_input("Volume Larutan 1 (mL)", value=50.0)
    M2 = st.number_input("Molaritas Larutan 2", value=0.1, format="%.4f")
    V2 = st.number_input("Volume Larutan 2 (mL)", value=50.0)
    Ka = st.number_input("Ka", value=1.8e-5, format="%.10f")
    Kb = st.number_input("Kb", value=1.8e-5, format="%.10f")

    if st.button("🧪 HITUNG CAMPURAN"):
        mol1 = M1 * V1 / 1000
        mol2 = M2 * V2 / 1000
        volume_total = (V1 + V2) / 1000
        langkah_html = ""
        ph = None
        sifat = ""

        # ---------- ASAM KUAT + BASA KUAT ----------
        if tipe == "Asam Kuat + Basa Kuat":
            if mol1 > mol2:
                sisa = mol1 - mol2
                h    = sisa / volume_total
                ph   = -math.log10(h)
                sifat = "Asam"
                langkah_html = f"""
                <div class='step-box'>
                    <h4>📐 Langkah — Asam Kuat + Basa Kuat (Sisa Asam)</h4>
                    <b>Hitung mol:</b><br>
                    &nbsp;&nbsp;mol asam = {M1:.4f} × {V1:.1f}/1000 = <code>{mol1:.4f} mol</code><br>
                    &nbsp;&nbsp;mol basa = {M2:.4f} × {V2:.1f}/1000 = <code>{mol2:.4f} mol</code><br><br>
                    <b>Reaksi:</b> mol asam &gt; mol basa → sisa asam<br>
                    &nbsp;&nbsp;mol sisa H⁺ = {mol1:.4f} − {mol2:.4f} = <code>{sisa:.4f} mol</code><br><br>
                    <b>Hitung [H⁺]:</b><br>
                    &nbsp;&nbsp;[H⁺] = {sisa:.4f} / {volume_total:.4f} = <code>{h:.4e} M</code><br><br>
                    <b>Hitung pH:</b><br>
                    &nbsp;&nbsp;pH = −log(<code>{h:.4e}</code>)<br>
                    &nbsp;&nbsp;<b>pH = {round(ph, 2)}</b>
                </div>
                """
            elif mol2 > mol1:
                sisa = mol2 - mol1
                oh   = sisa / volume_total
                poh  = -math.log10(oh)
                ph   = 14 - poh
                sifat = "Basa"
                langkah_html = f"""
                <div class='step-box'>
                    <h4>📐 Langkah — Asam Kuat + Basa Kuat (Sisa Basa)</h4>
                    <b>Hitung mol:</b><br>
                    &nbsp;&nbsp;mol asam = <code>{mol1:.4f} mol</code><br>
                    &nbsp;&nbsp;mol basa = <code>{mol2:.4f} mol</code><br><br>
                    <b>Reaksi:</b> mol basa &gt; mol asam → sisa basa<br>
                    &nbsp;&nbsp;mol sisa OH⁻ = {mol2:.4f} − {mol1:.4f} = <code>{sisa:.4f} mol</code><br><br>
                    <b>Hitung [OH⁻]:</b><br>
                    &nbsp;&nbsp;[OH⁻] = {sisa:.4f} / {volume_total:.4f} = <code>{oh:.4e} M</code><br><br>
                    <b>Hitung pOH:</b><br>
                    &nbsp;&nbsp;pOH = −log(<code>{oh:.4e}</code>) = <code>{round(poh, 4)}</code><br><br>
                    <b>Hitung pH:</b><br>
                    &nbsp;&nbsp;pH = 14 − <code>{round(poh, 4)}</code><br>
                    &nbsp;&nbsp;<b>pH = {round(ph, 2)}</b>
                </div>
                """
            else:
                ph = 7
                sifat = "Netral"
                langkah_html = f"""
                <div class='step-box'>
                    <h4>📐 Langkah — Asam Kuat + Basa Kuat (Ekuivalen)</h4>
                    &nbsp;&nbsp;mol asam = mol basa = <code>{mol1:.4f} mol</code><br>
                    &nbsp;&nbsp;Reaksi sempurna → tidak ada sisa asam/basa<br>
                    &nbsp;&nbsp;Larutan bersifat <b>Netral</b><br>
                    &nbsp;&nbsp;<b>pH = 7</b>
                </div>
                """

        # ---------- ASAM LEMAH + BASA KUAT ----------
        elif tipe == "Asam Lemah + Basa Kuat":
            if mol1 > mol2:
                sisa_asam = mol1 - mol2
                garam     = mol2
                pKa       = -math.log10(Ka)
                ph        = pKa + math.log10(garam / sisa_asam)
                sifat     = "Buffer Asam"
                langkah_html = f"""
                <div class='step-box'>
                    <h4>📐 Langkah — Asam Lemah + Basa Kuat → Buffer Asam</h4>
                    <b>Hitung mol:</b><br>
                    &nbsp;&nbsp;mol asam lemah = <code>{mol1:.4f} mol</code><br>
                    &nbsp;&nbsp;mol basa kuat  = <code>{mol2:.4f} mol</code><br><br>
                    <b>Setelah reaksi:</b><br>
                    &nbsp;&nbsp;mol sisa asam = {mol1:.4f} − {mol2:.4f} = <code>{sisa_asam:.4f} mol</code><br>
                    &nbsp;&nbsp;mol garam     = <code>{garam:.4f} mol</code><br><br>
                    <b>Rumus Henderson-Hasselbalch:</b><br>
                    &nbsp;&nbsp;pKa = −log(<code>{Ka:.2e}</code>) = <code>{round(pKa, 4)}</code><br>
                    &nbsp;&nbsp;pH = pKa + log(mol garam / mol sisa asam)<br>
                    &nbsp;&nbsp;pH = {round(pKa,4)} + log(<code>{garam:.4f}</code> / <code>{sisa_asam:.4f}</code>)<br>
                    &nbsp;&nbsp;pH = {round(pKa,4)} + <code>{round(math.log10(garam/sisa_asam),4)}</code><br>
                    &nbsp;&nbsp;<b>pH = {round(ph, 2)}</b>
                </div>
                """
            else:
                sisa_oh = mol2 - mol1
                oh  = sisa_oh / volume_total
                poh = -math.log10(oh)
                ph  = 14 - poh
                sifat = "Basa"
                langkah_html = f"""
                <div class='step-box'>
                    <h4>📐 Langkah — Asam Lemah + Basa Kuat (Sisa Basa)</h4>
                    &nbsp;&nbsp;mol sisa OH⁻ = {mol2:.4f} − {mol1:.4f} = <code>{sisa_oh:.4f} mol</code><br>
                    &nbsp;&nbsp;[OH⁻] = <code>{oh:.4e} M</code><br>
                    &nbsp;&nbsp;pOH = −log(<code>{oh:.4e}</code>) = <code>{round(poh, 4)}</code><br>
                    &nbsp;&nbsp;pH = 14 − <code>{round(poh, 4)}</code><br>
                    &nbsp;&nbsp;<b>pH = {round(ph, 2)}</b>
                </div>
                """

        # ---------- BASA LEMAH + ASAM KUAT ----------
        elif tipe == "Basa Lemah + Asam Kuat":
            if mol1 > mol2:
                sisa_basa = mol1 - mol2
                garam     = mol2
                pKb       = -math.log10(Kb)
                poh       = pKb + math.log10(garam / sisa_basa)
                ph        = 14 - poh
                sifat     = "Buffer Basa"
                langkah_html = f"""
                <div class='step-box'>
                    <h4>📐 Langkah — Basa Lemah + Asam Kuat → Buffer Basa</h4>
                    <b>Hitung mol:</b><br>
                    &nbsp;&nbsp;mol basa lemah = <code>{mol1:.4f} mol</code><br>
                    &nbsp;&nbsp;mol asam kuat  = <code>{mol2:.4f} mol</code><br><br>
                    <b>Setelah reaksi:</b><br>
                    &nbsp;&nbsp;mol sisa basa = {mol1:.4f} − {mol2:.4f} = <code>{sisa_basa:.4f} mol</code><br>
                    &nbsp;&nbsp;mol garam     = <code>{garam:.4f} mol</code><br><br>
                    <b>Rumus Henderson-Hasselbalch:</b><br>
                    &nbsp;&nbsp;pKb = −log(<code>{Kb:.2e}</code>) = <code>{round(pKb, 4)}</code><br>
                    &nbsp;&nbsp;pOH = pKb + log(mol garam / mol sisa basa)<br>
                    &nbsp;&nbsp;pOH = {round(pKb,4)} + log(<code>{garam:.4f}</code> / <code>{sisa_basa:.4f}</code>)<br>
                    &nbsp;&nbsp;pOH = {round(pKb,4)} + <code>{round(math.log10(garam/sisa_basa),4)}</code> = <code>{round(poh,4)}</code><br>
                    &nbsp;&nbsp;pH = 14 − <code>{round(poh, 4)}</code><br>
                    &nbsp;&nbsp;<b>pH = {round(ph, 2)}</b>
                </div>
                """
            else:
                sisa_h = mol2 - mol1
                h   = sisa_h / volume_total
                ph  = -math.log10(h)
                sifat = "Asam"
                langkah_html = f"""
                <div class='step-box'>
                    <h4>📐 Langkah — Basa Lemah + Asam Kuat (Sisa Asam)</h4>
                    &nbsp;&nbsp;mol sisa H⁺ = {mol2:.4f} − {mol1:.4f} = <code>{sisa_h:.4f} mol</code><br>
                    &nbsp;&nbsp;[H⁺] = <code>{h:.4e} M</code><br>
                    &nbsp;&nbsp;pH = −log(<code>{h:.4e}</code>)<br>
                    &nbsp;&nbsp;<b>pH = {round(ph, 2)}</b>
                </div>
                """

        # ---------- GARAM DARI ASAM LEMAH (HIDROLISIS) ----------
        elif tipe == "Garam dari Asam Lemah":
            konsentrasi_garam = mol1 / volume_total
            Kw  = 1e-14
            Kb_eff = Kw / Ka
            oh  = math.sqrt(Kb_eff * konsentrasi_garam)
            poh = -math.log10(oh)
            ph  = 14 - poh
            sifat = "Basa"
            langkah_html = f"""
            <div class='step-box'>
                <h4>📐 Langkah — Garam dari Asam Lemah (Hidrolisis)</h4>
                <b>Garam dari asam lemah bersifat basa (hidrolisis anion)</b><br><br>
                <b>Hitung konsentrasi garam:</b><br>
                &nbsp;&nbsp;C = mol / V total = {mol1:.4f} / {volume_total:.4f} = <code>{konsentrasi_garam:.4f} M</code><br><br>
                <b>Hitung Kb hidrolisis:</b><br>
                &nbsp;&nbsp;Kb = Kw / Ka = 1×10⁻¹⁴ / <code>{Ka:.2e}</code> = <code>{Kb_eff:.4e}</code><br><br>
                <b>Hitung [OH⁻]:</b><br>
                &nbsp;&nbsp;[OH⁻] = √(Kb × C) = √(<code>{Kb_eff:.4e}</code> × <code>{konsentrasi_garam:.4f}</code>)<br>
                &nbsp;&nbsp;[OH⁻] = √(<code>{Kb_eff * konsentrasi_garam:.4e}</code>)<br>
                &nbsp;&nbsp;[OH⁻] = <code>{oh:.4e} M</code><br><br>
                <b>Hitung pOH:</b><br>
                &nbsp;&nbsp;pOH = −log(<code>{oh:.4e}</code>) = <code>{round(poh, 4)}</code><br><br>
                <b>Hitung pH:</b><br>
                &nbsp;&nbsp;pH = 14 − <code>{round(poh, 4)}</code><br>
                &nbsp;&nbsp;<b>pH = {round(ph, 2)}</b>
            </div>
            """

        # Tampilkan langkah rumus
        st.markdown(langkah_html, unsafe_allow_html=True)

        # Tampilkan hasil akhir
        st.markdown(f"""
        <div class='ph-box'>
        ⚗️ HASIL CAMPURAN<br><br>
        pH = {round(ph, 2)}<br>
        Sifat Larutan = {sifat}
        </div>
        """, unsafe_allow_html=True)

        st.write(f"Mol larutan 1 = {mol1:.4f} mol")
        st.write(f"Mol larutan 2 = {mol2:.4f} mol")
        st.write(f"Volume total  = {volume_total:.4f} L")

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

    st.success("🧪 Aplikasi dibuat untuk membantu pembelajaran kimia.")
