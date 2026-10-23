
import random


class Environment:
    def __init__(self, width, height, resource_count=5):
        self.width = width
        self.height = height
        self.agents = []

        # Membuat posisi resource yang unik
        positions = [
            (x, y)
            for x in range(width)
            for y in range(height)
        ]

        self.resources = set(
            random.sample(positions, min(resource_count, len(positions)))
        )

    def add_agent(self, agent):
        self.agents.append(agent)

    def is_valid_position(self, x, y):
        return 0 <= x < self.width and 0 <= y < self.height

    def display(self, step):
        print(f"\n--- Simulasi Langkah ke-{step} ---")

        for y in range(self.height):
            row = ""

            for x in range(self.width):
                agent_here = next(
                    (a for a in self.agents if (a.x, a.y) == (x, y)),
                    None
                )

                if agent_here:
                    row += f" [{agent_here.name[0]}] "
                elif (x, y) in self.resources:
                    row += "  $  "
                else:
                    row += "  .  "

            print(row)

        print(f"Sisa resource: {len(self.resources)}")


class ForagingAgent:
    def __init__(self, name, env):
        self.name = name
        self.env = env
        self.score = 0

        # Memilih posisi awal secara acak
        self.x = random.randint(0, env.width - 1)
        self.y = random.randint(0, env.height - 1)

    def perceive_and_act(self):
        current_position = (self.x, self.y)

        # Perceive: memeriksa resource di posisi saat ini
        if current_position in self.env.resources:
            self.env.resources.remove(current_position)
            self.score += 1

            print(
                f"[{self.name}] Mengambil resource di "
                f"{current_position}. Skor: {self.score}"
            )
            return

        # Act: bergerak satu sel ke arah acak
        moves = [
            (-1, 0),  # Kiri
            (1, 0),   # Kanan
            (0, -1),  # Atas
            (0, 1)    # Bawah
        ]

        random.shuffle(moves)

        for dx, dy in moves:
            new_x = self.x + dx
            new_y = self.y + dy

            if self.env.is_valid_position(new_x, new_y):
                self.x = new_x
                self.y = new_y
                break


def main():
    # Membuat environment
    env = Environment(width=5, height=5, resource_count=5)

    # Membuat dua agen
    agent1 = ForagingAgent("Alpha", env)
    agent2 = ForagingAgent("Beta", env)

    env.add_agent(agent1)
    env.add_agent(agent2)

    total_steps = 30

    for step in range(1, total_steps + 1):
        env.display(step)

        for agent in env.agents:
            agent.perceive_and_act()

        # Menghentikan simulasi jika semua resource terkumpul
        if not env.resources:
            print("\nSemua resource berhasil dikumpulkan!")
            break

    # Menampilkan hasil akhir
    print("\n--- Hasil Akhir Simulasi ---")
    print(f"Skor Alpha: {agent1.score}")
    print(f"Skor Beta: {agent2.score}")
    print(f"Total resource terkumpul: "
          f"{agent1.score + agent2.score}")
    print(f"Sisa resource: {len(env.resources)}")


if __name__ == "__main__":
    main()
