# SPDX-License-Identifier: BSD-3-Clause

from tilthenightends import Levelup, LevelupOptions, Move, Strategist, Team


class Bot1:
    def __init__(self):
        self.hero = "alaric"

    def run(self, t, dt, monsters, players) -> Move:
        move = Move()
        move.left = True
        return move


class Bot2:
    def __init__(self):
        self.hero = "cedric"

    def run(self, t, dt, monsters, players) -> Move:
        move = Move()
        move.left = True
        move.up = True
        return move


class Bot3:
    def __init__(self):
        self.hero = "evelyn"

    def run(self, t, dt, monsters, players) -> Move:
        move = Move()
        move.up = True
        return move


class Bot4:
    def __init__(self):
        self.hero = "garron"

    def run(self, t, dt, monsters, players) -> Move:
        move = Move()
        move.up = True
        move.right = True
        return move


class Bot5:
    def __init__(self):
        self.hero = "isolde"

    def run(self, t, dt, monsters, players) -> Move:
        move = Move()
        move.right = True
        return move


class Brain:
    def __init__(self):
        # self.bots = []
        # self.bots.append(Bot1())
        # self.bots.append(Bot2())
        # self.bots.append(Bot3())
        # self.bots.append(Bot4())
        # self.bots.append(Bot5())
        return

    def levelup(self, t, dt, players) -> Levelup:
        return Levelup("alaric", LevelupOptions.player_speed)


team = Team(
    players=[Bot1(), Bot2(), Bot3(), Bot4(), Bot5()],
    strategist=Strategist(Brain()),
)
