import unittest
from module_12_2 import Runner, Tournament

# Декоратор для пропуска тестов, если is_frozen = True
def skip_if_frozen(test_method):
    def wrapper(self, *args, **kwargs):
        if self.is_frozen:
            self.skipTest("Тесты в этом кейсе заморожены")
        else:
            test_method(self, *args, **kwargs)
    return wrapper

class RunnerTest(unittest.TestCase):
    is_frozen = False  # Тесты RunnerTest не заморожены

    def setUp(self):
        self.runner = Runner("Усэйн", speed=10)

    @skip_if_frozen
    def test_run(self):
        self.runner.run()
        self.assertEqual(self.runner.distance, 20)

    @skip_if_frozen
    def test_walk(self):
        self.runner.walk()
        self.assertEqual(self.runner.distance, 10)

    @skip_if_frozen
    def test_challenge(self):
        self.runner.run()
        self.runner.walk()
        self.assertEqual(self.runner.distance, 30)

class TournamentTest(unittest.TestCase):
    is_frozen = True  # Тесты TournamentTest заморожены

    def setUp(self):
        self.runner1 = Runner("Усэйн", speed=10)
        self.runner2 = Runner("Андрей", speed=9)
        self.runner3 = Runner("Ник", speed=3)

    @skip_if_frozen
    def test_first_tournament(self):
        tournament = Tournament(90, self.runner1, self.runner3)
        results = tournament.start()
        self.assertTrue(results[max(results.keys())] == self.runner3)

    @skip_if_frozen
    def test_second_tournament(self):
        tournament = Tournament(90, self.runner2, self.runner3)
        results = tournament.start()
        self.assertTrue(results[max(results.keys())] == self.runner3)

    @skip_if_frozen
    def test_third_tournament(self):
        tournament = Tournament(90, self.runner1, self.runner2, self.runner3)
        results = tournament.start()
        self.assertTrue(results[max(results.keys())] == self.runner3)

if __name__ == "__main__":
    unittest.main()