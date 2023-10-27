import tqdm

from gym_super_mario_bros import SuperMarioBrosEnv

env = SuperMarioBrosEnv()

DONE = True

try:
    for _ in tqdm.tqdm(range(5000)):
        if DONE is True:
            state = env.reset()
            DONE = False
        else:
            state, reward, done, info = env.step(env.action_space.sample())
except KeyboardInterrupt:
    pass
