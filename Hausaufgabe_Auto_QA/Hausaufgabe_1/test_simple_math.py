import pytest
from SimpleMath import SimpleMath

@pytest.fixture
def simple_math():
    return SimpleMath()

@pytest.mark.parametrize("a,expected",[
    (2,4),
    (4,16),
])
def test_positive_square(simple_math,a,expected) :
    assert simple_math.square(a) == expected


@pytest.mark.parametrize("a,expected",[
    (2,8),
    (3,27),
    (-3,-27)
])
def test_positive_cube(simple_math,a,expected) :
    assert simple_math.cube(a) == expected