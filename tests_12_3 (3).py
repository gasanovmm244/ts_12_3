import Runner
import Runner_Tournament as RT
import unittest

class RunnerTest(unittest.TestCase):
    is_frozen = True

    @unittest.skipIf(is_frozen == False, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        runner = Runner.Runner("TestRunner")
        for i in range(10):
            runner.walk()
        self.assertEqual(runner.distance,50)

    @unittest.skipIf(is_frozen == False, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        runner2 = Runner.Runner("TestRunner")
        for i in range(10):
            runner2.run()
        self.assertEqual(runner2.distance,100)

    @unittest.skipIf(is_frozen == False, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        runner3 = Runner.Runner("Runner1")
        runner4 = Runner.Runner("Runner2")
        for i in range(10):
            runner3.walk()
            runner4.run()
        self.assertNotEqual(runner3.distance,runner4.distance)

class TournamentTest(unittest.TestCase):
    is_frozen = True
    all_results = None

    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    def setUp(self):
        self.r1 = RT.Runner('Усэйн', 10)
        self.r2 = RT.Runner('Андрей', 9)
        self.r3 = RT.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for i, elem in enumerate(cls.all_results):
            print(elem)

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_tournament_1(self):
        t1 = RT.Tournament(90, self.r1, self.r3)
        t1_result = {k: str(x) for k, x in t1.start().items()}
        TournamentTest.all_results.append(t1_result)
        self.assertTrue(t1_result[2], 'Ник')

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_tournament_2(self):
        t2 = RT.Tournament(90, self.r2, self.r3)
        t2_result = {k: str(x) for k, x in t2.start().items()}
        TournamentTest.all_results.append(t2_result)
        self.assertTrue(t2_result[2], 'Ник')

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_tournament_3(self):
        t3 = RT.Tournament(90, self.r2, self.r1, self.r3)
        t3_result = {k: str(x) for k, x in t3.start().items()}
        TournamentTest.all_results.append(t3_result)
        self.assertTrue(t3_result[3], 'Ник')


if __name__ == '__main__':
    unittest.main()