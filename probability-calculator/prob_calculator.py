import copy
import random
# Consider using the modules imported above.

"""
What i learn:

**kwargs = can be used to pass many arguments to a function as a dictionary.

print(kwargs) = {'red': 2, 'blue': 3}
print(type(kwargs)) = <class 'dict'>

print(kwargs['red']) = 2
print(kwargs.get('red')) = 2

print(kwargs.items()) = dict_items([('red', 2), ('blue', 3)])
print(kwargs.keys()) = dict_keys(['red', 'blue'])
print(kwargs.values()) = dict_values([2, 3])
"""

class Hat:
    def __init__(self, **kwargs):
        self.kwargs = kwargs
        self.contents = []
        for key, value in kwargs.items():
            for i in range(value):
                self.contents.append(key)

    def draw(self, num_balls_drawn):
        if num_balls_drawn >= len(self.contents):
            return self.contents
        else:
            balls_drawn = []
            for i in range(num_balls_drawn):
                random_ball = random.choice(self.contents)
                balls_drawn.append(random_ball)
                self.contents.remove(random_ball)
            return balls_drawn
        
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    count = 0
    for i in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        balls_drawn = hat_copy.draw(num_balls_drawn)
        balls_drawn_dict = {}
        for ball in balls_drawn:
            balls_drawn_dict[ball] = balls_drawn_dict.get(ball, 0) + 1
        flag = True
        for key, value in expected_balls.items():
            if key not in balls_drawn_dict.keys():
                flag = False
                break
            elif balls_drawn_dict[key] < value:
                flag = False
                break
        if flag:
            count += 1
    return count / num_experiments

