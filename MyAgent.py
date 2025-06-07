import random

class Agent:
    def chooseAction(self, observations, possibleActions):
        lidar = observations['lidar']
        velocity = observations['velocity']

        left, mid_left, center, mid_right, right = lidar
        side_balance = left - right
        if velocity < 0.09:
            return ('straight','accelerate')
        if center == 2.0:
            return('straight', 'coast')
        if left < 0.15:
            return('right','coast')
        if right < 0.15:
            return('left','coast')
        if center > 3.5 and center < 5.0:
            return('straight', 'accelerate')
        if side_balance > 0.35:
            return('left','brake')
        elif side_balance > 0.1:
            return('left','accelerate')
        elif side_balance < -0.35:
            return('right','brake')
        elif side_balance < -0.1:
            return('right','accelerate')
        if velocity < 0.9:
            return('straight','accelerate')
        else:
            return('straight','coast') 