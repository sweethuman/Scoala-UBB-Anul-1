from .operation import Operation


class CascadedOperation(Operation):
    def __init__(self, *operations: Operation):
        self._operations = operations

    def undo(self):
        # some more assembly required
        for o in self._operations:
            o.undo()

    def redo(self):
        # same
        for o in self._operations:
            o.redo()
