import copy
import random

class Hat:

  def __init__(self, **kwargs):
    self.contents = [
        key for key, value in kwargs.items() for int in range(value)
    ]

  def draw(self, num):
    if len(self.contents) > num:
      items_to_remove = random.sample(self.contents, num)
      for item in items_to_remove:
        self.contents.remove(item)
      return items_to_remove
    else:
      items_to_remove = self.contents
      self.contents = []
      return items_to_remove


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

  balls_matched = 0
  experiments_run = 0

  while experiments_run < num_experiments:
    hat_copy = copy.deepcopy(hat)
    balls_drawn = hat_copy.draw(num_balls_drawn)
    balls_drawn_dict = {x: balls_drawn.count(x) for x in balls_drawn}
    if all(value <= balls_drawn_dict.get(key, 0)
           for key, value in expected_balls.items()):
      balls_matched += 1
    experiments_run += 1
  probability = balls_matched / num_experiments
  return probability
