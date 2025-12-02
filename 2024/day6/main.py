def make_rectangle(x, y, z):
    x1, y1 = x
    x2, y2 = y
    x3, y3 = z

    # Fourth vertex directly calculated
    Dx = x1 ^ x2 ^ x3
    Dy = y1 ^ y2 ^ y3

    return (int(Dx), int(Dy))


class Runner:
    turns = {(0, 1): (1, 0), (1, 0): (0, -1), (0, -1): (-1, 0), (-1, 0): (0, 1)}

    def __init__(self, data):
        self.data = data.splitlines()

    def find_start(self):
        for i in range(len(self.data)):
            for j in range(len(self.data[0])):
                if self.data[i][j] == "^":
                    self.pos = i, j
                elif self.data[i][j] == "#":
                    self.barriers += 1

    def play(self):
        self.movement = -1, 0
        self.visited = {}
        self.barriers = 0
        self.find_start()
        while True:
            if self.visited.get(self.pos, None) == self.movement:
                return -1
            if self.pos not in self.visited:
                # Store the current position with movement information
                self.visited[self.pos] = self.movement
            # print(self.visited)

            next_pos = self.pos[0] + self.movement[0], self.pos[1] + self.movement[1]
            # print(f"checking {next_pos}")
            # Bounds check
            if not 0 <= next_pos[0] < len(self.data[0]) or not 0 <= next_pos[1] < len(
                self.data
            ):
                return len(self.visited)
            # print(f"{self.data[next_pos[0]][next_pos[1]]}")
            if self.data[next_pos[0]][next_pos[1]] == "#":
                # print(f"blocked at {next_pos}")
                # If we hit an obstacle, turn right
                self.movement = self.turns[self.movement]
                continue

            # Proceed
            self.pos = next_pos

    def find_loop_positions(self):
        loop_positions = 0
        for i in range(len(self.data)):
            for j in range(len(self.data[0])):
                if self.data[i][j] in ("#", "^"):
                    continue
                old_line = self.data[i]
                self.data[i] = self.data[i][:j] + "#" + self.data[i][j + 1 :]
                game_length = self.play()
                if game_length == -1:
                    print(i, j)
                    # print("found infinite loop")
                    loop_positions += 1
                self.data[i] = old_line
        return loop_positions


if __name__ == "__main__":
    with open("day6/sample.txt") as file:
        runner = Runner(file.read())
        assert runner.play() == 41
        assert runner.find_loop_positions() == 6

    # with open("day6/input.txt") as file:
    #    runner = Runner(file.read())
    #    print(runner.play())
    #    print(runner.find_loop_positions())

    with open("day6/input2.txt") as file:
        runner = Runner(file.read())
        print(runner.find_loop_positions())
