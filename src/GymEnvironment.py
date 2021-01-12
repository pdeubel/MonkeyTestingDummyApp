from abc import ABC, abstractmethod


class GymEnvironment(ABC):

    @abstractmethod
    def step(self, action):
        pass

    @abstractmethod
    def reset(self):
        pass

    @abstractmethod
    def close(self):
        pass
