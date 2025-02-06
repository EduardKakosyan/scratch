import random
import gymnasium as gym  # Use gymnasium instead of gym
import numpy as np
import pygame

env = gym.make("Taxi-v3")
alpha = 0.99  # Learning rate

gamma = 0.95  # Discount rate

epsilon = 1  # Proportion of time random action is taken, 1 always, 0 never
epsilon_decay = 0.9995  # Decay rate of the epsilon value
min_epsilon = 0.01

num_episodes = 10000
max_steps = 100  # Max steps in an episode

q_table = np.zeros((env.observation_space.n, env.action_space.n))


def choose_action(state):
    if random.uniform(0, 1) < epsilon:
        return env.action_space.sample()
    else:
        return np.argmax(q_table[state, :])


for episode in range(num_episodes):
    state, info = env.reset()
    done = False

    for step in range(max_steps):
        action = choose_action(state)

        next_state, reward, terminated, truncated, info = env.step(action)
        done = terminated or truncated
        old_value = q_table[state, action]
        next_max = np.max(q_table[next_state, :])

        q_table[state, action] = (1 - alpha) * old_value + alpha * (
            reward + gamma * next_max
        )

        state = next_state

        if done:
            break

    epsilon = max(min_epsilon, epsilon * epsilon_decay)

# Create a new environment for rendering
env = gym.make("Taxi-v3", render_mode="human")

for episode in range(5):
    state, info = env.reset()
    done = False

    print("Episode", episode)

    for step in range(max_steps):
        env.render()
        pygame.event.pump()
        action = np.argmax(q_table[state, :])

        next_state, reward, terminated, truncated, info = env.step(action)
        done = terminated or truncated
        state = next_state

        if done:
            env.render()
            pygame.event.pump()
            print("Finished episode ", episode, " with reward ", reward)
            break

env.close()
