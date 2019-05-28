import argparse

import cartpole_env
import numpy as np
from pid import PID

#####################################
parser = argparse.ArgumentParser(description='I Love CartPole')

parser.add_argument(
    '--num_episodes',
    type=int,
    default=10,
    help='number of episodes')

parser.add_argument(
    '--max_steps',
    type=int,
    default=100,
    help='max number of steps in one episode')

parser.add_argument(
    '--if_print',
    type=bool,
    default=False,
    help='Print')

parser.add_argument(
    '--if_render',
    type=bool,
    default=False,
    help='Render')

args = parser.parse_args()

#######################################

env = cartpole_env.CartPoleEnv()

policy = PID(1, 0, 1, 100, 10, 50)

#######################################
num_episodes = args.num_episodes
max_steps = args.max_steps
rewards = []


def if_print (str):
    if args.if_print:
        print(str)


for _, episode in enumerate(range(1, num_episodes + 1)):
    if_print("Start episode {}".format(episode))

    observation = env.reset()
    cumulative_reward = 0

    for t in range(max_steps):
        if args.if_render:
            env.render()

        act = policy.act(observation)

        observation, reward, done, info = env.step(act)
        cumulative_reward += reward

        if_print("Cart Position: {}, Cart Velocity: {}, Pole Angle: {}, Pole Velocity At Tip {}"
                 .format(*(observation)))

        if done or t == max_steps - 1:
            if_print("Episode finished after {} timesteps".format(t + 1))
            rewards.append(cumulative_reward)
            break

env.close()

print("Average reward is {}".format(np.average(rewards)))

## Print graphs
