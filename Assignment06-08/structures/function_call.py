from typing import Callable


class FunctionCall:
    def __init__(self, function: Callable, *parameters):
        self._function = function
        self._params = parameters

    def call(self):
        self._function(*self._params)

    def __call__(self, *args, **kwargs):
        self.call()
