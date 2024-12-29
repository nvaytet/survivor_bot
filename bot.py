# SPDX-License-Identifier: BSD-3-Clause

import numpy as np
from snakes import Instructions


class Bot:
    def __init__(self):
        self.team = "Anaconda"  # This is your team name

    def run(self, dt, board, players, powerups) -> Instructions:
        instructions = Instructions()

        me = players[self.team]

        # Projected position: check what is N pixels ahead?
        n = 8
        hwidth = (me.thickness - 1) // 2
        x = int(me.x)
        y = int(me.y)

        bounds = {
            "U": (x, x + 1, y + hwidth + 1, y + n + 1),
            "D": (x, x + 1, y - n, y - hwidth),
            "L": (x - n, x - hwidth, y, y + 1),
            "R": (x + hwidth + 1, x + n + 1, y, y + 1),
        }

        xmin, xmax, ymin, ymax = bounds[me.direction]
        xmin, xmax = np.clip([xmin, xmax], 0, board.shape[1])
        ymin, ymax = np.clip([ymin, ymax], 0, board.shape[0])

        if np.any(board[ymin:ymax, xmin:xmax] > 0):
            instructions.left = True

        return instructions
