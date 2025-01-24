import unittest
from module_12_1 import Runner

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        runner = Runner("Test Walk")
        for i in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    def test_run(self):
        runner = Runner("Test Run")
        for i in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    def test_challenge(self):
        walker = Runner("Test Walk")
        runner = Runner("Test Run")

        for i in range(10):
            walker.walk()
            runner.run()

        self.assertNotEqual(walker.distance, runner.distance)

if __name__ == '__main__':
    unittest.main()
