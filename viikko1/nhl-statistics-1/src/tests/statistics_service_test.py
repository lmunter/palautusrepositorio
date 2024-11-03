import unittest
from statistics_service import StatisticsService, SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_top_goals_palauttaa_oikean_tuloksen(self):
        result = self.stats.top(4, SortBy.GOALS)
        useful_result = []
        for i in result:
            useful_result.append(str(i))
        self.assertEqual(useful_result, [
            "Lemieux PIT 45 + 54 = 99",
            "Yzerman DET 42 + 56 = 98",
            "Kurri EDM 37 + 53 = 90",
            "Gretzky EDM 35 + 89 = 124",
            "Semenko EDM 4 + 12 = 16"
        ])

    def test_top_points_palauttaa_oikean_tuloksen(self):
        result = self.stats.top(4, SortBy.POINTS)
        useful_result = []
        for i in result:
            useful_result.append(str(i))
        self.assertEqual(useful_result, [
            "Gretzky EDM 35 + 89 = 124",
            "Lemieux PIT 45 + 54 = 99",
            "Yzerman DET 42 + 56 = 98",
            "Kurri EDM 37 + 53 = 90",
            "Semenko EDM 4 + 12 = 16"
        ])

    def test_top_assists_palauttaa_oikean_tuloksen(self):
        result = self.stats.top(4, SortBy.ASSISTS)
        useful_result = []
        for i in result:
            useful_result.append(str(i))
        self.assertEqual(useful_result, [
            "Gretzky EDM 35 + 89 = 124",
            "Yzerman DET 42 + 56 = 98",
            "Lemieux PIT 45 + 54 = 99",
            "Kurri EDM 37 + 53 = 90",
            "Semenko EDM 4 + 12 = 16"
        ])

    def test_team_palauttaa_oikean_tuloksen(self):
        result = self.stats.team("EDM")
        self.assertEqual(len(result), 3)

    def test_search_ei_hallusinoi_pelaajia(self):
        result = self.stats.search("Koivu")
        self.assertEqual(result, None)

    def test_search_palauttaa_oikean_tuloksen(self):
        result = self.stats.search("Kurri")
        self.assertEqual(str(result), "Kurri EDM 37 + 53 = 90")