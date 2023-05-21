import pytest
# parametrize

def square(n : int) -> int:
    return n*n

def test_square_1():
    assert square(1) == 1

def test_square_2():
    assert square(2) == 4

def test_square_3():
    assert square(3) == 9







@pytest.mark.parametrize(
    ('input', 'expected'),
    (
            (1, 1),
            (2, 4),
            (3, 9),

    )
)
def test_all_square(input, expected):
    assert square(input) == expected