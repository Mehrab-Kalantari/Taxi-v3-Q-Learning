import gym
import random
import numpy as np
from time import sleep


class QLearning:
    def __init__(self, env_name, mode):
        self.env_name = env_name
        self.mode = mode
        self.env = gym.make(self.env_name, render_mode=self.mode)
        self.q_table = np.zeros([self.env.observation_space.n, self.env.action_space.n])

    def learn(self, alpha=0.1, gamma=0.5, epsilon=0.1, iterations=10000):
        for _ in range(iterations):
            state, _ = self.env.reset()
            epochs, penalties, reward = 0, 0, 0
            done = False
            while not done:
                if random.uniform(0, 1) < epsilon:
                    action = self.env.action_space.sample()
                else:
                    action = np.argmax(self.q_table[state])
                next_state, reward, done, _, _ = self.env.step(action)
                old_value = self.q_table[state, action]
                next_max = np.max(self.q_table[next_state])
                new_value = (1 - alpha) * old_value + alpha * (reward + gamma * next_max)
                self.q_table[state, action] = new_value
                if reward == -10:
                    penalties += 1
                state = next_state
                epochs += 1

    def show(self):
        state, _ = self.env.reset()
        print(self.env.render())
        epochs, penalties, reward = 0, 0, 0
        done = False
        while not done:
            action = np.argmax(self.q_table[state])
            state, reward, done, _, _ = self.env.step(action)
            if reward == -10:
                penalties += 1
            epochs += 1
            print(self.env.render())
            sleep(0.5)


if __name__ == '__main__':
    model = QLearning(env_name='Taxi-v3', mode='ansi')
    model.learn()
    model.show()
