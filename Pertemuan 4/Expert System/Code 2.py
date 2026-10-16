def collect_input(self):
        print("=" * 65)
        print("EXPERT SYSTEM REKOMENDASI METODE BELAJAR")
        print("Artificial Intelligence - Rule-Based Expert System")
        print("=" * 65)

        print("\nJawab pertanyaan berikut sesuai kondisi kamu.")
        print("Untuk pertanyaan ya/tidak, masukkan y atau n.\n")

        difficulty = self.ask_choice(
            "1. Kesulitan belajar yang paling sering dialami:",
            [
                ("1", "Sulit memahami konsep"),
                ("2", "Sulit mengerjakan soal"),
                ("3", "Keduanya"),
                ("4", "Tidak ada kesulitan utama")
            ]
        )

        if difficulty in ("1", "3"):
            self.add_fact("difficulty_concept")
        if difficulty in ("2", "3"):
            self.add_fact("difficulty_practice")

        time_available = self.ask_choice(
            "\n2. Waktu belajar di luar kuliah per hari:",
            [
                ("1", "Kurang dari 1 jam"),
                ("2", "1 sampai 2 jam"),
                ("3", "Lebih dari 2 jam")
            ]
        )

        if time_available == "1":
            self.add_fact("time_limited")

        target = self.ask_choice(
            "\n3. Target nilai yang ingin dicapai:",
            [
                ("1", "Lulus atau memahami dasar"),
                ("2", "Nilai tinggi, sekitar 80 ke atas")
            ]
        )

        if target == "2":
            self.add_fact("target_high")

        if self.ask_yes_no("\n4. Apakah kamu sering lupa materi yang dipelajari?"):
            self.add_fact("often_forget")

        if self.ask_yes_no("5. Apakah ujian akan berlangsung dalam 7 hari?"):
            self.add_fact("exam_soon")

        learning_style = self.ask_choice(
            "\n6. Cara belajar yang paling kamu sukai:",
            [
                ("1", "Melihat diagram, gambar, atau video"),
                ("2", "Belajar sendiri"),
                ("3", "Diskusi dengan teman"),
                ("4", "Belum memiliki preferensi")
            ]
        )

        if learning_style == "1":
            self.add_fact("prefer_visual")
        elif learning_style == "2":
            self.add_fact("prefer_solo")
        elif learning_style == "3":
            self.add_fact("prefer_group")

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

    # --------------------------------------------------------
    # EXPLANATION FACILITY DAN LAPORAN
    # --------------------------------------------------------
    def show_report(self):
        print("\n" + "=" * 65)
        print("HASIL REKOMENDASI METODE BELAJAR")
        print("=" * 65)

        recommended_methods = [
            fact for fact in self.method_details
            if fact in self.facts
        ]

        if not recommended_methods:
            print("Belum ada metode spesifik yang direkomendasikan.")
            print("Coba evaluasi kembali kondisi dan tujuan belajar.")
        else:
            for index, fact in enumerate(recommended_methods, start=1):
                name, description = self.method_details[fact]
                print(f"\n{index}. {name}")
                print(f"   Saran: {description}")

        print("\n" + "-" * 65)
        print("ALASAN SISTEM MEMBERIKAN REKOMENDASI")
        print("-" * 65)

        active_rules = [
            item for item in self.trace
            if item["type"] == "RULE"
        ]

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
        print(
            "Catatan: rekomendasi merupakan panduan awal berdasarkan "
            "aturan yang dirancang, bukan jaminan peningkatan nilai."
        )


# ============================================================
# PROGRAM UTAMA
# ============================================================
def main():
    system = ExpertSystemBelajar()
    system.collect_input()
    system.forward_chaining()
    system.show_report()


if _name_ == "_main_":
    main()
