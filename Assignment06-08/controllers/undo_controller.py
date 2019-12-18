from typing import List

from structures import Operation


class UndoController:
    def __init__(self):
        self._duringUndo = False
        self._undo_operations: List[Operation] = []
        self._redo_operations: List[Operation] = []

    def record_operation(self, operation: Operation):
        if self._duringUndo:
            return
        self._undo_operations.append(operation)
        self._redo_operations.clear()

    def undo(self):
        operation = self._undo_operations.pop()
        operation.undo()
        self._redo_operations.append(operation)

    def redo(self):
        operation = self._redo_operations.pop()
        operation.redo()
        self._undo_operations.append(operation)
