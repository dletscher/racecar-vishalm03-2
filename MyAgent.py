import random

class Agent:
    def chooseAction(self, observations, possibleActions):
        lidar = observations['lidar']
        velocity = observations['velocity']

        left, mid_left  , center, mid_right, right = lidar
        side_balance = left - right
        if velocity < 0.05:
            return ('straight','accelerate')
        if left < 0.2:
            return('right','brake')
        if right < 0.2:
            return('left','brake')
        if side_balance > 0.25:
            return('left','brake')
        elif side_balance > 0.1:
            return('left','coast')
        elif side_balance < -0.25:
            return('right','brake')
        elif side_balance < -0.1:
            return('right','coast')
        if velocity < 0.5:
            return('straight','accelerate')
        else:
            return('straight','coast') 