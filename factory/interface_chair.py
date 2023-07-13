'''
Chair Interface
'''

from abc import ABCMeta, abstractmethod

class IChair(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def get_dimensions():
        'return chair dimensions'
    