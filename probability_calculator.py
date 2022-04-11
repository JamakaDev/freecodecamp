import random


class Hat(object):

    def __init__(self, **kwargs):
        self.contents = [balls for balls in kwargs for ball in range(kwargs[balls])]

    # Method to randomly draw balls from hat object
    def draw(self, num_balls):
        if num_balls > len(self.contents):
            return self.contents
        random_draw = random.sample(self.contents, num_balls)
        for i in random_draw:
            self.contents.remove(i)
        return random_draw


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    match_counter = 0
    for exp in range(num_experiments):
        tmp_hat = hat.contents
        if num_balls_drawn <= len(tmp_hat):
            draw = random.sample(tmp_hat, num_balls_drawn)
        else:
            draw = tmp_hat
        successful = all([expected_balls[ball_draw] <= draw.count(ball_draw) for ball_draw in expected_balls])
        if successful:
            match_counter += 1
    return match_counter / num_experiments


hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
                         expected_balls={"red": 2, "green": 1},
                         num_balls_drawn=5,
                         num_experiments=2000)
print(probability)
