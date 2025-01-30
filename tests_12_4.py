import unittest
import logging
from module_12_4 import Runner

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    filename="runner_tests.log",
    filemode="w",
    encoding="utf-8",
    format="%(levelname)s: %(message)s"
)

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        try:
            # Передаем отрицательное значение скорости
            runner = Runner("Усэйн", speed=-10)
            runner.walk()
            logging.info('"test_walk" выполнен успешно')
        except ValueError as e:
            logging.warning(f"Неверная скорость для Runner: {e}")

    def test_run(self):
        try:
            # Передаем не строку в name
            runner = Runner(123, speed=10)
            runner.run()
            logging.info('"test_run" выполнен успешно')
        except TypeError as e:
            logging.warning(f"Неверный тип данных для объекта Runner: {e}")

if __name__ == "__main__":
    unittest.main()