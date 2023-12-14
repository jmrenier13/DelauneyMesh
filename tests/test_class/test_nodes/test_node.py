# Futures

# Generic/Built-in

# Other Libs
import pytest

# Owned
from delauneymesh import Node

tol = 1e-5


@pytest.mark.parametrize(
    'x, y, check',
    [
        (-1, -1, True),
        (-1, 0, True),
        (-1, 1, True),
        (0, -1, True),
        (0, 0, True),
        (0, 1, True),
        (1, -1, True),
        (1, 0, True),
        (1, 1, True),
        (-0.5, -0.5, True),
        (-0.5, 0.5, True),
        (0.5, -0.5, True),
        (0.5, 0.5, True),
        ('1', '1', True),
        ('a', 1, False),
        (1, 'a', False)
    ]
)
def test_init(x, y, check):
    if check:
        _ = Node(x, y)
    else:
        with pytest.raises(ValueError):
            _ = Node(x, y)


@pytest.mark.parametrize(
    'x',
    [
        (-2),
        (-1),
        (0),
        (1),
        (2)
    ]
)
def test_x(x):
    node = Node(x, 0)
    assert node.x == pytest.approx(float(x), tol)


@pytest.mark.parametrize(
    'y',
    [
        (-2),
        (-1),
        (0),
        (1),
    ]
)
def test_y(y):
    node = Node(0, y)
    assert node.y == pytest.approx(float(y), tol)


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
def test_str(x, y):
    node = Node(x, y)
    assert str(node) == '[{x} {y}]'.format(x=float(x), y=float(y))


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
def test_repr(x, y):
    node = Node(x, y)
    assert repr(node) == 'Node([{x} {y}])'.format(x=float(x), y=float(y))


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
def test_logic(x1, y1, x2, y2):
    node1 = Node(x1, y1)
    node2 = Node(x2, y2)
    assert node1 == node1
    assert node2 == node2
    assert node1 != node2

    node2._Node__x = float(x1)
    node2._Node__y = float(y1)

    assert node1 == node2
