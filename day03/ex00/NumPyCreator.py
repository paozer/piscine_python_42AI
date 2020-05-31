import numpy as np


class NumPyCreator:
    @staticmethod
    def from_list(self, lst):
        return np.array(lst)

    @staticmethod
    def from_tuple(self, tpl):
        return np.array(tpl)

    @staticmethod
    def from_iterable(self, itr):
        return np.array(itr)

    @staticmethod
    def from_shape(self, shape, value=0):
        return np.full(shape, value)

    @staticmethod
    def random(self, shape):
        return np.random.rand(shape[0], shape[1])

    @staticmethod
    def identity(self, n):
        return np.identity(n)
