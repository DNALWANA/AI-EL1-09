import random

class Environment:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
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
                
                agent_here = next((a for a in self.agents if a.x == x and a.y == y), None)
                if agent_here:
                    row_str += f" [{agent_here.name[0]}] "
                elif (x, y) in self.resources:
                    row_str += "  $  "  
                else:
                    row_str += "  .  "  
            print(row_str)
        print(f"Sisa Resource di Environment: {len(self.resources)}")


class ForagingAgent:
    def __init__(self, name, env):
        self.name = name
        self.env = env
        self.x = random.randint(0, env.width - 1)
        self.y = random.randint(0, env.height - 1)
        self.score = 0

    def perceive_and_act(self):
        
        if (self.x, self.y) in self.env.resources:
            self.env.resources.remove((self.x, self.y))
            self.score += 1
            print(f"[{self.name}] Menemukan dan mengambil resource di ({self.x}, {self.y})! Skor: {self.score}")
        else:
            
            moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            dx, dy = random.choice(moves)
            new_x, new_y = self.x + dx, self.y + dy

            if self.env.is_valid_position(new_x, new_y):
                self.x, new_y = new_x, new_y  
                self.y = new_y                



def main():
    
    env = Environment(width=5, height=5)

    
    agent1 = ForagingAgent("Alpha", env)
    agent2 = ForagingAgent("Beta", env)

    env.add_agent(agent1)
    env.add_agent(agent2)

    
    total_steps = 6
    for step in range(1, total_steps + 1):
        env.display(step)
        
        
        for agent in env.agents:
            agent.perceive_and_act()
            
        
        if len(env.resources) == 0:
            print("\nSemua resource telah habis dikumpulkan oleh agen!")
            break

    print("\n--- Hasil Akhir Simulasi ---")
    print(f"Skor {agent1.name}: {agent1.score}")
    print(f"Skor {agent2.name}: {agent2.score}")


if __name__ == "__main__":
    main()
