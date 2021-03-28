from project.hero import Hero

import unittest

class TestHero(unittest.TestCase):
    def setUp(self):
        self.hero = Hero("Wizard", 70, 6000.00, 1500.00)
        self.enemy = Hero("Barbarian", 80, 10000.00, 2000.00)
        self.mario = Hero("Mario", 1, 100.00, 100.00)

    def test_init(self):
        self.assertEqual(self.hero.username, "Wizard")
        self.assertEqual(self.hero.level, 70)
        self.assertEqual(self.hero.health, 6000.00)
        self.assertEqual(self.hero.damage, 1500.00)

    def test_str(self):
        self.assertEqual(self.hero.__str__(), f"Hero Wizard: {self.hero.level} lvl\n"
                                              f"Health: {self.hero.health}\nDamage: {self.hero.damage}\n")

    def test_fight_with_yourself(self):
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.hero)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_hero_with_zero_health(self):
        self.hero.health = 0
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_enemy_with_zero_health(self):
        self.enemy.health = 0
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.enemy)
        self.assertEqual(f"You cannot fight {self.enemy.username}. He needs to rest", str(ex.exception))

    def test_fight_draw_game(self):
        self.hero.battle(self.enemy)
        self.assertEqual(self.hero.health, -154000.00)
        self.assertEqual(self.enemy.health, -95000.00)
        self.assertRaises(Exception, "Draw")

    def test_fight_for_win(self):
        fight = self.hero.battle(self.mario)
        self.assertEqual(self.hero.level, 71)
        self.assertEqual(self.hero.damage, 1505.00)
        self.assertEqual(self.hero.health, 5905.00)
        self.assertEqual(fight, "You win")

    def test_fight_for_loose(self):
        self.hero = Hero("Wizard", 70, 6000.00, 10.00)
        fight = self.hero.battle(self.enemy)
        self.assertEqual(self.enemy.level, 81)
        self.assertEqual(self.enemy.damage, 2005.00)
        self.assertEqual(self.enemy.health, 9305.00)
        self.assertEqual(fight, "You lose")


