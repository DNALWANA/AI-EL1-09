#BAGIAN 1 INISIASI RULE ATAU ATURAN UNTUK PERBANDINGAN DENGAN DATA INPUT DARI USER


class Rule:
    """Merepresentasikan aturan IF-THEN dalam Knowledge Base."""

    def __init__(self, rule_id, name, conditions, conclusion, explanation):
        self.rule_id = rule_id
        self.name = name
        self.conditions = conditions
        self.conclusion = conclusion
        self.explanation = explanation


class ExpertSystemBelajar:
    def __init__(self):
        # Working Memory: fakta awal dan kesimpulan yang dihasilkan.
        self.facts = set()
        self.fact_sources = {}
        self.trace = []
        self.fired_rules = set()

        # Knowledge Base: kumpulan aturan IF-THEN.
        self.rules = [
            # Aturan untuk mengenali kebutuhan belajar.
            Rule(
                "R01", "Kesulitan memahami konsep",
                ["difficulty_concept"],
                "need_concept_understanding",
                "Pengguna mengalami kesulitan memahami konsep."
            ),
            Rule(
                "R02", "Kesulitan mengerjakan soal",
                ["difficulty_practice"],
                "need_problem_solving",
                "Pengguna mengalami kesulitan menerapkan materi."
            ),
            Rule(
                "R03", "Waktu belajar terbatas",
                ["time_limited"],
                "need_efficient_method",
                "Waktu belajar yang tersedia terbatas."
            ),
            Rule(
                "R04", "Target nilai tinggi",
                ["target_high"],
                "need_intensive_practice",
                "Pengguna memiliki target nilai yang tinggi."
            ),
            Rule(
                "R05", "Materi mudah terlupakan",
                ["often_forget"],
                "need_memory_retention",
                "Pengguna membutuhkan strategi untuk mengingat materi."
            ),
            Rule(
                "R06", "Belajar menjelang ujian",
                ["exam_soon"],
                "need_exam_preparation",
                "Pengguna perlu mempersiapkan ujian dalam waktu dekat."
            ),
            Rule(
                "R07", "Menyukai belajar visual",
                ["prefer_visual"],
                "visual_preference",
                "Pengguna lebih menyukai bantuan visual."
            ),
            Rule(
                "R08", "Menyukai belajar mandiri",
                ["prefer_solo"],
                "independent_preference",
                "Pengguna lebih nyaman belajar mandiri."
            ),
            Rule(
                "R09", "Menyukai diskusi",
                ["prefer_group"],
                "collaborative_preference",
                "Pengguna menyukai proses belajar bersama."
            ),

            # Aturan untuk memilih metode belajar.
            Rule(
                "R10", "Rekomendasi active recall",
                ["need_memory_retention"],
                "method_active_recall",
                "Active recall membantu melatih pengambilan informasi dari ingatan."
            ),
            Rule(
                "R11", "Rekomendasi spaced repetition",
                ["need_memory_retention"],
                "method_spaced_repetition",
                "Pengulangan dengan jeda membantu menjaga ingatan dalam jangka panjang."
            ),
            Rule(
                "R12", "Rekomendasi latihan soal",
                ["need_problem_solving"],
                "method_practice",
                "Latihan soal membantu menerapkan konsep dan mengevaluasi pemahaman."
            ),
            Rule(
                "R13", "Rekomendasi latihan intensif",
                ["need_intensive_practice"],
                "method_practice",
                "Latihan bertahap membantu mengevaluasi kesiapan mencapai target."
            ),
            Rule(
                "R14", "Rekomendasi belajar terstruktur",
                ["need_efficient_method"],
                "method_study_plan",
                "Jadwal terstruktur membantu memprioritaskan waktu yang terbatas."
            ),
            Rule(
                "R15", "Rekomendasi simulasi ujian",
                ["need_exam_preparation"],
                "method_mock_exam",
                "Simulasi ujian membantu melatih manajemen waktu dan kesiapan."
            ),
            Rule(
                "R16", "Rekomendasi peta konsep",
                ["need_concept_understanding", "visual_preference"],
                "method_concept_map",
                "Peta konsep membantu menghubungkan ide dan konsep secara visual."
            ),
            Rule(
                "R17", "Rekomendasi penjelasan ulang",
                ["need_concept_understanding"],
                "method_feynman",
                "Menjelaskan materi dengan bahasa sendiri membantu menguji pemahaman."
            ),
            Rule(
                "R18", "Rekomendasi belajar mandiri",
                ["independent_preference"],
                "method_solo_study",
                "Belajar mandiri sesuai dengan preferensi pengguna."
            ),
            Rule(
                "R19", "Rekomendasi diskusi kelompok",
                ["collaborative_preference"],
                "method_group_discussion",
                "Diskusi memungkinkan pertukaran penjelasan dan sudut pandang."
            ),
        ]

        # Penjelasan metode yang ditampilkan kepada pengguna.
        self.method_details = {
            "method_active_recall": (
                "Active recall",
                "Tutup catatan, lalu jawab pertanyaan dari ingatan."
            ),
            "method_spaced_repetition": (
                "Spaced repetition",
                "Ulangi materi pada beberapa sesi dengan jeda."
            ),
            "method_practice": (
                "Latihan soal",
                "Kerjakan soal dari tingkat dasar hingga menantang."
            ),
            "method_study_plan": (
                "Jadwal belajar terstruktur",
                "Bagi waktu berdasarkan prioritas dan tingkat kesulitan."
            ),
            "method_mock_exam": (
                "Simulasi ujian",
                "Kerjakan soal dalam batas waktu seperti ujian sebenarnya."
            ),
            "method_concept_map": (
                "Peta konsep",
                "Gambarkan hubungan antarkonsep menggunakan cabang dan kata kunci."
            ),
            "method_feynman": (
                "Teknik Feynman",
                "Jelaskan materi dengan bahasa sederhana seolah mengajar orang lain."
            ),
            "method_solo_study": (
                "Belajar mandiri",
                "Pelajari materi secara individual dan evaluasi pemahaman sendiri."
            ),
            "method_group_discussion": (
                "Diskusi kelompok",
                "Bandingkan jawaban, bertukar penjelasan, dan bahas soal bersama."
            ),
        }

