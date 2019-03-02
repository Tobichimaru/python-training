from multiprocessing import Process
from abc import abstractmethod


class Philosopher(Process):
    def __init__(self, id, stop_event, left_fork, right_fork, eat_time, think_time,*args,**kwargs):
        super(Philosopher, self).__init__()
        self.left_fork = left_fork
        self.right_fork = right_fork
        self.eat_time = eat_time
        self.think_time = think_time

        # info 
        self.id = id  # int
        self.dinner_end = stop_event # multiprocessing.Event

    @abstractmethod
    def dining(self):
        pass

    def think(self):
        pass

    def eat(self):
        pass


class Fork(object):
    def __init__(self,id,*args,**kwargs): 
        self.id = id # int

    def take(self, timeout=None):
        """
        :return: True on success, False otherwise
        """
        pass

    def release(self, timeout=None):
        pass
