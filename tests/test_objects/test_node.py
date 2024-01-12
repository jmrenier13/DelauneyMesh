# Futures

# Generic/Built-in

# Other Libs
import pytest

# Owned
from delauneymesh import Node


@pytest.mark.parametrize(
    'value',
    [
        -2,
        -1,
        0,
        1,
        2
    ]
)
def test_x(value: float) -> None:
    assert Node(value, 0.).x == pytest.approx(value)


@pytest.mark.parametrize(
    'value',
    [
        -2,
        -1,
        0,
        1,
        2
    ]
)
def test_y(value: float) -> None:
    assert Node(0., value).y == pytest.approx(value)


@pytest.mark.parametrize(
    'x, y',
    [
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 0),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1)
    ]
)
def test_str(x, y) -> None:
    assert str(Node(x, y)) == '[{} {}]'.format(float(x), float(y))


@pytest.mark.parametrize(
    'x, y',
    [
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 0),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1)
    ]
)
def test_repr(x, y) -> None:
    assert repr(Node(x, y)) == 'Node(x={} y={})'.format(float(x), float(y))


@pytest.mark.parametrize(
    'x1, y1, x2, y2',
    [
        (-1, -1, 5, 5),
        (-1, 0, 5, 5),
        (-1, 1, 5, 5),
        (0, -1, 5, 5),
        (0, 0, 5, 5),
        (0, 1, 5, 5),
        (1, -1, 5, 5),
        (1, 0, 5, 5),
        (1, 1, 5, 5)
    ]
)
def test_logic(x1, y1, x2, y2) -> None:
    n1 = Node(x1, y1)
    n2 = Node(x2, y2)
    assert n1 != n2

    n2._Node__x = float(x1)
    n2._Node__y = float(y1)
    assert n1 == n2
