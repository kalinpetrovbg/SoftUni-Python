from abc import ABC, abstractmethod

class Robot:
    def __init__(self, type):
        self.type = type

    def get_type(self):
        return self.type

    @staticmethod
    def count_sensors():
        pass


class Android(Robot):
    def count_sensors(self):
        return 4


class Chappie(Robot):
    def count_sensors(self):
        return 6


def count_robot_senzors(robots: list):
    for robot in robots:
        print(robot.count_sensors())

robots = [Android('Robocop'), Chappie('XIX')]
count_robot_senzors(robots)
