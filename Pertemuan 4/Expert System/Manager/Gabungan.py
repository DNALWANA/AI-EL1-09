

class Rule:
    """Aturan IF-THEN dalam Knowledge Base."""

    def __init__(self, rule_id, name, conditions, conclusion, explanation):
        self.rule_id = rule_id
        self.name = name
        self.conditions = conditions
        self.conclusion = conclusion
        self.explanation = explanation


class ExpertSystemBelajar:
    def __init__(self):
        # Working Memory
        self.facts = set()
        self.fact_sources = {}
        self.trace = []
        self.fired_rules = set()

        # Knowledge Base: IF seluruh conditions terpenuhi, THEN conclusion.
        self.rules = [
            Rule("R01", "Kesulitan memahami konsep",
                 ["difficulty_concept"], "need_concept_understanding",
                 "Pengguna mengalami kesulitan memahami konsep."),
            Rule("R02", "Kesulitan mengerjakan soal",
                 ["difficulty_practice"], "need_problem_solving",
                 "Pengguna mengalami kesulitan menerapkan materi."),
            Rule("R03", "Waktu belajar terbatas",
                 ["time_limited"], "need_efficient_method",
                 "Waktu belajar yang tersedia terbatas."),
            Rule("R04", "Target nilai tinggi",
                 ["target_high"], "need_intensive_practice",
                 "Pengguna memiliki target nilai yang tinggi."),
            Rule("R05", "Materi mudah terlupakan",
                 ["often_forget"], "need_memory_retention",
                 "Pengguna membutuhkan strategi mengingat materi."),
            Rule("R06", "Ujian dalam waktu dekat",
                 ["exam_soon"], "need_exam_preparation",
                 "Pengguna perlu mempersiapkan ujian dalam waktu dekat."),
            Rule("R07", "Preferensi visual",
                 ["prefer_visual"], "visual_preference",
                 "Pengguna menyukai bantuan visual."),
            Rule("R08", "Preferensi belajar mandiri",
                 ["prefer_solo"], "independent_preference",
                 "Pengguna lebih nyaman belajar mandiri."),
            Rule("R09", "Preferensi diskusi",
                 ["prefer_group"], "collaborative_preference",
                 "Pengguna menyukai proses belajar bersama."),

            Rule("R10", "Active recall",
                 ["need_memory_retention"], "method_active_recall",
                 "Latihan mengingat kembali dapat membantu mengevaluasi ingatan."),
            Rule("R11", "Spaced repetition",
                 ["need_memory_retention"], "method_spaced_repetition",
                 "Pengulangan dengan jeda dapat membantu retensi materi."),
            Rule("R12", "Latihan soal",
                 ["need_problem_solving"], "method_practice",
                 "Latihan soal membantu menerapkan dan mengevaluasi pemahaman."),
            Rule("R13", "Latihan untuk target tinggi",
                 ["need_intensive_practice"], "method_practice",
                 "Latihan bertahap membantu memantau kesiapan mencapai target."),
            Rule("R14", "Jadwal belajar terstruktur",
                 ["need_efficient_method"], "method_study_plan",
                 "Jadwal terstruktur membantu memprioritaskan waktu terbatas."),
            Rule("R15", "Simulasi ujian",
                 ["need_exam_preparation"], "method_mock_exam",
                 "Simulasi ujian melatih kesiapan dan pengelolaan waktu."),
            Rule("R16", "Peta konsep",
                 ["need_concept_understanding", "visual_preference"],
                 "method_concept_map",
                 "Peta konsep membantu memvisualisasikan hubungan antarkonsep."),
            Rule("R17", "Teknik Feynman",
                 ["need_concept_understanding"], "method_feynman",
                 "Menjelaskan materi dengan bahasa sendiri menguji pemahaman."),
            Rule("R18", "Belajar mandiri",
                 ["independent_preference"], "method_solo_study",
                 "Metode ini sesuai dengan preferensi belajar mandiri."),
            Rule("R19", "Diskusi kelompok",
                 ["collaborative_preference"], "method_group_discussion",
                 "Diskusi memungkinkan pertukaran penjelasan dan sudut pandang."),
        ]

        self.method_details = {
            "method_active_recall": (
                "Active recall",
                "Tutup catatan, lalu jawab pertanyaan dari ingatan."
            ),
            "method_spaced_repetition": (
                "Spaced repetition",
                "Ulangi materi dalam beberapa sesi dengan jeda."
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
                "Kerjakan soal dengan batas waktu seperti ujian sebenarnya."
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
                "Pelajari materi sendiri dan evaluasi pemahaman secara berkala."
            ),
            "method_group_discussion": (
                "Diskusi kelompok",
                "Bandingkan jawaban dan bahas soal bersama teman."
            ),
        }

    def add_fact(self, fact, source="Input pengguna"):
        """Tambahkan fakta baru dan catat asalnya."""
        if fact in self.facts:
            return False
        self.facts.add(fact)
        self.fact_sources[fact] = source
        self.trace.append({
            "type": "FACT",
            "fact": fact,
            "source": source
        })
        return True

    def forward_chaining(self):
        """Jalankan aturan sampai tidak ada fakta baru."""
        changed = True
        while changed:
            changed = False
            for rule in self.rules:
                if rule.rule_id in self.fired_rules:
                    continue
                if all(condition in self.facts for condition in rule.conditions):
                    self.fired_rules.add(rule.rule_id)
                    self.trace.append({
                        "type": "RULE",
                        "rule_id": rule.rule_id,
                        "name": rule.name,
                        "conditions": list(rule.conditions),
                        "conclusion": rule.conclusion,
                        "explanation": rule.explanation
                    })
                    if self.add_fact(rule.conclusion, f"Kesimpulan {rule.rule_id}"):
                        changed = True
        return self.facts

    @staticmethod
    def ask_choice(question, options):
        while True:
            print(question)
            for key, description in options:
                print(f"  {key}. {description}")
            answer = input("Pilih nomor: ").strip()
            if answer in [key for key, _ in options]:
                return answer
            print("Pilihan tidak valid. Silakan coba lagi.\n")

    @staticmethod
    def ask_yes_no(question):
        while True:
            answer = input(question + " (y/n): ").strip().lower()
            if answer in ("y", "ya"):
                return True
            if answer in ("n", "tidak"):
                return False
            print("Masukkan y atau n.")

    def collect_input(self):
        print("=" * 65)
        print("EXPERT SYSTEM REKOMENDASI METODE BELAJAR")
        print("Artificial Intelligence - Rule-Based Expert System")
        print("=" * 65)
        print("\nJawab pertanyaan berikut sesuai kondisi kamu.")
        print("Untuk pertanyaan ya/tidak, masukkan y atau n.\n")

        difficulty = self.ask_choice(
            "1. Kesulitan belajar yang paling sering dialami:",
            [("1", "Sulit memahami konsep"),
             ("2", "Sulit mengerjakan soal"),
             ("3", "Keduanya"),
             ("4", "Tidak ada kesulitan utama")]
        )
        if difficulty in ("1", "3"):
            self.add_fact("difficulty_concept")
        if difficulty in ("2", "3"):
            self.add_fact("difficulty_practice")

        time_available = self.ask_choice(
            "\n2. Waktu belajar di luar kuliah per hari:",
            [("1", "Kurang dari 1 jam"),
             ("2", "1 sampai 2 jam"),
             ("3", "Lebih dari 2 jam")]
        )
        if time_available == "1":
            self.add_fact("time_limited")

        target = self.ask_choice(
            "\n3. Target nilai yang ingin dicapai:",
            [("1", "Lulus atau memahami dasar"),
             ("2", "Nilai tinggi, sekitar 80 ke atas")]
        )
        if target == "2":
            self.add_fact("target_high")

        if self.ask_yes_no("\n4. Apakah kamu sering lupa materi yang dipelajari?"):
            self.add_fact("often_forget")
        if self.ask_yes_no("5. Apakah ujian akan berlangsung dalam 7 hari?"):
            self.add_fact("exam_soon")

        learning_style = self.ask_choice(
            "\n6. Cara belajar yang paling kamu sukai:",
            [("1", "Melihat diagram, gambar, atau video"),
             ("2", "Belajar sendiri"),
             ("3", "Diskusi dengan teman"),
             ("4", "Belum memiliki preferensi")]
        )
        if learning_style == "1":
            self.add_fact("prefer_visual")
        elif learning_style == "2":
            self.add_fact("prefer_solo")
        elif learning_style == "3":
            self.add_fact("prefer_group")

    def show_report(self):
        print("\n" + "=" * 65)
        print("HASIL REKOMENDASI METODE BELAJAR")
        print("=" * 65)
        recommended = [
            fact for fact in self.method_details if fact in self.facts
        ]
        if not recommended:
            print("Belum ada metode spesifik yang direkomendasikan.")
            print("Evaluasi kembali kondisi dan tujuan belajar.")
        else:
            for number, fact in enumerate(recommended, start=1):
                name, description = self.method_details[fact]
                print(f"\n{number}. {name}")
                print(f"   Saran: {description}")

        print("\n" + "-" * 65)
        print("JEJAK INFERENSI (EXPLANATION FACILITY)")
        print("-" * 65)
        active_rules = [item for item in self.trace if item["type"] == "RULE"]
        if not active_rules:
            print("Tidak ada aturan yang aktif.")
        else:
            for step in active_rules:
                print(f"\n[{step['rule_id']}] {step['name']}")
                print("  IF   :", " AND ".join(step["conditions"]))
                print("  THEN :", step["conclusion"])
                print("  Alasan:", step["explanation"])

        print("\n" + "-" * 65)
        print("FAKTA AKHIR DALAM WORKING MEMORY")
        print("-" * 65)
        for fact in sorted(self.facts):
            print("-", fact)
        print("\nJumlah aturan aktif:", len(self.fired_rules))
        print("Catatan: rekomendasi adalah panduan berdasarkan aturan yang dibuat,")
        print("bukan jaminan peningkatan nilai atau penilaian ilmiah terhadap individu.")


def main():
    system = ExpertSystemBelajar()
    system.collect_input()
    system.forward_chaining()
    system.show_report()


if __name__ == "__main__":
    main()
