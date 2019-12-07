from .function_call import FunctionCall


class Operation:
    """
    Store the function reference and params for both undo and redo
    """

    def __init__(self, undo_function: FunctionCall, redo_function: FunctionCall):
        self._undo = undo_function
        self._redo = redo_function

    def undo(self):
        self._undo()

    def redo(self):
        self._redo()
