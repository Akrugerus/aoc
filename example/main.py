class Runner:
    def __init__(self, data):
        self.data = data

    def run(self):
        return


if __name__ == "__main__":
    with open("example/sample.txt") as file:
        runner = Runner(file.read())
        assert runner.run() == None

    with open("example/input.txt") as file:
        runner = Runner(file.read())
        print(runner.run())

    with open("example/input.txt") as file:
        runner = Runner(file.read())
        print(runner.run())
