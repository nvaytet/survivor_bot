# SPDX-License-Identifier: BSD-3-Clause

import numpy as np
from tilthenightends import Levelup, LevelupOptions, Vector, Team, Towards


class Leader:
    def __init__(self, hero: str):
        self.hero = hero
        self.next_turn = 5.0
        self.vector = Vector(1, 1)

    def run(self, t, dt, monsters, players) -> Vector | Towards | None:
        if t > self.next_turn:
            self.vector = Vector(*np.random.random(2) * 2 - 1)
            self.next_turn += 5.0
        return self.vector


class Follower:
    def __init__(self, hero: str, following: str):
        self.hero = hero
        self.following = following

    def run(self, t, dt, monsters, players) -> Vector | Towards | None:
        for player in players:
            if player["hero"] == self.following:
                return Towards(player["x"], player["y"])
        return None


class Brain:
    def __init__(self):
        self.switch = True
        return

    def levelup(self, t: float, info: dict, players: dict) -> Levelup:
        if self.switch:
            out = Levelup("alaric", LevelupOptions.player_speed)
        else:
            out = Levelup("evelyn", LevelupOptions.player_health)
        self.switch = not self.switch
        return out
        # return Levelup("alaric", LevelupOptions.player_speed)


team = Team(
    players=[
        Leader(hero="alaric"),
        # Follower(hero="cedric", following="alaric"),
        Follower(hero="kaelen", following="alaric"),
        Follower(hero="garron", following="alaric"),
        Follower(hero="theron", following="alaric"),
        Follower(hero="isolde", following="alaric"),
    ],
    strategist=Brain(),
)
