# Futures
from __future__ import annotations
from __future__ import unicode_literals
from __future__ import print_function

# Generic/Built-in

# Other Libs
import numpy as np

# Owned
from ..nodes import Node

__all__ = ['Edge']
tol = 1e-5


class Edge:

    """Edge object"""

    def __init__(self, start: Node, end: Node, enforced: bool = False):
        self.__data = [None, None]
        if end.x > start.x:
            self.__data[0] = start
            self.__data[1] = end
        elif end.x < start.x:
            self.__data[0] = end
            self.__data[1] = start
        else:
            if end.y > start.y:
                self.__data[0] = start
                self.__data[1] = end
            elif end.y < start.y:
                self.__data[0] = end
                self.__data[1] = start
            else:
                raise ValueError('Edge init node error')

        if not isinstance(enforced, bool):
            raise ValueError('Enforced is not boolean')

        self.__center: Node | None = None
        self.__enforced = enforced
        self.__iter: int = 0
        self.__length: float | None = None
        self.__normal: np.ndarray | None = None
        self.__vector: np.ndarray | None = None

    @property
    def center(self) -> Node | None:
        if self.__center is None:
            x = 0.5 * (self[0].x + self[1].x)
            y = 0.5 * (self[0].y + self[1].y)
            self.__center = Node(x, y)
        return self.__center

    @property
    def enforced(self) -> bool:
        return self.__enforced

    @property
    def length(self) -> float | None:
        if self.__length is None:
            dx = abs(self[0].x - self[1].x)
            dy = abs(self[0].y - self[1].y)
            self.__length = (dx ** 2 + dy ** 2) ** 0.5
        return self.__length

    @property
    def normal(self) -> np.ndarray | None:
        if self.__normal is None:
            self.__normal = np.array([-self.vector[1], self.vector[0]]) / self.length
        return self.__normal

    @property
    def vector(self) -> np.ndarray | None:
        if self.__vector is None:
            dx = self[1].x - self[0].x
            dy = self[1].y - self[0].y
            self.__vector = np.array([dx, dy])
        return self.__vector

    def split(self, point: Node | None = None) -> list[Node]:
        if point is None:
            point = self.center
        else:
            if not isinstance(point, Node):
                raise ValueError('point is not node')
            if self.__distance(point) > tol:
                raise ValueError('point is not on the edge')

        e1 = Edge(self[0], point, enforced=self.enforced)
        e2 = Edge(point, self[1], enforced=self.enforced)
        return [e1, e2]

    def __distance(self, point: Node) -> float:
        x21 = self[1].x - self[0].x
        y21 = self[1].y - self[0].y
        num = abs(x21 * (self[0].y - point.y) - (self[0].x - point.x) * y21)
        den = (x21 ** 2 + y21 ** 2) ** 0.5
        return num / den

    def __len__(self) -> int:
        return 2

    def __getitem__(self, index) -> Node:
        return self.__data[index]

    def __iter__(self) -> Edge:
        self.__iter = 0
        return self

    def __next__(self) -> Node:
        if self.__iter < 2:
            output = self.__data[self.__iter]
            self.__iter += 1
            return output
        else:
            raise StopIteration

    def __str__(self) -> str:
        return '[{}\n {}]'.format(self[0], self[1])

    def __repr__(self) -> str:
        return 'Edge([{}\n      {}])'.format(self[0], self[1])

    def __ne__(self, other: Edge) -> bool:
        return not self.__eq__(other)

    def __eq__(self, other: Edge) -> bool:
        return isinstance(other, Edge) and hash(self) == hash(other)

    def __hash__(self) -> int:
        return hash(tuple([self[0], self[1], self.center, self.enforced, self.length]))
