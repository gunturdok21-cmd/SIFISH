import streamlit as st
import pandas as pd
import plotly.express as px
from io import StringIO   # ← tambahkan ini

# Konfigurasi halaman
st.set_page_config(
    page_title="Aplikasi Penilaian TRL",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Minimum skor untuk melanjutkan (70%)
MIN_SCORE_THRESHOLD = 0.7

def main():
    # Inisialisasi session state
    initialize_session_state()
    st.title("📊 Sistem Informasi Penangkapan Ikan Secara Real-Time Berbasis Satelit dan IoT (SIFISH)")
   # st.write("SIFSH")

    # Style tambahan
    st.markdown("""
    <style>
    .warning-box {
        background-color: #fff3cd;
        border-radius: 0.5rem;
        padding: 1rem;
        margin-bottom: 1rem;
    }
    .success-box {
        background-color: #d4edda;
        border-radius: 0.5rem;
        padding: 1rem;
        margin-bottom: 1rem;
    }
    .locked-level {
        color: #ff0000;
        font-weight: bold;
    }
    .next-button {
        margin-top: 1rem;
        padding: 0.5rem 1rem;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

    with st.sidebar:
        st.header("Navigasi")
        page_options = get_page_options()
       # page = st.radio("Pilih halaman:", page_options, key="navigation")
        page = st.radio("Pencarian:", page_options, key="navigation")
        # Tampilkan status penyelesaian
       # st.markdown("### Progress Penilaian")

        #for i in range(1, 10):
        #    score = st.session_state.get(f'trl_{i}_score', 0)
        #    max_score = st.session_state.get(f'trl_{i}_max', 1)
        #    progress = score / max_score if max_score > 0 else 0
        #    status = "✅" if progress >= MIN_SCORE_THRESHOLD else "❌"
        #    st.caption(f"{status} TRL {i}: {progress:.0%}")

    if page == "Profil Organisasi":
        show_organization_profile()
    #elif get_page_options == "Hasil Penilaian":
    elif page == "Hasil Penilaian":
        # page == "Hasil Penilaian":
        show_hasil_penilaian()
    else:
        #trl_level = int(page.split(":")[0].split(" ")[1])
        #show_trl_assessment(trl_level)
        show_halaman_lain()

def initialize_session_state():
    """Inisialisasi semua variabel session state yang diperlukan"""
    if 'organization_info' not in st.session_state:
        st.session_state.organization_info = {}
    for i in range(1, 10):
        if f'trl_{i}_score' not in st.session_state:
            st.session_state[f'trl_{i}_score'] = 0
        if f'trl_{i}_max' not in st.session_state:
            st.session_state[f'trl_{i}_max'] = 0
        if f'trl_{i}_locked' not in st.session_state:
            # TRL 1 tidak pernah dikunci, lainnya dikunci secara default
            st.session_state[f'trl_{i}_locked'] = i != 1

def get_page_options():
    """Generate opsi halaman dengan status kunci berdasarkan penyelesaian"""
    pages = [
        "Profil Organisasi",
        "1: Provinsi",
        "2: Kabupaten",
        "3: Kota"

       # "TRL 1: Prinsip Dasar",
       # "TRL 2: Konsep Teknologi",
       # "TRL 3: Validasi Analitis",
       # "TRL 4: Validasi Lab",
       # "TRL 5: Lingkungan Relevan",
       # "TRL 6: Demo Prototipe",
       # "TRL 7: Demo Operasional",
       # "TRL 8: Sistem Lengkap",
        # "TRL 9: Bukti Operasional",
        #"Hasil Penilaian"
    ]

    # Periksa TRL mana yang terbuka
    unlocked_pages = ["Profil Organisasi"]

    #for i in range(1, 10):
    #    page_name = f"TRL {i}:"
        # Periksa apakah level sebelumnya memenuhi threshold
    #    if i > 1:
    #        prev_score = st.session_state.get(f'trl_{i-1}_score', 0)
    #        prev_max = st.session_state.get(f'trl_{i-1}_max', 1)
    #        prev_progress = prev_score / prev_max if prev_max > 0 else 0
    #        if prev_progress < MIN_SCORE_THRESHOLD:
    #            st.session_state[f'trl_{i}_locked'] = True

        # Tambahkan ke halaman yang tersedia jika tidak terkunci
    #    if not st.session_state.get(f'trl_{i}_locked', True):
            #unlocked_pages.append(next(p for p in pages if p.startswith(page_name)))
    #        unlocked_pages.append(next(p for p in pages))


    unlocked_pages.append("Hasil Penilaian")
    unlocked_pages.append("Halaman Lainnya")

    return unlocked_pages

def show_hasil_penilaian():
    st.header("Hasil Penilaian")
    st.write("Silakan lengkapi informasi dasar tentang organisasi Anda.")

def show_halaman_lain():
    st.header("Halaman Lainnya")
    st.write("Halaman lain, silakan diganti dengan halaman yang sebenarnya")

def show_organization_profile():
    st.header("Profil Organisasi")
    st.write("Silakan lengkapi informasi dasar tentang organisasi Anda.")

    with st.form("org_info"):
        cols = st.columns(2)
        with cols[0]:
            name = st.text_input("Nama Organisasi",
                               value=st.session_state.organization_info.get('name', ''))
            industry = st.selectbox(
               "Industri Utama",
               ["Provinsi", "Kabupaten", "Kota"],
               # "Industri Utama",
               # ["Teknologi Informasi", "Keuangan", "Kesehatan", "Manufaktur", "Energi", "Lainnya"],
                index=0
            )
        with cols[1]:
            employees = st.number_input("Nama Provinsi/kabupaten/Kota",
                                      min_value=1,
                                      value=st.session_state.organization_info.get('employees', 10))
            country = st.text_input("Nama Penenggung Jawab:",
                                  value=st.session_state.organization_info.get('country', 'Indonesia'))

           # employees = st.number_input("Jumlah Karyawan",
           #                           min_value=1,
           #                           value=st.session_state.organization_info.get('employees', 10))
           # country = st.text_input("Negara",
           #                       value=st.session_state.organization_info.get('country', 'Indonesia'))

        submitted = st.form_submit_button("Simpan Profil")
        if submitted:
            st.session_state.organization_info = {
                'name': name,
                'industry': industry,
                'employees': employees,
                'country': country
            }
            st.success("Profil berhasil disimpan!")

def show_trl_assessment(level):
    trl_data = get_trl_data(level)
    if not trl_data or not trl_data['questions']:
        st.error(f"Data pertanyaan untuk TRL {level} tidak tersedia")
        return

    st.header(f"TRL {level}: {trl_data['title']}")
    st.caption(f"Penilaian Technology Readiness Level {level}")
    st.markdown(f"""
    **Definisi**: {trl_data['definition']}
    """)

    # Periksa apakah level ini terkunci
    if st.session_state.get(f'trl_{level}_locked', True):
        st.error(f"🔒 Level ini terkunci. Anda harus menyelesaikan TRL {level-1} dengan skor minimal {MIN_SCORE_THRESHOLD:.0%} untuk membuka.")
        if level > 1:
            prev_score = st.session_state.get(f'trl_{level-1}_score', 0)
            prev_max = st.session_state.get(f'trl_{level-1}_max', 1)
            prev_progress = prev_score / prev_max if prev_max > 0 else 0
            st.warning(f"Skor TRL {level-1} Anda {prev_progress:.0%} (perlu {MIN_SCORE_THRESHOLD:.0%} untuk membuka TRL {level})")
        return

    scores = []
    with st.form(f"trl_{level}_form"):
        st.markdown("**Pertanyaan Penilaian:**")
        for i, question in enumerate(trl_data['questions']):
            answer = st.radio(
                question,
                options=["Belum", "Sedang", "Sudah"],
                horizontal=True,
                key=f"trl_{level}_q_{i}"
            )
            scores.append(1 if answer == "Sudah" else 0)

        submitted = st.form_submit_button("Simpan Penilaian")
        if submitted:
            total_score = sum(scores)
            st.session_state[f'trl_{level}_score'] = total_score
            st.session_state[f'trl_{level}_max'] = len(trl_data['questions'])

            # Periksa apakah ini membuka level berikutnya
            progress = total_score / len(trl_data['questions'])
            if progress >= MIN_SCORE_THRESHOLD and level < 9:
                st.session_state[f'trl_{level+1}_locked'] = False
                st.success(f"Penilaian TRL {level} disimpan! ✅ TRL {level+1} sekarang terbuka!")

                # Auto redirect ke TRL berikutnya
                st.session_state.auto_redirect = level + 1
                st.rerun()
            else:
                st.success(f"Penilaian TRL {level} disimpan! Skor: {total_score}/{len(trl_data['questions'])}")

    # Tampilkan progress saat ini
    current_score = st.session_state[f'trl_{level}_score']
    max_score = st.session_state[f'trl_{level}_max']
    if max_score > 0:
        progress = current_score / max_score
        st.progress(progress, text=f"Penyelesaian: {progress:.0%}")

        # Periksa auto redirect
        if st.session_state.get('auto_redirect') == level:
            st.session_state['auto_redirect'] = None
            next_level = level + 1
            st.info(f"Melanjutkan ke TRL {next_level}...")
            st.session_state.current_page = f"TRL {next_level}: {get_trl_data(next_level)['title']}"
            st.rerun()

        # Tombol untuk melanjutkan ke level berikutnya jika memenuhi syarat
        if progress >= MIN_SCORE_THRESHOLD and level < 9:
            st.markdown(f'<div class="success-box">🎉 Anda telah mencapai skor minimal untuk melanjutkan!</div>', unsafe_allow_html=True)
            # Tombol untuk melanjutkan ke level berikutnya
            if st.button(f"Lanjutkan ke TRL {level+1}", key=f"next_{level}",
                        help="Klik untuk melanjutkan ke level berikutnya",
                        type="primary"):
                # Update halaman yang aktif
                st.session_state['current_page'] = f"TRL {level+1}: {get_trl_data(level+1)['title']}"
                st.rerun()
        elif progress > 0:
            st.markdown(f'<div class="warning-box">⚠️ Anda membutuhkan skor {MIN_SCORE_THRESHOLD:.0%} untuk membuka level berikutnya</div>', unsafe_allow_html=True)

def show_results():
    st.header("Hasil Penilaian TRL")

    # Tampilkan nama organisasi
    org_name = st.session_state.organization_info.get('name', 'Organisasi Belum Didaftarkan')
    st.subheader(f"Organisasi: {org_name}")

    if not any(st.session_state.get(f'trl_{i}_max', 0) > 0 for i in range(1, 10)):
        st.warning("Belum ada data penilaian. Silakan lengkapi setidaknya satu penilaian TRL.")
        return

    # Hitung skor
    results = []
    total_score = 0
    total_max = 0
    for i in range(1, 10):
        score = st.session_state.get(f'trl_{i}_score', 0)
        max_score = st.session_state.get(f'trl_{i}_max', 0)
        if max_score > 0:
            percentage = (score / max_score) * 100
            meets_threshold = percentage >= (MIN_SCORE_THRESHOLD * 100)
            results.append({
                "Level TRL": f"TRL {i}",
                "Skor": f"{score}/{max_score}",
                "Persentase": percentage,
                "Status": "✅ Lengkap" if meets_threshold else "❌ Belum Lengkap",
                "Deskripsi": get_trl_definition(i)
            })
            total_score += score
            total_max += max_score

    overall = (total_score / total_max) * 100 if total_max > 0 else 0

    # Tampilkan metrik ringkasan
    cols = st.columns(3)
    with cols[0]:
        st.metric("Skor TRL Keseluruhan", f"{overall:.1f}%")
    with cols[1]:
        completed = sum(1 for r in results if r["Status"] == "✅ Lengkap")
        st.metric("Level yang Lengkap", f"{completed}/9")
    with cols[2]:
        current_level = max([int(r['Level TRL'].split(" ")[1]) for r in results if r['Persentase'] >= (MIN_SCORE_THRESHOLD * 100)] or [0])
        st.metric("Level TRL Saat Ini", f"TRL {current_level}")

    # Visualisasi
    tab1, tab2 = st.tabs(["Diagram Radar", "Hasil Detail"])

    with tab1:
        df = pd.DataFrame(results)
        fig = px.line_polar(
            df,
            r="Persentase",
            theta="Level TRL",
            line_close=True,
            range_r=[0, 100],
            title="Progress Penilaian TRL",
            color_discrete_sequence=["green" if x >= (MIN_SCORE_THRESHOLD * 100) else "red" for x in df["Persentase"]]
        )
        fig.update_traces(fill='toself')
        st.plotly_chart(fig, use_container_width=True)

    with tab2:
        st.dataframe(
            pd.DataFrame(results),
            column_config={
                "Persentase": st.column_config.ProgressColumn(
                    "Progress",
                    format="%.1f%%",
                    min_value=0,
                    max_value=100
                )
            },
            hide_index=True,
            use_container_width=True
        )

    # Rekomendasi
    st.subheader("Rekomendasi Pengembangan")
    if current_level == 9:
        st.success("Teknologi Anda sudah matang sepenuhnya! Fokus pada optimasi dan scaling.")
    elif current_level > 0:
        st.info(f"Teknologi Anda saat ini berada pada TRL {current_level}. Fokus pada:")
        st.write(get_trl_recommendations(current_level))
        # Tampilkan persyaratan level berikutnya jika belum lengkap
        if current_level < 9:
            next_level = current_level + 1
            if next_level in [int(r['Level TRL'].split(" ")[1]) for r in results]:
                st.warning(f"Untuk membuka TRL {next_level}, Anda perlu mencapai skor minimal {MIN_SCORE_THRESHOLD:.0%} pada TRL {current_level}")

def get_trl_data(level):
    """Return data pertanyaan dan metadata untuk setiap level TRL"""
    trl_db = {
        1: {
            "title": "Prinsip Dasar Diamati",
            "questions": [
                "Apakah prinsip ilmiah dasar sudah diamati dan didokumentasikan?",
                "Apakah ada penelitian yang mendukung prinsip dasar tersebut?",
                "Apakah tinjauan literatur awal sudah diselesaikan?",
                "Apakah fenomena dasar sudah dipahami secara teoritis?"
            ],
            "definition": get_trl_definition(1)
        },
        2: {
            "title": "Konsep Teknologi Diformulasikan",
            "questions": [
                "Apakah konsep teknologi sudah diformulasikan berdasarkan prinsip-prinsip tersebut?",
                "Apakah aplikasi potensial sudah diidentifikasi?",
                "Apakah diagram konseptual atau model sudah dibuat?",
                "Apakah keunggulan dibanding solusi existing sudah didokumentasikan?"
            ],
            "definition": get_trl_definition(2)
        },
        3: {
            "title": "Validasi Analitis Komponen",
            "questions": [
                "Apakah validasi analitis atau komputasional dari karakteristik teknologi sudah dilakukan?",
                "Apakah dilakukan melalui simulasi, pemodelan, atau analisis teoritis?",
                "Apakah komponen atau subsistem kecil sudah diverifikasi secara teoritis?",
                "Apakah hasil analisis menunjukkan bukti konsep yang valid?"
            ],
            "definition": get_trl_definition(3)
        },
        4: {
            "title": "Validasi di Lingkungan Laboratorium",
            "questions": [
                "Apakah pengujian eksperimental sudah dilakukan di lingkungan terkontrol?",
                "Apakah komponen atau subsistem kecil sudah diuji secara nyata di lab?",
                "Apakah validasi eksperimental dari hasil analitis sebelumnya sudah dilakukan?",
                "Apakah hasil lab mendukung kelayakan teknologi?"
            ],
            "definition": get_trl_definition(4)
        },
        5: {
            "title": "Validasi di Lingkungan Relevan",
            "questions": [
                "Apakah pengujian sudah dilakukan di lingkungan yang mendekati kondisi nyata?",
                "Apakah komponen atau subsistem sudah diuji dalam kondisi operasional yang direpresentasikan?",
                "Apakah validasi kemampuan teknologi dalam menghadapi kondisi sebenarnya sudah dilakukan?",
                "Apakah teknologi menunjukkan performa yang memadai di lingkungan relevan?"
            ],
            "definition": get_trl_definition(5)
        },
        6: {
            "title": "Demonstrasi Model/Prototipe",
            "questions": [
                "Apakah prototipe sistem lengkap sudah diuji di lingkungan yang relevan?",
                "Apakah sistem sudah diintegrasikan dan diuji sebagai kesatuan?",
                "Apakah demonstrasi kemampuan sistem secara menyeluruh sudah dilakukan?",
                "Apakah prototipe menunjukkan fungsionalitas inti yang diharapkan?"
            ],
            "definition": get_trl_definition(6)
        },
        7: {
            "title": "Demonstrasi Prototipe Operasional",
            "questions": [
                "Apakah prototipe akhir sudah diuji di lingkungan operasional nyata?",
                "Apakah sistem sudah diuji dalam kondisi sebenarnya di tempat penggunaannya?",
                "Apakah validasi kesiapan untuk produksi atau implementasi sudah dilakukan?",
                "Apakah prototipe berfungsi dengan baik di lingkungan operasional?"
            ],
            "definition": get_trl_definition(7)
        },
        8: {
            "title": "Sistem Lengkap dan Terbukti",
            "questions": [
                "Apakah sistem sebenarnya sudah selesai dikembangkan dan diuji?",
                "Apakah sudah melalui pengujian menyeluruh dan terbukti berfungsi?",
                "Apakah siap untuk produksi massal atau implementasi luas?",
                "Apakah semua dokumentasi dan pelatihan sudah disiapkan?"
            ],
            "definition": get_trl_definition(8)
        },
        9: {
            "title": "Sistem Terbukti Beroperasi",
            "questions": [
                "Apakah teknologi sudah digunakan secara operasional dan sukses?",
                "Apakah ada bukti dokumentasi operasi yang sukses?",
                "Apakah semua parameter operasional sudah divalidasi?",
                "Apakah teknologi sudah digunakan oleh pelanggan akhir?",
                "Apakah ada rekam jejak kinerja yang terbukti?"
            ],
            "definition": get_trl_definition(9)
        }
    }
    return trl_db.get(level, {"title": "", "questions": [], "definition": ""})

def get_trl_definition(level):
    definitions = {
        1: "Prinsip dasar diamati dan dilaporkan.",
        2: "Konsep teknologi dan/atau aplikasi diformulasikan.",
        3: "Bukti konsep fungsi kritis secara analitis dan eksperimental.",
        4: "Validasi komponen dan/atau breadboard di lingkungan laboratorium.",
        5: "Validasi komponen dan/atau breadboard di lingkungan yang relevan.",
        6: "Demonstrasi model/subsistem atau prototipe di lingkungan relevan.",
        7: "Demonstrasi prototipe sistem di lingkungan operasional.",
        8: "Sistem aktual selesai dan memenuhi kualifikasi melalui pengujian.",
        9: "Sistem aktual terbukti melalui operasi misi yang sukses."
    }
    return definitions.get(level, "Definisi tidak tersedia.")

def get_trl_recommendations(current_level):
    recommendations = {
        1: "Lakukan lebih banyak penelitian fundamental untuk memahami prinsip dasar.",
        2: "Kembangkan konsep teknologi detail dan identifikasi aplikasi potensial.",
        3: "Lakukan validasi analitis dan eksperimen bukti konsep.",
        4: "Mulai pengujian laboratorium untuk komponen dan subsistem.",
        5: "Uji komponen dalam lingkungan yang mensimulasikan kondisi dunia nyata.",
        6: "Kembangkan dan demonstrasikan prototipe kerja di lingkungan relevan.",
        7: "Demonstrasikan prototipe dalam kondisi operasional aktual.",
        8: "Selesaikan pengembangan sistem penuh dan pengujian kualifikasi.",
        9: "Fokus pada optimasi operasional dan scaling untuk deployment."
    }
    next_steps = recommendations.get(current_level, "Lanjutkan dengan jalur pengembangan saat ini.")
    if current_level < 9:
        next_level = current_level + 1
        next_goal = f"\nTujuan berikutnya (TRL {next_level}): {get_trl_definition(next_level)}"
        return next_steps + next_goal
    return next_steps

if __name__ == "__main__":
    main()
    # By cahyonno
