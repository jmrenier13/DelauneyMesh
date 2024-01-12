# Futures
from __future__ import annotations
from __future__ import unicode_literals
from __future__ import print_function

# Generic/Built-in

# Other Libs

# Owned

__all__ = ['Node']


class Node:

    """
    Class of a 2D node

    Parameters
    ----------
    x : float
        x can be any value.
    y : float
        y can be any value.

    """

    def __init__(self, x: float, y: float):
        self.__x = float(x)
        self.__y = float(y)

    @property
    def x(self) -> float:
        return self.__x

    @property
    def y(self) -> float:
        return self.__y

    def __str__(self) -> str:
        return '[{x} {y}]'.format(x=self.x, y=self.y)

    def __repr__(self) -> str:
        return 'Node(x={x} y={y})'.format(x=self.x, y=self.y)

    def __ne__(self, other: Node) -> bool:
        return not self.__eq__(other)

    def __eq__(self, other: Node) -> bool:
        return isinstance(other, Node) and hash(self) == hash(other)

    def __hash__(self) -> int:
        return hash(tuple([self.x, self.y, self.x + self.y]))
