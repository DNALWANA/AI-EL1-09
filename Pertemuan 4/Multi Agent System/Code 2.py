import random

class Environment:
    def _init_(self, width, height):
        self.width = width
        self.height = height
        # Menempatkan beberapa sumber daya di grid (koordinat x, y)
        self.resources = {(random.randint(0, width-1), random.randint(0, height-1)) for _ in range(5)}
        self.agents = []

    def add_agent(self, agent):
        self.agents.append(agent)

    def is_valid_position(self, x, y):
        return 0 <= x < self.width and 0 <= y < self.height

    def display(self, step):
        print(f"\n--- Simulasi Langkah ke-{step} ---")
        for y in range(self.height):
            row_str = ""
            for x in range(self.width):
                # Cek apakah ada agen di posisi ini
                agent_here = next((a for a in self.agents if a.x == x and a.y == y), None)
                if agent_here:
                    row_str += f" [{agent_here.name[0]}] "
                elif (x, y) in self.resources:
                    row_str += "  $  "  # Tanda sumber daya
                else:
                    row_str += "  .  "  # Area kosong
            print(row_str)
        print(f"Sisa Resource di Environment: {len(self.resources)}")


class ForagingAgent:
    def _init_(self, name, env):
        self.name = name
        self.env = env
        self.x = random.randint(0, env.width - 1)
        self.y = random.randint(0, env.height - 1)
        self.score = 0

    def perceive_and_act(self):
        # Perilaku reaktif: Cek apakah di posisi saat ini ada resource
        if (self.x, self.y) in self.env.resources:
            self.env.resources.remove((self.x, self.y))
            self.score += 1
            print(f"[{self.name}] Menemukan dan mengambil resource di ({self.x}, {self.y})! Skor: {self.score}")
        else:
            # Bergerak secara acak ke arah tetangga (Aturan reaktif: arah random)
            moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            dx, dy = random.choice(moves)
            new_x, new_y = self.x + dx, self.y + dy

            if self.env.is_valid_position(new_x, new_y):
                self.x, new_y = new_x, new_y  # Update posisi x
                self.y = new_y                # Update posisi y


# ============================================================
# PROGRAM UTAMA
# ============================================================
def main():
    # Buat Environment ukuran 5x5
    env = Environment(width=5, height=5)

    # Buat beberapa agen otonom
    agent1 = ForagingAgent("Alpha", env)
    agent2 = ForagingAgent("Beta", env)

    env.add_agent(agent1)
    env.add_agent(agent2)

    # Jalankan simulasi selama beberapa siklus (steps)
    total_steps = 6
    for step in range(1, total_steps + 1):
        env.display(step)
        
        # Setiap agen menjalankan fungsi persepsi dan aksinya
        for agent in env.agents:
            agent.perceive_and_act()
            
        # Berhenti jika semua resource sudah habis
        if len(env.resources) == 0:
            print("\nSemua resource telah habis dikumpulkan oleh agen!")
            break

    print("\n--- Hasil Akhir Simulasi ---")
    print(f"Skor {agent1.name}: {agent1.score}")
    print(f"Skor {agent2.name}: {agent2.score}")


if _name_ == "_main_":
    main()
